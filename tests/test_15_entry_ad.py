import pytest
from playwright.sync_api import expect
from utils.base_test import BaseTest


class TestEntryAd(BaseTest):
	page_url = '/entry_ad'

	def test_modal_close(self):
		p_close = self.page.locator('.modal-footer p')
		p_close.click()
		modal = self.page.locator('.modal')
		expect(modal).not_to_be_visible()

	def test_modal_does_not_reappear(self):
		modal = self.page.locator('.modal')
		p_close = self.page.locator('.modal-footer p')
		p_close.click()
		expect(modal).not_to_be_visible()
		self.page.reload()
		expect(modal).not_to_be_visible()

	@pytest.mark.only_browser(
		'chromium'
	)  # Test is unstable in WebKit and flaky on Firefox on CI
	def test_make_modal_reappear(self):
		modal = self.page.locator('.modal')
		p_close = self.page.locator('.modal-footer p')
		p_close.click()
		expect(modal).not_to_be_visible()

		self.page.get_by_role('link', name='Click here').click()
		self.page.reload()
		expect(modal).to_be_visible()
