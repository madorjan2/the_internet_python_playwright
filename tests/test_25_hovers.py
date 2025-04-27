from playwright.sync_api import expect

from utils.base_test import BaseTest


class TestHovers(BaseTest):
	page_url = '/hovers'

	def test_hovers(self):
		imgs = self.page.get_by_role('img', name='User Avatar').all()
		captions = self.page.locator('figcaption').all()
		for i in range(len(imgs)):
			imgs[i].hover()
			for j in range(len(captions)):
				if i == j:
					expect(captions[j]).to_be_visible()
				else:
					expect(captions[j]).not_to_be_visible()
