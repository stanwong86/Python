import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools

class Mercs(object):
	def __init__(self, koc):
		self.koc = koc

	def get_current_merc_count(self, merc_type):
		url = 'https://www.kingsofchaos.com/mercs.php'
		source = self.koc.read_url(url)
		
		if merc_type == 'general':
			m = re.search('>Untrained Mercenaries.*$\n.*>(.*)</td>', source, re.MULTILINE)
		elif merc_type == 'attack':
			m = re.search('>Trained Attack Mercenaries.*$\n.*>(.*)</td>', source, re.MULTILINE)
		elif merc_type == 'defend':
			m = re.search('>Trained Defense Mercenaries.*$\n.*>(.*)</td>', source, re.MULTILINE)

		if m:
			merc_with_comma = m.group(1)
			tools.log('%s Mercs {%s}' % (merc_type.capitalize(), merc_with_comma))
			merc_count = re.sub(',','',merc_with_comma)
			return merc_count

	def buy_mercs_impl(self, merc_type, amount):
		url = 'https://www.kingsofchaos.com/mercs.php'

		amounts = {'attack': '0', 'defend': '0', 'general': '0'}
		amounts[merc_type] = amount

		payload = {
			'mercs[attack]' : amounts['attack'],
			'mercs[defend]' : amounts['defend'],
			'mercs[general]' : amounts['general'],
			'turing': self.koc.get_turing_string()
		}

		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		source = post.content

	def buy_mercs(self, merc_type, limit):
		merc_costs = {'attack': 4500, 'defend': 4500, 'general': 3500}
		merc_cost = merc_costs[merc_type]

		gold = self.koc.get_current_gold()
		self.koc.random_sleep_seconds(5, 10)
		mercs = self.get_current_merc_count(merc_type)

		if int(mercs) < limit:
			self.koc.random_sleep_seconds(5, 10)
			amount = int(gold)/merc_cost
			self.buy_mercs_impl(merc_type, amount)
			tools.log('%s Mercs Current {%s} Bought {%s} ' % (merc_type.capitalize(), mercs, amount))

def main():
	from koc import KoC
	k = KoC('qqqq')
	mercs = Mercs(k)
	mercs.buy_untrained_mercs()

if __name__ == "__main__":
	main()