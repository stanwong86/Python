from Armory import Armory
from conquest import Conquest
from training import Training
from attack import Attack
from mercs import Mercs
from koc import KoC

def setup(user):
	global k, arm, con, training, merc
	k = KoC(user)
	arm = Armory(k)
	con = Conquest(k)
	training = Training(k)
	attack = Attack(k)
	merc = Mercs(k)

def login():
	k.login()

def create_diversion():
	k.create_diversion()

def random_sleep_minutes(minutes_start, minutes_end):
	k.random_sleep_minutes(minutes_start, minutes_end)
	
def random_sleep_seconds(seconds_start, seconds_end):
	k.random_sleep_seconds(seconds_start, seconds_end)

def buy_weapon(weapon, amount, limit=0):
	arm.buy_weapon(weapon, amount, limit)

def sell_weapon(weapon, amount):
	arm.sell_weapon(weapon, amount)

def repair_chariots():
	arm.repair_chariots()

def conquest(target, count):
	con.conquest(target, count)

def train(selection, amount):
	training.train(selection, amount)

def upgrade_UP():
	training.upgrade_unit_production()

def buy_max_attackers():
	training.buy_max_attackers()

def upgrade_siege():
	arm.upgrade_siege()

def raid(defender_id):
	attack.raid(defender_id)

def get_current_gold():
	return k.get_current_gold()

def buy_mercs(merc_type, limit):
	return merc.buy_mercs(merc_type, limit)
