import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def nav_page(page: Page, request):
    base_url = getattr(request.cls, 'base_url', None)
    page_url = getattr(request.cls, 'page_url', None)
    if base_url and page_url:
        page.goto(base_url + page_url)
    elif base_url:
        page.goto(base_url)
    yield page