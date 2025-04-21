import base64
import pytest

from utils.base_test import BaseTest
from utils.handle_route import handle_route_wrapper

from playwright.sync_api import expect
from playwright.sync_api._generated import Error as PlaywrightError

valid_auth = base64.encodebytes('admin:admin'.encode()).decode().strip()
invalid_auth = base64.encodebytes('something:other'.encode()).decode().strip()


class TestBasicAuth(BaseTest):
	page_url = '/basic_auth'

	def test_valid_login(self, prenav_page):
		header_modifier = handle_route_wrapper(
			'Authorization', f'Basic {valid_auth}'
		)
		self.page.route(f'**{self.page_url}', header_modifier)
		self.page.goto(self.base_url + self.page_url)
		expect(self.page.get_by_role('heading', level=3)).to_have_text(
			'Basic Auth'
		)
		expect(self.page.get_by_role('paragraph')).to_have_text(
			'Congratulations! You must have the proper credentials.'
		)

	def test_invalid_login(self, prenav_page, pytestconfig):
		header_modifier = handle_route_wrapper(
			'Authorization', f'Basic {invalid_auth}'
		)
		self.page.route(f'**{self.page_url}', header_modifier)

		# if running in headed mode, the Basic Auth login "alert"-like popup will appear
		if pytestconfig.getoption('--headed', False):
			with pytest.raises(PlaywrightError) as error_info:
				self.page.goto(self.base_url + self.page_url)
			assert 'ERR_INVALID_AUTH_CREDENTIALS' in str(error_info.value)
		# in headless mode, we just get to the Not authorized page, same as if we click Cancel in headed mode
		else:
			self.page.goto(self.base_url + self.page_url)
			expect(self.page.locator('body')).to_have_text('Not authorized')
