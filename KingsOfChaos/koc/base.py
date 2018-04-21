import sys
import os
import re
import tools
from PIL import Image
from StringIO import StringIO
import requests
from random import randint
import time
from weapons import get_weapons

class Base(object):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Connection': 'keep-alive',
		'Host': 'www.kingsofchaos.com',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
	}

	count = 0

	def __new__(cls, *args, **kwargs):
		obj = super(Base, cls).__new__(cls)
		obj.__init__(*args, **kwargs)
		obj.set_session

	def set_session(self):
		with requests.session as temp_session:
			self.session = temp_session
			self.login()
			print count
			count += 1	

	def __init__(self):
		print 'i am useless init'
		

	def get_user_password(self):
		d = {}
		lines = tools.read_file('._login.txt').split('\n')
		for line in lines:
			if line:
				field, value = line.split('=', 1)
				d[field] = value
		return d['username'], d['password']

	def login(self):
		if self._is_login_required():
			user, pw = self.get_user_password()
			payload = {'usrname': user, 'peeword': pw}
			url = 'https://www.kingsofchaos.com/login.php'
			post = self.session.post(url, data=payload, headers=self.headers)
			tools.log('Logged In as {%s}' % user)
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
		tools.log_silently('read_url: {%s}' % url)
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
			tools.log('Current Gold {%s}' % gold_with_comma)
			gold = re.sub(',','',gold_with_comma)
			return gold
		return '0'

	def get_current_gold(self, url=None):
		if not url:
			url = 'https://www.kingsofchaos.com/armory.php'
		source = self.read_url(url)
		return self.get_current_gold_from_source(source)
		

def main():
	pass
	
if __name__ == "__main__":
	main()