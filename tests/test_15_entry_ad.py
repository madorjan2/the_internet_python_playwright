import pytest
from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestEntryAd(BaseTest):
	page_url = '/entry_ad'

	@pytest.mark.flaky(reruns=3)
	def test_entry_ad(self, def_page):
		self.page.locator('.modal-footer p').click()
		modal = self.page.locator('.modal')
		modal.wait_for(state='hidden')
		expect(modal).not_to_be_visible()

		self.page.get_by_role('link', name='click here').click()
		expect(modal).to_be_visible()

		self.page.reload()
		expect(modal).to_be_visible()
