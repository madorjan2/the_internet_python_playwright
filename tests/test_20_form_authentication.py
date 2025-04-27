from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestFormAuthentication(BaseTest):
	page_url = '/login'

	def fill_form(self, username, password):
		self.page.get_by_role('textbox', name='Username').fill(username)
		self.page.get_by_role('textbox', name='Password').fill(password)
		self.page.get_by_role('button', name='Login').click()

	def test_positive(self):
		username, password = [
			elem.text_content()
			for elem in self.page.get_by_role('emphasis').all()
		]
		self.fill_form(username, password)
		expect(self.page.locator('#flash-messages')).to_contain_text(
			'You logged into a secure area!'
		)

	def test_wrong_username(self):
		username, password = [
			elem.text_content()
			for elem in self.page.get_by_role('emphasis').all()
		]
		self.fill_form(username + '1', password)
		expect(self.page.locator('#flash-messages')).to_contain_text(
			'Your username is invalid!'
		)

	def test_wrong_password(self):
		username, password = [
			elem.text_content()
			for elem in self.page.get_by_role('emphasis').all()
		]
		self.fill_form(username, password + '1')
		expect(self.page.locator('#flash-messages')).to_contain_text(
			'Your password is invalid!'
		)

	def test_empty_username(self):
		password = self.page.get_by_role('emphasis').last.text_content()
		self.fill_form('', password)
		expect(self.page.locator('#flash-messages')).to_contain_text(
			'Your username is invalid!'
		)

	def test_empty_password(self):
		username = self.page.get_by_role('emphasis').first.text_content()
		self.fill_form(username, '')
		expect(self.page.locator('#flash-messages')).to_contain_text(
			'Your password is invalid!'
		)

	def test_empty_username_and_password(self):
		self.fill_form('', '')
		expect(self.page.locator('#flash-messages')).to_contain_text(
			'Your username is invalid!'
		)
