import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools
import time
from koc.koc import KoC

class Recon(KoC):
	def __init__(self):
		super(Recon, self).__init__()

		all_users = {}
		for i in xrange(1,20):
			users = self.recon_page(page=i, min_gold=5000000, min_tff=74000)
			all_users.update(users)

		self.print_target_users(all_users, max_defense=60000000)

	def get_user_ids_with_gold(self, html_source, min_gold, min_tff):
		user_ids_with_gold = {}
		user_id_search = re.findall('<tr class="player" user_id="(\d*)" ', html_source)
		gold_search = re.findall('<td align="right" style="padding-right: 20px;">([^\s]*) Gold</td>', html_source)
		usernames = re.findall('stats.php\?id=.*>(.*)</a></td>\n', html_source)
		tff = re.findall('stats.php\?id=.*?</td>\n		<td align="right">(.*)</td>', html_source)

		for i in xrange(len(user_id_search)):
			if gold_search[i] != '???' and int(gold_search[i].replace(',','')) > min_gold and int(tff[i].replace(',','')) > min_tff:
				user_ids_with_gold[user_id_search[i]] = {'Gold': gold_search[i], 'TFF': tff[i], 'Username': usernames[i]}
		return user_ids_with_gold

	def recon_page(self, page, min_gold, min_tff):
		start = (page-1)*20
		url = 'http://www.kingsofchaos.com/battlefield.php?start=%s&search=&search_type=&buddy_type=' % start
		values = [
		]

		html_source = self.submit_form(url, values).read()
		users_ids_gold_dict = self.get_user_ids_with_gold(html_source, min_gold, min_tff)
		return users_ids_gold_dict

	da_dict = {
		'thisisme': '48,000,000', 
		'shk1020-SR': '48,000,000',
		'sushicaserole7777': '200,000,000',
		'strider':'15,000,000',
		'MachineSaw':'110,000,000',
		'krisv': '2,300,000',
		'Releaseme-SR': '6,000,000',
		'Noisekick': '37,000,000',
		'FearlessOrc': '80,000,000',
		'Reeb-': '4,500,000',
		'TAS-IRONg0rFz': '63,000,000'
	}

	def print_target_users(self, d, max_defense):
		for userid, values in d.iteritems():
			if values['Username'] in self.da_dict.keys():
				values['DA'] = self.da_dict[values['Username']]
			if int(values.get('DA','0').replace(',','')) < max_defense:
				tools.log('User:%s, Values: %s' % (userid, values))

	def recon(self, user_id):
		url = 'http://www.kingsofchaos.com/attack.php'
		values = [
			['mission_type', 'recon'],
			['defender_id', user_id],
			['spyrbut', 'Spying..'],
			['turing', self.get_turing_string()]
		]
		html_source = self.submit_form(url, values).read()
		m = re.search('<td>Defensive Action</td>\n\t\t\t<td align="right">(.*)</td>', html_source)
		if m:
			if m.group(1) == '???':
				self.recon(user_id)
			else:
				tools.log('Logged user {%s} DA {%s}' % (user_id, m.group(1)))

def main():
	r = Recon()
	pass
	
if __name__ == "__main__":
	main()