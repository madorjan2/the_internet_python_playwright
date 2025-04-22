from utils.base_test import BaseTest

class TestCheckboxes(BaseTest):
	page_url = '/checkboxes'

	def test_checkboxes(self, def_page):
		cb1, cb2 = self.page.get_by_role('checkbox').all()
		assert cb1.is_enabled() and cb2.is_enabled()
		cb1.set_checked(False)
		cb2.set_checked(False)
		assert not cb1.is_checked() and not cb2.is_checked()
		cb1.click()
		assert cb1.is_checked() and not cb2.is_checked()
		cb2.click()
		assert cb1.is_checked() and cb2.is_checked()
		cb1.set_checked(True)
		cb2.set_checked(True)
		assert cb1.is_checked() and cb2.is_checked()
		cb1.set_checked(not cb1.is_checked())
		assert not cb1.is_checked() and cb2.is_checked()
		cb2.set_checked(not cb2.is_checked())
		assert not cb1.is_checked() and not cb2.is_checked()
