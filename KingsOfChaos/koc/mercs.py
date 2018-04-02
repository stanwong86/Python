import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools

class Mercs(object):
	def __init__(self, koc):
		self.koc = koc

	def get_current_merc_count(self):
		url = 'https://www.kingsofchaos.com/mercs.php'
		source = self.koc.read_url(url)
		
		m = re.search('>Untrained Mercenaries.*$\n.*>(.*)</td>', source, re.MULTILINE)
		if m:
			merc_with_comma = m.group(1)
			tools.log('Untrained Mercs: %s' % merc_with_comma)
			untrained_mercs = re.sub(',','',merc_with_comma)
			return untrained_mercs

	def buy_untrained_impl(self, amount):
		url = 'https://www.kingsofchaos.com/mercs.php'

		payload = {
			'mercs[attack]' : '0',
			'mercs[defend]' : '0',
			'mercs[general]' : amount,
			'turing': self.koc.get_turing_string()
		}

		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		source = post.content
		tools.log('Bought %s Untrained Mercs' % amount)

	def buy_untrained_mercs(self, limit):
		gold = self.koc.get_current_gold('https://www.kingsofchaos.com/mercs.php')
		self.koc.random_sleep_seconds(5, 10)
		mercs = self.get_current_merc_count()

		if int(mercs) < limit:
			self.koc.random_sleep_seconds(5, 10)
			self.buy_untrained_impl(int(gold)/3500)

def main():
	from koc import KoC
	k = KoC('qqqq')
	mercs = Mercs(k)
	mercs.buy_untrained_mercs()

if __name__ == "__main__":
	main()