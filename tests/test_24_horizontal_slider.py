from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestHorizontalSlider(BaseTest):
	page_url = '/horizontal_slider'

	def get_slider(self):
		return self.page.get_by_role('slider')

	def get_value(self):
		return self.page.locator('#range')

	def test_click_in_the_middle_by_bbox(self):
		expect(self.get_value()).to_have_text('0')
		bbox = self.get_slider().bounding_box()
		mid_x = bbox['x'] + bbox['width'] / 2
		mid_y = bbox['y'] + bbox['height'] / 2
		self.page.mouse.click(mid_x, mid_y)
		expect(self.get_value()).to_have_text('2.5')

	def test_cursor_keys(self):
		self.get_slider().focus()
		for i in range(10):
			expected_result = int(i * 0.5) if i % 2 == 0 else i * 0.5
			expect(self.get_value()).to_have_text(str(expected_result))
			self.page.keyboard.press('ArrowRight')
		expect(self.get_value()).to_have_text('5')

	def test_dragging(self):
		expect(self.get_value()).to_have_text('0')
		bbox = self.get_slider().bounding_box()
		left_x = bbox['x']
		right_x = bbox['x'] + bbox['width']
		mid_y = bbox['y'] + bbox['height'] / 2
		self.page.mouse.move(left_x, mid_y)
		self.page.mouse.down()
		self.page.mouse.move(right_x + bbox['width'], mid_y)
		self.page.mouse.up()
		expect(self.get_value()).to_have_text('5')
