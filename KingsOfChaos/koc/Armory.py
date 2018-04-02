import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools

class Armory(object):
	def __init__(self, koc):
		self.koc = koc
		self.url = 'https://www.kingsofchaos.com/armory.php'

	def log_result(self, html_source, weapon, amount):
		pattern = 'Not enough money for those items.'
		msg = 'Bought %s %s' % (amount, weapon)
		m = re.search(pattern, html_source)
		if m:
			msg = 'Not enough money for %s' % (weapon)
		tools.log(msg)

	def new_buy_weapon_impl(self, weapon, amount):
		url = 'https://www.kingsofchaos.com/armory.php'
		payload = {
			'buy_weapon[%s]' % (self.koc.weapons[weapon]): amount,
			'turing': self.koc.get_turing_string(),
			'buybut': 'Buy Weapons'
		}

		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		html_source = post.content
		self.log_result(html_source, weapon, amount)

	def buy_weapon(self, weapon, amount):
		try:
			self.new_buy_weapon_impl(weapon, amount)
		except Exception:
			tools.log('Connection Error in Armory')
			print "Unexpected error:", sys.exc_info()[0]

	def sell_weapon(self, weapon, amount):
		url = 'https://www.kingsofchaos.com/armory.php'
		payload = {
			'scrapsell[%s]' % (self.koc.weapons[weapon]): amount,
			'hash': ''
		}
		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		html_source = post.content
		tools.log('Sold Weapon {%s} Amount {%s}' % (weapon, amount))

	def upgrade_siege(self):
		url = 'https://www.kingsofchaos.com/armory.php'
		payload = {
			'upgrade_siege':'yes',
			'upgrade_siege_type': 'attack',
			'hash':''
		}
		post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
		html_source = post.content
		tools.log('Upgraded Siege')

	def repairs_needed(self):
		source = self.koc.read_url(self.url)
		m = re.search('Repair all weapons', source)
		pattern = 'repair\[72\]" size="4" maxlength="7" value="(.*)"'

		if m:
			repair_m = re.search(pattern, source)
			if repair_m:
				repair_value = repair_m.group(1)
				return repair_value
		return 0

	def repair_chariots(self):
		repair_value = self.repairs_needed()
		if float(repair_value) > 0:
			payload = {
				'repair[72]': repair_value,
				'hash':''
			}
			self.koc.session.post(self.url, data=payload, headers=self.koc.headers)
			tools.log('Repaired {} Chariots'.format(repair_value))

def main():
	from koc import KoC
	k = KoC('qqqq')
	arm = Armory(k)
	arm.repair_chariots()
	#arm.buy_weapon(weapon='Chariot', amount=1)

if __name__ == "__main__":
	main()