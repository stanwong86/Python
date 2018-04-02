class Weapons(object): 
	attack_weapons = {
		'Broken Stick': '69',
		'Heavy Steed': '23',
		'Excalibur': '27',
		'Chariot': '72',
		'Blackpowder Missile': '70'
	}

	defense_weapons = {
		'Shield': '38',
		'Mithril': '46',
		'Dragonskin': '51',
		'Invisibility Shield': '71'
	}

	spy_weapons = {
		'Rope': '58',
		'Dirk': '63',
		'Cloak': '65',
		'Grappling Hook': '67',
		'Skeleton Key': '73',
		'Nunchaku': '75'
	}

	sentry_weapons = {
		'Big Candle': '62',
		'Horn': '64',
		'Tripwire': '66',
		'Guard Dog': '68',
		'Lookout Tower': '74'
	}

	def get_weapons(self):
		d = {}
		d.update(self.attack_weapons)
		d.update(self.defense_weapons)
		d.update(self.spy_weapons)
		d.update(self.sentry_weapons)
		return d

def get_weapons():
	w = Weapons()
	return w.get_weapons()