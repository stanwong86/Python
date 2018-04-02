import sys
import os
import re
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import tools
from PIL import Image
from StringIO import StringIO
import requests
from weapons import get_weapons
from random import randint
import time

class KoC(object):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Connection': 'keep-alive',
		'Host': 'www.kingsofchaos.com',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
	}

	def __init__(self, user):
		self.weapons = get_weapons()
		self.user = user

		with requests.Session() as session:
			self.session = session
			self.login()

	def login(self):
		if self._is_login_required():
			pw = tools.read_file('._login.txt')
			payload = {'usrname': self.user, 'peeword': pw}
			url = 'https://www.kingsofchaos.com/login.php'
			post = self.session.post(url, data=payload, headers=self.headers)
			print 'Logged In'
			return post

	def _is_login_required(self):
		url = 'https://www.kingsofchaos.com/base.php'
		source = self.read_url(url)
		m = re.search('Please login to view that page', source)
		if m:
			return True
		return False

	def get_image_from_url(self, url, payload = {}):
		image_request_result = self.session.get(url, data=payload, headers=self.headers)
		image = Image.open(StringIO(image_request_result.content))
		return image

	def get_turing_string(self):
		url = 'https://www.kingsofchaos.com/armory.php'
		source = self.read_url(url)
		m = re.search('name="turing" value="(.*)">', source)
		if m:
			return m.group(1)

	def read_url(self, url):
		response = self.session.get(url, headers=self.headers)
		source = response.content
		response.close()
		return source

	def random_sleep_minutes(self, minutes_start, minutes_end):
		sleep_time = randint(minutes_start*60, minutes_end*60)
		tools.log('Sleeping %s minutes' % str(sleep_time/60))
		time.sleep(sleep_time)

	def random_sleep_seconds_with_page(self, php_page, seconds_start, seconds_end):
		url = 'https://www.kingsofchaos.com/%s.php' % php_page
		self.read_url(url)

		sleep_time = randint(seconds_start, seconds_end)
		print('Sleeping %s seconds for %s page' % (str(sleep_time), php_page))
		time.sleep(sleep_time)

	def random_sleep_seconds(self, seconds_start, seconds_end):
		sleep_time = randint(seconds_start, seconds_end)
		print('Sleeping %s seconds' % (str(sleep_time)))
		time.sleep(sleep_time)

	def create_diversion(self):
		tools.log('--- Diversion Start ---')
		self.random_sleep_seconds_with_page('base', 5, 20)
		self.random_sleep_seconds_with_page('train', 5, 20)
		self.random_sleep_seconds_with_page('armory', 5, 20)
		print('--- Diversion End ---')

	def get_current_gold_from_source(self, source):
		m = re.search('>Gold:<.*$\n\s*(.*)', source, re.MULTILINE)
		if m:
			gold_with_comma = m.group(1)
			tools.log('Current Gold: %s' % gold_with_comma)
			gold = re.sub(',','',gold_with_comma)
			return gold
		return '0'

	def get_current_gold(self, url=None):
		if not url:
			url = 'https://www.kingsofchaos.com/armory.php'
		source = self.read_url(url)
		return self.get_current_gold_from_source(source)
		

def main():
	k = KoC('qqqq')
	
if __name__ == "__main__":
	main()