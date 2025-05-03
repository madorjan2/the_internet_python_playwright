import os
import time

import pytest
from playwright.sync_api import expect

from utils.base_test import BaseTest


def is_file_downloaded(path, timeout=5, poll_frequency=0.1):
	start_time = time.monotonic()
	while time.monotonic() < start_time + timeout:
		if os.path.exists(path):
			return True
		time.sleep(poll_frequency)
	return False


class TestJQueryMenus(BaseTest):
	page_url = '/jqueryui/menu'

	# we get <div> subtree intercepts pointer event if we try to click regularly, therefore Javascript clicking is necessary
	def click_jquery_element_by_id(self, element_id):
		elem = self.page.locator(f'#{element_id}').element_handle()
		self.page.evaluate('element => element.click()', elem)

	# in the JQuery menu, the button does not have enabled/disabled state
	def test_first_button_is_disabled(self):
		assert 'ui-state-disabled' in (
			self.page.get_by_role('menuitem', name='Disabled').locator('..')
		).get_attribute('class')

	@pytest.mark.parametrize(
		'file_type, element_id',
		[
			('menu.pdf', 'ui-id-6'),
			('menu.csv', 'ui-id-7'),
			('menu.xls', 'ui-id-8'),
		],
	)
	def test_download_file(self, file_type, element_id):
		with self.page.expect_download() as download_info:
			self.click_jquery_element_by_id('ui-id-2')
			self.click_jquery_element_by_id('ui-id-4')
			self.click_jquery_element_by_id(element_id)
		download = download_info.value
		path = os.path.join(self.download_path, download.suggested_filename)
		download.save_as(path)
		assert is_file_downloaded(path)

	def test_back_to_jquery(self):
		self.click_jquery_element_by_id('ui-id-2')
		self.click_jquery_element_by_id('ui-id-5')
		expect(self.page).to_have_url('http://localhost:7080/jqueryui')
