import os
import time

from utils.base_test import BaseTest


def get_downloaded_data(path, timeout=5, polling_interval=0.2):
	start_time = time.monotonic()
	while not os.path.exists(path) and time.monotonic() - start_time < timeout:
		time.sleep(polling_interval)
	if not os.path.exists(path):
		raise FileNotFoundError(f'File could not be found: {path}')
	else:
		with open(path, 'r') as f:
			return f.read()


def get_test_data():
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'test_data', 'test_data_17.txt')
	with open(path, 'r') as f:
		return f.read()


class TestFileDownload(BaseTest):
	page_url = '/download'

	def test_file_download(self):
		with self.page.expect_download() as download_info:
			self.page.get_by_role('link', name='some-file.txt').click()
		download = download_info.value
		path = os.path.join(self.download_path, download.suggested_filename)
		download.save_as(path)
		assert get_downloaded_data(path) == get_test_data()
