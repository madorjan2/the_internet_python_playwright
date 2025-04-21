from utils.base_test import BaseTest

from playwright.sync_api import expect


class TestSmoke(BaseTest):
	page_url = ''

	def test_title(self, nav_page):
		expect(nav_page.get_by_role('heading').first).to_have_text('Welcome to the-internet')
		expect(nav_page.get_by_role('listitem')).to_have_count(42)