import sys
import os
import re
import tools
from base import Base

class Conquest(Base):
	def __init__(self):
		pass

	def conquest(self, target, count):
		url = 'https://www.kingsofchaos.com/conquest.php'
		payload = {
			'conquest_target': target,
			'hash': '',
			'conquest': 'Go on a conquest against %s!' % target
		}

		for i in xrange(count):
			post = self.session.post(url, data=payload, headers=self.headers)
			html_source = post.content

			m = re.search('.*\(You have completed this conquest \d* times\)', html_source)
			if m:
				tools.log('%s: %s' % (target, m.group()))

def main():
	c = Conquest()
	c.conquest(target='Wizards', count=1)

if __name__ == "__main__":
	main()