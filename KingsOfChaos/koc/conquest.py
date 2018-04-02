import sys
import os
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import re
import tools

class Conquest(object):
	def __init__(self, koc):
		self.koc = koc

	def conquest(self, target, count):
		url = 'https://www.kingsofchaos.com/conquest.php'
		payload = {
			'conquest_target': target,
			'hash': '',
			'conquest': 'Go on a conquest against %s!' % target
		}

		for i in xrange(count):
			post = self.koc.session.post(url, data=payload, headers=self.koc.headers)
			html_source = post.content

			m = re.search('.*\(You have completed this conquest \d* times\)', html_source)
			if m:
				tools.log('%s: %s' % (target, m.group()))

def main():
	from koc import KoC
	k = KoC('qqqq')
	c = Conquest(k)
	c.conquest(target='Wizards', count=1)

if __name__ == "__main__":
	main()