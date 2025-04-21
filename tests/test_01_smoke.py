from utils.base_test import BaseTest

from playwright.sync_api import expect


class TestSmoke(BaseTest):
	page_url = ''

	def test_title(self, def_page):
		expect(self.page.get_by_role('heading').first).to_have_text('Welcome to the-internet')
		expect(self.page.get_by_role('listitem')).to_have_count(44)