from utils.base_test import BaseTest


def handle_dialog(dialog):
	assert dialog.type == 'alert'
	assert dialog.message == 'You selected a context menu'
	dialog.accept()


class TestContextMenus(BaseTest):
	base_url = 'https://the-internet.herokuapp.com'
	page_url = '/context_menu'

	def test_context_menu(self, def_page):
		self.page.on('dialog', handle_dialog)
		self.page.locator('#hot-spot').click(button='right')
