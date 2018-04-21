import sys
import os
import re
import tools

from Armory import Armory
from conquest import Conquest
from training import Training
from attack import Attack
from mercs import Mercs

class KoC(Armory, Conquest, Attack, Mercs):
	def __init__(self):
		super(KoC, self).__init__()
		return self

def main():
	k = KoC()
	
if __name__ == "__main__":
	main()