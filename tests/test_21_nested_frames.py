from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestNestedFrames(BaseTest):
	page_url = '/nested_frames'

	def test_nested_frames(self):
		for direction in ['left', 'middle', 'right']:
			expect(
				self.page.frame_locator('[name="frame-top"]')
				.frame_locator(f'[name="frame-{direction}"]')
				.locator('//body')
			).to_contain_text(direction.upper())

		expect(
			self.page.frame_locator('[name="frame-bottom"]').locator('//body')
		).to_contain_text('BOTTOM')
