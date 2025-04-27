from playwright.sync_api import expect

from utils.base_test import BaseTest


TEST_DATA = {'latitude': 12.345, 'longitude': 9.8765}


class TestGeolocation(BaseTest):
	page_url = '/geolocation'

	def test_geolocation(self):
		self.page.context.grant_permissions(['geolocation'])
		self.page.context.set_geolocation(
			{
				'longitude': TEST_DATA['longitude'],
				'latitude': TEST_DATA['latitude'],
			}
		)
		self.page.get_by_role('button', name='Where am I?').click()
		expect(self.page.locator('#lat-value')).to_have_text(
			str(TEST_DATA['latitude'])
		)
		expect(self.page.locator('#long-value')).to_have_text(
			str(TEST_DATA['longitude'])
		)
