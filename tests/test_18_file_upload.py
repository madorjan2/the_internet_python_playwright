import os

from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestFileUpload(BaseTest):
	page_url = '/upload'

	def test_file_upload(self):
		with self.page.expect_file_chooser() as fc_info:
			self.page.locator('#file-upload').click()
		file_chooser = fc_info.value
		file_chooser.set_files(
			os.path.join(self.data_path, 'test_data_17.txt')
		)
		self.page.get_by_role('button', name='Upload').click()
		uploaded_files = self.page.locator('#uploaded-files')
		expect(uploaded_files).to_contain_text('test_data_17.txt')
