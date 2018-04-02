import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools

class Attack(object):
	def __init__(self, koc):
		self.koc = koc

	def open_stats_page(self, defender_id):
		source = self.koc.read_url('https://www.kingsofchaos.com/stats.php?id=%s' % defender_id)

	def raid(self, defender_id):
		self.open_stats_page(defender_id)
		url = 'https://www.kingsofchaos.com/attack.php'

		payload = {
			'defender_id': defender_id,
			'attack_type': 'raid',
			'attackbut': 'Raiding..',
			'turing': self.koc.get_turing_string()
		}

		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		source = post.content
		print 'Target raided'

def main():
	from koc import KoC
	k = KoC('qqqq')
	t = Training(k)
	t.buy_max_attackers()

if __name__ == "__main__":
	main()