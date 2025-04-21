import pytest
from playwright.sync_api import Page


@pytest.fixture(scope='function')
def def_page(page: Page, request):
	base_url = getattr(request.cls, 'base_url', None)
	page_url = getattr(request.cls, 'page_url', None)

	if base_url and page_url:
		page.goto(base_url + page_url)
	elif base_url:
		page.goto(base_url)

	# adding self.page to all test cases that use def_page
	if request.instance is not None:
		request.instance.page = page

	yield page


@pytest.fixture(scope='function')
def prenav_page(page: Page, request):
	if request.instance is not None:
		request.instance.page = page

	yield page
