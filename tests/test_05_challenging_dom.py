from utils.base_test import BaseTest

import csv
import base64
import pytesseract
import io
import os
from PIL import Image


def read_expected():
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'test_data', 'test_5.csv')
	with open(path, 'r') as testdata_csv:
		csv_reader = csv.reader(testdata_csv)
		testdata_list = list(csv_reader)
	return testdata_list


class TestChallengingDom(BaseTest):
	page_url = '/challenging_dom'

	# given that the buttons have different id and name on each reload
	# we can only use locators to find them
	def get_buttons(self):
		return self.page.locator('//a[@class]').all()

	def get_table(self):
		return self.page.get_by_role('table')

	def get_num_from_dom(self):
		scripts = self.page.locator('//script').all()
		for script in scripts:
			if 'Answer: ' in script.evaluate('(element) => element.innerHTML'):
				return (
					script.evaluate('(element) => element.innerHTML')
					.split('Answer: ')[1]
					.split("'")[0]
					.replace(',', '')
				)
		raise ValueError('No script tag with an answer on page')

	def test_buttons(self):
		for button in self.get_buttons():
			button_id = button.get_attribute('id')
			button.click()
			assert button.get_attribute('id') != button_id

	def test_table(self):
		table_content = []
		trs = self.get_table().get_by_role('row').all()
		for tr in trs:
			tds = tr.get_by_role('cell').all()
			table_content.append(
				[
					td.text_content().replace('\n', '').replace(' ', '')
					for td in tds
				]
			)
		assert table_content == read_expected()

	def test_image(self):
		canvas = self.page.locator('//canvas').element_handle()
		img_base64 = self.page.evaluate(
			"(canvas) => canvas.toDataURL('image/png').substring(21)", canvas
		)
		img_data = Image.open(io.BytesIO(base64.b64decode(img_base64)))
		num = pytesseract.image_to_string(img_data).split(': ')[1].strip()
		assert num == self.get_num_from_dom()
