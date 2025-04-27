import os

import pytest
from playwright.sync_api import Page


class BaseTest(object):
	base_url = 'http://localhost:7080'
	page_url = None
	download_path = None
	page: Page

	@pytest.fixture(autouse=True)
	def setup_page(self, def_page):
		self.download_path = self.get_download_folder_path()
		self.clear_download_directory()
		return def_page

	def get_download_folder_path(self):
		this_folder_path = os.path.abspath(
			os.path.join(os.path.realpath(__file__), os.pardir)
		)
		path = os.path.join(
			this_folder_path,
			'..',
			'tests',
			'downloads',
			self.page.context.browser.browser_type.name,
		)
		if not os.path.exists(path):
			os.makedirs(path)
		return path

	def clear_download_directory(self):
		for filename in os.listdir(self.download_path):
			file_path = os.path.join(self.download_path, filename)
			os.remove(file_path)
