import re
import urllib2
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode
from weapons import Weapons
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import tools

class KoC(object):
	def __init__(self, user=None):
		self.setup(user)
		self.weapons = Weapons().get_weapons()

	def setup(self, user):
		self._setup_opener()
		if self._is_login_required():
			self._login(user)
			
	def _setup_opener(self):
		import cookielib
		opener = register_openers()
		cj = cookielib.CookieJar()
		cookie_handler = urllib2.HTTPCookieProcessor(cj)
		opener.add_handler(cookie_handler)

	def submit_form(self, url, values=[]):
		data, headers = multipart_encode(values)
		headers['User-Agent'] = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
		request = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(request)
		return response

	def _is_login_required(self):
		url = 'http://www.kingsofchaos.com/base.php'
		source = self.submit_form(url).read()
		m = re.search('Please login to view that page', source)
		if m:
			return True
		return False

	def _login(self, user=None):
		url = 'http://www.kingsofchaos.com/login.php'
		if not user:
			user = 'qqqq'

		pw = tools.read_file('._login.txt')
		values = [['usrname', user], ['peeword', pw]]
		res = self.submit_form(url, values)

	def get_turing_string(self):
		url = 'http://www.kingsofchaos.com/armory.php'
		values = []
		html_source = self.submit_form(url, values).read()
		m = re.search('name="turing" value="(.*)">', html_source)
		if m:
			return m.group(1)

	def upgrade_unit_production(self):
		url = 'http://www.kingsofchaos.com/train.php'
		values = [
			['upgrade_prod', 'yes'],
			['hash','']
		]
		self.submit_form(url, values)
		print 'Unit Production Upgraded'

def main():
	k = KoC()
	
if __name__ == "__main__":
	main()