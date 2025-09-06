import time
from utils.base_test import BaseTest


class TestFloatingMenu(BaseTest):
	page_url = '/floating_menu'
	url = 'http://localhost:7080/floating_menu'

	def are_we_scrolled_down(self, timeout=2, polling_interval=0.2):
		menu = self.page.locator('#menu')
		scroll = float(menu.get_attribute('style')[5:-3])
		start_time = time.monotonic()
		while scroll == 0 and time.monotonic() - start_time < timeout:
			scroll = float(menu.get_attribute('style')[5:-3])
			time.sleep(polling_interval)
		assert scroll > 0, 'Menu is not scrolled down'

	def are_elements_visible(self):
		names = ['Home', 'News', 'Contact', 'About']
		return all(
			[
				self.page.get_by_role('link', name=name).is_visible()
				for name in names
			]
		)

	def test_mouse_wheel(self):
		self.page.mouse.wheel(0, 1000)
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_scroll_to_element(self):
		a_bottom_of_page = self.page.get_by_role(
			'link', name='Elemental Selenium'
		)
		a_bottom_of_page.scroll_into_view_if_needed()
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_javascript_scroll_by(self):
		self.page.evaluate('window.scrollBy(0, 2000)')
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_javascript_scroll_to(self):
		self.page.evaluate('window.scrollTo(0, 2000)')
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_javascript_scroll_into_view(self):
		a_bottom_of_page = self.page.get_by_role(
			'link', name='Elemental Selenium'
		)
		self.page.evaluate(
			'element => element.scrollIntoView()',
			a_bottom_of_page.element_handle(),
		)
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_pagedown(self):
		self.page.keyboard.press('PageDown')
		self.are_we_scrolled_down()
		self.are_elements_visible()
