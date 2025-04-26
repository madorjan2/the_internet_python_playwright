from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestDynamicControls(BaseTest):
	page_url = '/dynamic_controls'

	def test_disappearing_checkbox(self, def_page):
		checkbox = self.page.get_by_role('checkbox')
		expect(checkbox).to_be_visible()

		button_remove_checkbox = self.page.get_by_role('button', name='Remove')
		button_add_checkbox = self.page.get_by_role('button', name='Add')
		button_remove_checkbox.click()
		expect(checkbox).not_to_be_visible()

		button_add_checkbox.click()
		expect(checkbox).to_be_visible()

	def test_disabled_input(self, def_page):
		input_field = self.page.get_by_role('textbox')
		expect(input_field).to_be_disabled()

		button_enable = self.page.get_by_role('button', name='Enable')
		button_disable = self.page.get_by_role('button', name='Disable')
		button_enable.click()

		expect(input_field).to_be_enabled()

		button_disable.click()
		expect(input_field).to_be_disabled()
