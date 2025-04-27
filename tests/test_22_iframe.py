from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestIframe(BaseTest):
	page_url = '/iframe'

	def test_iframe(self):
		self.page.get_by_role('button', name='Close').click()
		expect(
			self.page.frame_locator('#mce_0_ifr').locator('[data-id="mce_0"]')
		).to_contain_text('Your content goes here.')
