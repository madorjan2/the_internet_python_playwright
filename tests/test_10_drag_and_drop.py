import pytest
from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestDragAndDrop(BaseTest):
	page_url = '/drag_and_drop'

	# This test constantly fails on webkit
	@pytest.mark.skip_browser('webkit')
	def test_drag_and_drop_with_drag_to(self, def_page):
		left_box = self.page.locator('#column-a')
		right_box = self.page.locator('#column-b')
		expect(left_box).to_have_text('A')
		expect(right_box).to_have_text('B')
		left_box.drag_to(right_box)
		expect(left_box).to_have_text('B')
		expect(right_box).to_have_text('A')

	# This test constantly fails on webkit
	@pytest.mark.skip_browser('webkit')
	def test_drag_and_drop_with_mouse_actions(self, def_page):
		left_box = self.page.locator('#column-a')
		right_box = self.page.locator('#column-b')
		expect(left_box).to_have_text('A')
		expect(right_box).to_have_text('B')
		left_box.hover()
		self.page.mouse.down()
		right_box.hover()
		self.page.mouse.up()
		expect(left_box).to_have_text('B')
		expect(right_box).to_have_text('A')
