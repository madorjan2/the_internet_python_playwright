from utils.base_test import BaseTest


def are_different(str_list):
	zeroths = [str_list[i][0] for i in range(len(str_list))]
	firsts = [str_list[i][1] for i in range(len(str_list))]
	seconds = [str_list[i][2] for i in range(len(str_list))]
	return (
		len(set(zeroths)) > 1
		and len(set(firsts)) > 1
		and len(set(seconds)) > 1
	)


class TestDynamicContent(BaseTest):
	page_url = '/dynamic_content'

	def test_dynamic_content(self):
		profile_pics = []
		descriptions = []
		for i in range(10):
			current_pics = self.page.locator('//div[@id="content"]//img').all()
			profile_pics.append(
				[element.get_attribute('src') for element in current_pics]
			)
			current_desc = self.page.locator(
				'//div[@id="content"]//div[@class="large-10 columns"]'
			).all()
			descriptions.append(
				[element.text_content() for element in current_desc]
			)
			self.page.reload()
		assert are_different(profile_pics) and are_different(descriptions)
