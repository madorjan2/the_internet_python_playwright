from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestExitIntent(BaseTest):
	page_url = '/exit_intent'

	def test_exit_intent(self):
		viewport_size = self.page.viewport_size
		self.page.mouse.move(viewport_size['width'] / 2, 1)
		self.page.mouse.move(viewport_size['width'] / 2, -5)
		modal = self.page.locator('.modal')
		expect(modal).to_be_visible()
