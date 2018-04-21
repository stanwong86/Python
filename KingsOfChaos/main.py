import sys
import os
import re
from koc import KoC
from koc import tools
import math
import traceback


def _setup_ssl():
	''' Magic to bypass SSL '''
	import ssl
	ssl._create_default_https_context = ssl._create_unverified_context

def _setup_opener():
	import cookielib
	import urllib2
	from poster.streaminghttp import register_openers

	opener = register_openers()
	cj = cookielib.CookieJar()
	cookie_handler = urllib2.HTTPCookieProcessor(cj)
	opener.add_handler(cookie_handler)

def auto_website():
	while True:
		_setup_ssl()
		_setup_opener()
		url = 'https://striderxokoc.weebly.com/koc.html'
		source = read_url(url)

		interval = 10
		action = re.search('<action>(.*)</action>', source).group(1)
		interval = int(re.search('<interval>(.*)</interval>', source).group(1))

		if action == 'Buying':
			weapon = re.search('<weapon>(.*)</weapon>', source).group(1)
			amount = re.search('<amount>(.*)</amount>', source).group(1)
			
			print action, weapon, amount
			run_buying(weapon, amount=amount, user='dennab')

		elif action == 'Training':
			selection = re.search('<selection>(.*)</selection>', source).group(1)
			amount = re.search('<amount>(.*)</amount>', source).group(1)
			print action, selection, amount
			run_training(selection, amount)
		
		print 'Sleeping %s minutes\n' % str(interval)
		sleep_time = randint((interval-1)*60,(interval+1)*60)
		time.sleep(sleep_time)

def run_sell_and_upgrade_UP():
	koc.setup('qqqq')
	koc.login()
	koc.sell_weapon('Heavy Steed', 37)
	koc.upgrade_unit_production()

def run_sell_and_upgrade_siege():
	koc.setup('qqqq')
	koc.login()
	koc.sell_weapon('Heavy Steed', 100)
	koc.upgrade_siege()

def raid_dark_mirage():
	koc.setup('qqqq')
	koc.login()
	koc.raid('4515875')

def run_fake_sab():
	s = Sabotage()

def auto_buy(weapon, limit=0):
	weapon_costs = {
		'Nunchaku': 1000000,
		'Lookout Tower': 1000000,
		'Chariot': 450000
	}

	gold = koc.get_current_gold()
	max_amount = int(math.floor(int(gold)/weapon_costs[weapon]))
	koc.buy_weapon(weapon, max_amount, limit)
	koc.random_sleep_seconds(5, 10)

def cycle():
	koc.buy_mercs('general', 4000)
	koc.buy_mercs('attack', 40000)
	koc.repair_chariots()
	auto_buy('Chariot', 11000)
	auto_buy('Lookout Tower', 1200)
	auto_buy('Nunchaku')
	
def auto():
	while True:
		try:
			k = KoC()
			k.login()

			#koc.create_diversion()
			#koc.buy_max_attackers()

			#cycle()
			#koc.random_sleep_minutes(5, 10)
			#cycle()
			#koc.random_sleep_minutes(5, 10)
			
			#cycle()
		except Exception:
			tools.log('Connection Error in main')
			traceback.print_exc()
			print "Unexpected error:", sys.exc_info()[0]
		koc.random_sleep_minutes(5, 10)

def test():
	k = KoC()
	k.buy_weapon('Chariot', 1, 1)

def main():
	test()

if __name__ == "__main__":
	main()