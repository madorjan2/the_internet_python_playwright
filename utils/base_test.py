import pytest

class BaseTest(object):
	base_url = 'http://localhost:7080'
	page_url = None

	@pytest.fixture(scope="class", autouse=True)
	def page(self, browser):
		if self.page_url is None:
			raise ValueError(f"Subclass {self.__class__.__name__} must define base_url")
		self.setup_page = browser.new_page()
		self.setup_page.goto(self.base_url + self.page_url)
		yield self.setup_page
		self.setup_page.close()