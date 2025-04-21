from playwright.sync_api import Page


class BaseTest(object):
	base_url = 'http://localhost:7080'
	page_url = None
	page: Page