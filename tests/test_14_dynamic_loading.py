import pytest
from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestDynamicLoading(BaseTest):
	page_url = '/dynamic_loading'

	@pytest.mark.parametrize('link_name', ['Example 1', 'Example 2'])
	def test_hidden_element(self, def_page, link_name):
		self.page.get_by_role('link', name=link_name).click()
		h4_result = self.page.locator('#finish h4')

		expect(h4_result).not_to_be_visible()

		self.page.get_by_role('button', name='Start').click()

		h4_result.wait_for(state='visible')
		expect(h4_result).to_be_visible()
