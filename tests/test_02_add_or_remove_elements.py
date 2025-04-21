from utils.base_test import BaseTest

from playwright.sync_api import expect

class TestAddRemoveElement(BaseTest):
	page_url = '/add_remove_elements/'

	def add_element(self):
		self.page.get_by_role('button', name='Add Element').click()

	def get_number_of_delete_buttons(self):
		return len(self.page.get_by_role('button', name='Delete').all())

	def test_add_element(self, def_page):
		self.add_element()
		assert self.get_number_of_delete_buttons() == 1
		self.add_element()
		self.add_element()
		assert self.get_number_of_delete_buttons() == 3