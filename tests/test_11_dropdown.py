from utils.base_test import BaseTest

from playwright.sync_api import expect


class TestDropdown(BaseTest):
	page_url = '/dropdown'

	def test_dropdown(self, def_page):
		select = self.page.get_by_role('combobox')
		expect(select.locator('//option[@selected]')).to_have_text(
			'Please select an option'
		)
		options = select.locator('option')
		expect(options).to_have_count(3)
		select.select_option('1')
		expect(select.locator('//option[@selected]')).to_have_text('Option 1')
		expect(options).to_have_count(3)
		select.select_option(label='Option 2')
		expect(select.locator('//option[@selected]')).to_have_attribute(
			'value', '2'
		)
		expect(options.first).to_be_disabled()
