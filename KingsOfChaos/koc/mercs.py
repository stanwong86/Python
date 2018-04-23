import sys
import os
import re
import tools
from base import Base

class Mercs(Base):
	def __init__(self):
		super(Mercs, self).__init__()

	def buy_mercs_impl(self, merc_type, amount):
		url = 'https://www.kingsofchaos.com/mercs.php'

		amounts = {'attack': '0', 'defend': '0', 'general': '0'}
		amounts[merc_type] = amount

		payload = {
			'mercs[attack]' : amounts['attack'],
			'mercs[defend]' : amounts['defend'],
			'mercs[general]' : amounts['general'],
			'turing': self.get_turing_string()
		}

		post = self.session.post(url, data=payload, headers=self.headers)
		source = post.content

	def buy_mercs(self, merc_type, limit):
		merc_costs = {'attack': 4500, 'defend': 4500, 'general': 3500}
		merc_cost = merc_costs[merc_type]

		gold = self.get_current_gold()
		self.random_sleep_seconds(5, 10)
		mercs = self.get_current_merc_count(merc_type)

		if int(mercs) < limit:
			self.random_sleep_seconds(5, 10)
			amount = int(gold)/merc_cost
			self.buy_mercs_impl(merc_type, amount)
			tools.log('%s Mercs Current {%s} Bought {%s} ' % (merc_type.capitalize(), mercs, amount))

def main():
	mercs = Mercs(k)
	mercs.buy_untrained_mercs()

if __name__ == "__main__":
	main()