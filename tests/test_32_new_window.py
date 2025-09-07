from utils.base_test import BaseTest


class TestNewWindow(BaseTest):
	page_url = '/windows'

	def test_new_page_opens(self, context):
		with context.expect_page() as new_page_info:
			self.page.click('a[href="/windows/new"]')
		new_page = new_page_info.value

		assert new_page.url == self.base_url + '/windows/new'
		assert new_page.locator('h3').inner_text() == 'New Window'
