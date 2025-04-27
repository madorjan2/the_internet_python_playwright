import time


from utils.base_test import BaseTest


class TestHovers(BaseTest):
	page_url = '/infinite_scroll'

	def get_num_of_paragraphs(self):
		return len(self.page.locator('.jscroll-added').all())

	# PageDown key is not scrolling down enough on firefox
	def test_scroll_by_end(self):
		for _ in range(10):
			orig_num = self.get_num_of_paragraphs()
			self.page.keyboard.press('End')
			start_time = time.monotonic()
			while (
				self.get_num_of_paragraphs() == orig_num
				and time.monotonic() - start_time < 5
			):
				time.sleep(0.2)
			assert self.get_num_of_paragraphs() > orig_num

	def test_scroll_by_javascript(self):
		for _ in range(10):
			orig_num = self.get_num_of_paragraphs()
			self.page.evaluate(
				'window.scrollTo(0, document.body.scrollHeight);'
			)
			start_time = time.monotonic()
			while (
				self.get_num_of_paragraphs() == orig_num
				and time.monotonic() - start_time < 5
			):
				time.sleep(0.2)
			assert self.get_num_of_paragraphs() > orig_num
