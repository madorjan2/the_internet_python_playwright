from utils.base_test import BaseTest


class TestAlerts(BaseTest):
	page_url = '/javascript_error'

	def test_homepage_loads_without_errors(self, prenav_page):
		errors = []
		self.page.on('pageerror', lambda msg: errors.append(msg))
		self.page.goto(self.base_url)
		self.page.wait_for_load_state('networkidle')
		assert len(errors) == 0

	def test_page_loads_with_onload_errors(self, prenav_page):
		errors = []
		self.page.on('pageerror', lambda msg: errors.append(msg))
		self.page.goto(self.base_url + self.page_url)
		self.page.wait_for_load_state('networkidle')
		assert len(errors) > 0
