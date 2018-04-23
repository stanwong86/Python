import sys
import os
import re
import tools
from base import Base

class Attack(Base):
	def __init__(self):
		pass

	def open_stats_page(self, defender_id):
		source = self.read_url('https://www.kingsofchaos.com/stats.php?id=%s' % defender_id)

	def raid(self, defender_id):
		self.open_stats_page(defender_id)
		url = 'https://www.kingsofchaos.com/attack.php'

		payload = {
			'defender_id': defender_id,
			'attack_type': 'raid',
			'attackbut': 'Raiding..',
			'turing': self.get_turing_string()
		}

		post = self.session.post(url, data=payload, headers=self.headers)
		source = post.content
		print 'Target raided'

def main():
	pass

if __name__ == "__main__":
	main()