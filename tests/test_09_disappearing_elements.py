import time

from playwright.sync_api import expect

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class TestDisappearingElements(BaseTest):
	page_url = '/disappearing_elements'

	def is_gallery_present(self):
		return self.page.get_by_role('link', name='Gallery').count() > 0

	def get_number_of_reloads(self, is_present):
		"""Reloads the page until the gallery is present or 100 times.
		Returns the number of reloads."""
		counter = 0
		while is_present == self.is_gallery_present() and counter < 100:
			self.page.reload()
			counter += 1
		return counter

	def test_reload(self, def_page):
		assert self.get_number_of_reloads(self.is_gallery_present()) < 100
