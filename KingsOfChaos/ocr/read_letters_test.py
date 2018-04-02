import sys
import os
import re
import requests
sys.path.append('../koc')
from koc import KoC
from PIL import Image, ImageTk
from StringIO import StringIO
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import tools

def test():
	f = tools.read_file('letters_A.txt')
	numbers = f.split(',')

	for i in xrange(len(numbers)):
		if i in numbers[i+1:]:
			print 'Dupe'

	print len(numbers[154]), len(numbers[155])
	print len(numbers)

	l = [0,1,0]

	ls = ''.join(map(str, l))
	print ls

def is_letter_found(letter, image_bits_str):
	letter_bits_list_str = tools.read_file('letters_%s.txt' % letter)
	letter_bits_list = letter_bits_list_str.split(',')

	for letter_bits in letter_bits_list:
		letter_bits_sum = sum(map(int, letter_bits))
		image_bits_sum = sum(map(int, image_bits_str))
		if letter_bits_sum == image_bits_sum:
			print 'Sum Match Found'
		if image_bits_str in letter_bits:
			return True
	return False

def get_click_letter(image):
	image_bits = list(image.getdata())
	image_bits_str = ''.join(map(str, image_bits))

	#letters = 'kingchaos'
	letters = 'a'
	for letter in letters:
		print 'Expected {%s}' % sum(image_bits)
		if is_letter_found(letter, image_bits_str):
			print 'Letter found for {%s}' % letter
			return letter
	print 'Letter not found'
	return None

im1 = Image.open('../retrieved_letter_82f0d2.png', 'r')
get_click_letter(im1)
