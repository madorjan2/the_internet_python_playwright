from utils.base_test import BaseTest


class TestShadowDOM(BaseTest):
	page_url = '/shadowdom'

	def test_open_shadow_dom(self):
		first_line = self.page.locator('my-paragraph span')
		second_line = self.page.locator('my-paragraph li').first
		third_line = self.page.locator('my-paragraph li').last

		assert first_line.text_content() == "Let's have some different text!"
		assert second_line.text_content() == "Let's have some different text!"
		assert third_line.text_content() == 'In a list!'
