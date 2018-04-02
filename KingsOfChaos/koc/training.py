import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools

class Training(object):
	def __init__(self, koc):
		self.koc = koc

	def log_result(self, html_source, selection, amount):
		pattern = 'Not enough money for that operation.'
		msg = 'Attempted to Train %s %s' % (amount, selection)
		m = re.search(pattern, html_source)
		if m:
			msg = 'Not enough money for %s %s' % (amount, selection)
		tools.log(msg)
		print ''

	def validate_selection(self, selection):
		if selection not in ['attacker', 'defender', 'spy', 'sentry']:
			sys.exit('Invalid training selection {%s}' % selection)

	def train(self, selection, amount):
		self.validate_selection(selection)
		url = 'https://www.kingsofchaos.com/train.php'

		payload = {
			'train[%s]' % (selection) : amount,
			'turing': self.koc.get_turing_string(),
			'hash': ''
		}

		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		source = post.content
		self.log_result(source, selection, amount)

	def upgrade_unit_production(self):
		url = 'https://www.kingsofchaos.com/train.php'

		payload = {
			'upgrade_prod': 'yes',
			'hash': ''
		}
		
		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		tools.log('Unit Production Upgraded')

	def buy_max_attackers(self):
		gold = self.koc.get_current_gold('https://www.kingsofchaos.com/train.php')
		self.koc.random_sleep_seconds(5, 10)
		self.train('attacker', int(gold)/2000)

def main():
	from koc import KoC
	k = KoC('qqqq')
	t = Training(k)
	t.buy_max_attackers()

if __name__ == "__main__":
	main()