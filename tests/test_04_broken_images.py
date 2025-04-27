import pytest

from utils.base_test import BaseTest


class TestBrokenImages(BaseTest):
	page_url = '/broken_images'

	@pytest.mark.parametrize(
		'index, expected',
		[
			(1, True),
			(2, True),
			(3, False),
		],
	)
	def test_image_is_broken(self, index, expected):
		xpath_selector = f'//div[@id="content"]//img[{index}]'
		is_broken = self.page.evaluate(
			"""(selector) => {
				const img = document.evaluate(selector, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
				return img ? img.naturalWidth === 0 : true;
			}""",
			xpath_selector,
		)
		assert is_broken == expected
