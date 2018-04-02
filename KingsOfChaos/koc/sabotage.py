import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools

class Sabotage(object):
	def __init__(self, koc):
		self.koc = koc

	def fake_sab_impl(self, defender_id):
		url = 'https://www.kingsofchaos.com/attack.php'

		payload = {
			'mission_type': 'sabotage',
			'enemy_weapon': '69',
			'numsab': '1',
			'numspies': '1',
			'sabturns': '5',
			'turing': self.koc.get_turing_string(),
			'spybut': 'Sabotaging..',
			'defender_id': defender_id,
			'hash': ''
		}

		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		html_source = post.content

		m = re.search('Covert Mission Report(.*)<form method="get" action="attack.php">', html_source, re.MULTILINE|re.DOTALL)
		if m:
			return [1, m.group(1)]
		else:
			return [0, 'Failed to retrieve: Covert Mission Report']

	def fake_sab(self, defender_name, defender_id, count):
		for i in xrange(count):
			result, msg = self.fake_sab_impl(defender_id)

			log_msg = '%s: %s' % (i, msg)
			if msg.find(' are caught, interrogated, and executed') == -1 or msg.find('all your tools are intact') == -1:
				tools.log(log_msg)
			else:
				print 'Attempt %s: User {%s}' % (i, defender_name)
				tools.log(log_msg, True)

			if not result:
				break

def main():
	from koc import KoC
	k = KoC('qqqq')
	sab = Sabotage(k)

	# SR
	user_ids = {
		'Alexander_SR':'4527074',
		'wangtangkiki':'4527311', # replace
		'The-Punisher':'4527193', # replace
		'Aggie-SR':'4527024',
		'antons1':'4527304', # replace
		'Sonny':'4528226',
		'mastram':'4187669',
		'UncleFocker':'4527015',
		'DeathDragon':'4524459', # replace
		'Arthuraa':'4527030'
	}

	user_ids2 = {
	}
	user_ids.update(user_ids2)

	max_sab = 10
	current_sab_count = 0
	
	for username, user_id in user_ids.iteritems():
		if current_sab_count == max_sab:
			break
		turns = 46
		print 'User {%s} Id {%s}' % (username, user_id)
		sab.fake_sab(username, user_id, turns)

		current_sab_count +=1

if __name__ == "__main__":
	main()