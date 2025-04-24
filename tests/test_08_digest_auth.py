from urllib.error import HTTPError
from urllib.request import (
	HTTPDigestAuthHandler,
	build_opener,
	HTTPPasswordMgrWithDefaultRealm,
)

import pytest

from utils.base_test import BaseTest

from playwright.sync_api import expect
from playwright.sync_api._generated import Error as PlaywrightError


def handle_route_wrapper(username, password):
	def handle_route(route, request):
		url = request.url

		password_mgr = HTTPPasswordMgrWithDefaultRealm()
		password_mgr.add_password(None, url, username, password)

		handler = HTTPDigestAuthHandler(password_mgr)
		opener = build_opener(handler)

		try:
			response = opener.open(url)
			body = response.read()
			headers = dict(response.headers)

			route.fulfill(
				status=response.getcode(),
				headers=headers,
				content_type=headers.get('Content-Type'),
				body=body,
			)
		except HTTPError:
			route.abort()

	return handle_route


class TestBasicAuth(BaseTest):
	page_url = '/digest_auth'

	def test_valid_login(self, prenav_page):
		self.page.route(
			f'**{self.page_url}', handle_route_wrapper('admin', 'admin')
		)
		self.page.goto(self.base_url + self.page_url)
		expect(self.page.get_by_role('heading', level=3)).to_have_text(
			'Digest Auth'
		)
		expect(self.page.get_by_role('paragraph')).to_have_text(
			'Congratulations! You must have the proper credentials.'
		)

	def test_invalid_login(self, prenav_page, pytestconfig):
		self.page.route(
			f'**{self.page_url}', handle_route_wrapper('something', 'other')
		)

		with pytest.raises(PlaywrightError) as error_info:
			self.page.goto(self.base_url + self.page_url)
			assert 'NS_ERROR_FAILURE' in str(error_info.value)
