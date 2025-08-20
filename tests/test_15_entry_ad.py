# TODO: rewrite, logic is faulty
# should be checking if modal comes back after reload after clicking
import pytest
from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestEntryAd(BaseTest):
	page_url = '/entry_ad'

	@pytest.mark.flaky(reruns=3)
	@pytest.mark.skip_browser('webkit')
	def test_entry_ad(self):
		p_close = self.page.locator('.modal-footer p')
		p_close.click()
		modal = self.page.locator('.modal')
		modal.wait_for(state='hidden')
		expect(modal).not_to_be_visible()

		self.page.reload()

		if modal.count() > 0 and modal.is_visible():
			pytest.fail('Modal is still visible after reload')

		self.page.get_by_role('link', name='click here').click()
		modal.wait_for(state='visible')
		expect(modal).to_be_visible()
