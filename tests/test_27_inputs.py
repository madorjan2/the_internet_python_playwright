from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestInputs(BaseTest):
	page_url = '/inputs'

	def get_input_field(self):
		return self.page.get_by_role('spinbutton')

	def test_accepts_input(self):
		self.get_input_field().fill('123')
		expect(self.get_input_field()).to_have_value('123')

	def test_arrow_keys(self):
		self.get_input_field().fill('123')
		self.get_input_field().press('ArrowUp')
		expect(self.get_input_field()).to_have_value('124')
		self.get_input_field().press('ArrowDown')
		expect(self.get_input_field()).to_have_value('123')

	# ToDo (after multiple browser support implementation): negative branch is browser-dependant, since the accepted input differs (e.g. Firefox accepts all kind of input in number type fields)
