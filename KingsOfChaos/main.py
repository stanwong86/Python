import sys
import os
import re
import koc
import math
import tools

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

def short_sleep_buy(weapon, amount):
	koc.buy_weapon(weapon, amount)
	koc.random_sleep_seconds(5, 10)

def auto_buy(weapon, weapon_cost):
	gold = koc.get_current_gold()
	max_amount = math.floor(int(gold)/weapon_cost)
	short_sleep_buy(weapon, max_amount)

def auto():
	koc.setup('qqqq')

	while True:
		try:
			koc.login()
			koc.create_diversion()
			koc.buy_max_attackers()
			koc.buy_untrained_mercs(25000)
			koc.repair_chariots()
			
			auto_buy('Chariot', 450000)
			koc.random_sleep_minutes(9, 11)
			auto_buy('Lookout Tower', 1000000)
		except Exception:
			tools.log('Connection Error in main')
			print "Unexpected error:", sys.exc_info()[0]
		koc.random_sleep_minutes(9, 11)

def raid_dark_mirage():
	koc.setup('qqqq')
	koc.login()
	koc.raid('4515875')

def run_fake_sab():
	s = Sabotage()

def manual():
	pass

def main():
	auto()

if __name__ == "__main__":
	main()