import sys
import os
import re
import tools
import traceback
from base import Base

class Armory(Base):
	def __init__(self):
		super(Armory, self).__init__()
		self.url = 'https://www.kingsofchaos.com/armory.php'
		self.previous_weapon_counts = {
			'Nunchaku': 0,
			'Lookout Tower': 0,
			'Chariot': 0
		}

	def buy_weapon_impl(self, weapon, amount):
		url = 'https://www.kingsofchaos.com/armory.php',
		payload = {
			'buy_weapon[%s]' % (self.weapons[weapon]): amount,
			'turing': self.get_turing_string(),
			'buybut': 'Buy Weapons'
		}

		post = self.session.post(url, data=payload, headers=self.headers)

	def log_sabbed_weapons(self, weapon, weapon_count):
		previous_count = int(self.previous_weapon_counts[weapon])
		if weapon_count < previous_count:
			sabbed_count = previous_count - weapon_count
			msg = "=== {%s} %ss were sabbed! ===" % (sabbed_count, weapon)
			tools.log(msg)
			tools.log_sabbed_weapons('%s %s' % (weapon, sabbed_count))
		self.previous_weapon_counts[weapon] = weapon_count

	def buy_weapon(self, weapon, amount, limit=0):
		#try:
		weapon_count = int(self.get_current_weapon_count(weapon))
		if (weapon_count < limit or limit == 0) and amount != 0:
			self.buy_weapon_impl(weapon, amount)
			tools.log('%s - Current {%s} Bought {%s}' % (weapon, weapon_count, amount))
			weapon_count = weapon_count + int(amount)
		elif weapon_count > limit and limit != 0:
			tools.log('%s - Current {%s} Limit Reached {%s}' % (weapon, weapon_count, limit))
		elif amount == 0:
			tools.log('%s - Current {%s} Not Enough Money' % (weapon, weapon_count))

		self.log_sabbed_weapons(weapon, weapon_count)
		'''
		except Exception:
			tools.log('Connection Error in Armory')
			traceback.print_exc()
			print "Unexpected error:", sys.exc_info()[0]
		'''

	def sell_weapon(self, weapon, amount):
		url = 'https://www.kingsofchaos.com/armory.php'
		payload = {
			'scrapsell[%s]' % (self.weapons[weapon]): amount,
			'hash': ''
		}
		post = self.session.post(url, data=payload, headers=self.headers)
		html_source = post.content
		tools.log('Sold Weapon {%s} Amount {%s}' % (weapon, amount))

	def upgrade_siege(self):
		url = 'https://www.kingsofchaos.com/armory.php'
		payload = {
			'upgrade_siege':'yes',
			'upgrade_siege_type': 'attack',
			'hash':''
		}
		post = self.session.post(url, data=payload, headers=self.headers)
		html_source = post.content
		tools.log('Upgraded Siege')

	def repairs_needed(self):
		source = self.read_url(self.url)
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
			self.session.post(self.url, data=payload, headers=self.headers)
			tools.log('Repaired {} Chariots'.format(repair_value))

def main():
	from koc import KoC
	k = KoC('qqqq')
	arm = Armory(k)
	arm.repair_chariots()
	#arm.buy_weapon(weapon='Chariot', amount=1)

if __name__ == "__main__":
	main()