from utils.base_test import BaseTest

from playwright.sync_api import expect


class TestAddRemoveElement(BaseTest):
	page_url = '/add_remove_elements/'

	def add_element(self):
		self.page.get_by_role('button', name='Add Element').click()

	def assert_number_of_delete_buttons(self, num):
		expect(self.page.get_by_role('button', name='Delete')).to_have_count(
			num
		)

	def test_add_element(self, def_page):
		self.add_element()
		self.assert_number_of_delete_buttons(1)
		self.add_element()
		self.add_element()
		self.assert_number_of_delete_buttons(3)
