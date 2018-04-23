import sys
import os
import re
import tools
import traceback

class ArmorySource(object):
	def __init__(self):
		self.source = ''
		self.url = 'https://www.kingsofchaos.com/armory.php'

	def refresh_armory_source(self):
		self.source = self.read_url(self.url)

	def get_turing_str(self):
		m = re.search('name="turing" value="(.*)">', self.source)
		if m:
			tools.log('Turing Str {%s}' % m.group(1))
			return m.group(1)

	def get_current_gold(self, url = None):
		if not url:
			url = self.url
		m = re.search('>Gold:<.*$\n\s*(.*)', self.source, re.MULTILINE)
		if m:
			gold_with_comma = m.group(1)
			tools.log('Current Gold {%s}' % gold_with_comma)
			gold = re.sub(',', '', gold_with_comma)
			return gold
		return '0'

	def get_current_merc_count(self, merc_type):
		if merc_type == 'general':
			m = re.search('>Untrained Mercenaries.*$\n.*>(.*)</td>', self.source, re.MULTILINE)
		elif merc_type == 'attack':
			m = re.search('>Trained Attack Mercenaries.*$\n.*>(.*)</td>', self.source, re.MULTILINE)
		elif merc_type == 'defend':
			m = re.search('>Trained Defense Mercenaries.*$\n.*>(.*)</td>', self.source, re.MULTILINE)

		if m:
			merc_with_comma = m.group(1)
			tools.log('%s Mercs {%s}' % (merc_type.capitalize(), merc_with_comma))
			merc_count = re.sub(',', '', merc_with_comma)
			return merc_count

	def get_current_soldier_count(self, soldier_type):
		if soldier_type == 'general':
			m = re.search('>Untrained Soldiers.*$\n.*>(.*)</td>', self.source, re.MULTILINE)
		elif soldier_type == 'attack':
			m = re.search('>Trained Attack Soldiers.*$\n.*>(.*)</td>', self.source, re.MULTILINE)
		elif soldier_type == 'defend':
			m = re.search('>Trained Defense Soldiers.*$\n.*>(.*)</td>', self.source, re.MULTILINE)

		if m:
			soldier_with_comma = m.group(1)
			tools.log('%s Soldiers {%s}' % (soldier_type.capitalize(), soldier_with_comma))
			soldier_count = re.sub(',', '', soldier_with_comma)
			return soldier_count

	def get_current_weapon_count(self, weapon):
		pattern = '\t\t<td>%s</td>.*\n.*<td align="right">(.*)</td>' % weapon
		m = re.search(pattern, self.source, re.MULTILINE)
		if m:
			count_without_commas = re.sub(',', '', m.group(1))
			return count_without_commas
		else:
			print 'Cannot find weapon {%s}' % weapon
			tools.write_to_file('weapon_source.txt', source)
			return 0