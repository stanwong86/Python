import sys
import os
import re
import tools
import time
from PIL import Image
from StringIO import StringIO
from random import randint
import requests
sys.path.append('sql')
from sql_util import select
from koc.koc_v2 import KoC
import json

class AutoClicker(KoC):
	def __init__(self, user=None):
		super(AutoClicker, self).__init__(user)
		self.auto_click()

	def _get_recruit_values(self):
		url = 'http://www.kingsofchaos.com/recruit.php'
		source = self.session.get(url, headers=self.headers).text

		iuniqid_value = re.search('"iuniqid" value="(.*)">', source).group(1)
		uniqid_value = re.search('"uniqid" value="(.*)">', source).group(1)
		special_link_id = re.search("\'\.img\' \+ \'\?(.*)&", source).group(1)

		values = {
			'iuniqid': iuniqid_value,
			'uniqid': uniqid_value,
			'linkid': special_link_id
		}
		return values

	def _read_image_url(self, values, instance):
		img_url = 'http://www.kingsofchaos.com/ads/recruit.img?%s&uniqid=%s' % (values['linkid'], values['uniqid'])
		print img_url
		image = self.get_image_from_url(img_url)
		image.save('retrieved_letter_%s.png' % instance)
		return image

	def _get_letter_from_image(self, image):
		image_bits = list(image.getdata())
		image_bits_str = ''.join(map(str, image_bits))

		results = select("where letter_bits='%s'" % (image_bits_str))
		if results:
			print 'Found Letter %s' % results[0][1]
			return results[0][1]
		else:
			print 'Letter not found'
		return None

	def _click(self, values, letter):
		url = 'http://www.kingsofchaos.com/recruit.php'
		payload = {
			'iuniqid': values['iuniqid'],
			'uniqid': values['uniqid'],
			'hash': '',
			'image_click_number': letter
			#'recaptcha_response_field':
			#'image_click_value': ''
		}
		headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Referer': 'http://www.kingsofchaos.com/recruit.php?uniqid=%s' % values['uniqid']
		}

		self.headers.update(headers)
		post = self.session.post(url, data=payload, headers=self.headers)
		#print self.session.headers
		#print self.session
		tools.write_to_file_silently('PostSource.txt', post.content)
		#print payload
		#print 'Clicked for {%s}' % values['uniqid']

	def auto_click(self):
		count = 0
		for instance in xrange(10):
			recruit_values = self._get_recruit_values()
			print recruit_values
			image = self._read_image_url(recruit_values, instance)
			letter = self._get_letter_from_image(image)				
			if letter:
				count +=1
				self._click(recruit_values, letter)
		print 'Found %s' % count

def main():
	a = AutoClicker('qqqq')
	pass
	
if __name__ == "__main__":
	main()