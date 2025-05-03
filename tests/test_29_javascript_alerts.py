from playwright.sync_api import expect

from utils.base_test import BaseTest


def accept_dialog(dialog, text=''):
	if dialog.type == 'prompt':
		dialog.accept(text)
	else:
		dialog.accept('')


def dismiss_dialog(dialog):
	dialog.dismiss()


class TestAlerts(BaseTest):
	page_url = '/javascript_alerts'

	def test_simple_alert(self):
		self.page.on('dialog', accept_dialog)
		self.page.get_by_role('button', name='Click for JS Alert').click()
		expect(self.page.locator('#result')).to_have_text(
			'You successfuly clicked an alert'
		)

	def test_confirm_alert_accept(self):
		self.page.on('dialog', accept_dialog)
		self.page.get_by_role('button', name='Click for JS Confirm').click()
		expect(self.page.locator('#result')).to_have_text('You clicked: Ok')

	def test_confirm_alert_dismiss(self):
		self.page.on('dialog', dismiss_dialog)
		self.page.get_by_role('button', name='Click for JS Confirm').click()
		expect(self.page.locator('#result')).to_have_text(
			'You clicked: Cancel'
		)

	def test_prompt_alert_with_text(self):
		message = 'You are indeed a JS prompt'
		self.page.on('dialog', lambda dialog: accept_dialog(dialog, message))
		self.page.get_by_role('button', name='Click for JS Prompt').click()
		expect(self.page.locator('#result')).to_have_text(
			f'You entered: {message}'
		)

	def test_prompt_alert_without_text(self):
		self.page.on('dialog', accept_dialog)
		self.page.get_by_role('button', name='Click for JS Prompt').click()
		expect(self.page.locator('#result')).to_have_text('You entered:')

	def test_prompt_alert_dismiss(self):
		self.page.on('dialog', dismiss_dialog)
		self.page.get_by_role('button', name='Click for JS Prompt').click()
		expect(self.page.locator('#result')).to_have_text('You entered: null')
