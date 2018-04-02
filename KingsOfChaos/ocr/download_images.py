import sys
import os
import re
import requests
sys.path.append('../koc')
from koc_v2 import KoC
from PIL import Image
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import tools
import time
sys.path.append('../sql')
from sql_util import select
from SaveLettersToDB import save_images

k = None

def read_url(uniqid):
	r = k.session.get('http://www.kingsofchaos.com/recruit.php?uniqid=%s' % uniqid)
	data = r.text

	m = re.search("\'\.img\' \+ \'\?(.*)&", data)
	if m:
		random_id = m.group(1)
		return random_id

def get_image(random_id, uniqid):
	img_url = 'http://www.kingsofchaos.com/ads/recruit.img?%s&uniqid=%s' % (random_id, uniqid)
	image = k.get_image_from_url(img_url)
	return image

def display_results_count(current_list, image_bits_str, total_clicks):
	if len(current_list) == 0:
		result = select("where letter_bits='%s'" % (image_bits_str))
		letter = result[0][1]
		print 'Found all letters for {%s}!' % letter
	else:
		print 'Found %s out of %s' % (len(current_list), total_clicks)	

def save_image(image, instance, i):
	mypath = 'C:/Users/stanley.wong/Documents/Python_Scripts/Prototypes/KingsOfChaos/ocr/letters'
	filepath = os.path.join(mypath, 'letter%s_%s.png' % (instance, i))
	image.save(filepath)

def is_dupe(instance, image_bits_str, current_list):
	if image_bits_str in current_list:
		print '%s: Dupe' % instance
		return True
	elif select("where letter_bits='%s'" % (image_bits_str)):
		print '%s: Found in DB' % instance
		return True

	return False

def convert_image_to_image_bit_str(image):
	image_bits = list(image.getdata())
	image_bits_str = ''.join(map(str, image_bits))
	return image_bits_str

def download_images(instance):
	uniqid='hha62cme'
	random_id = read_url(uniqid)

	current_list = []
	total_clicks = 200

	for i in xrange(1, total_clicks):
		im = get_image(random_id, uniqid)
		image_bits_str = convert_image_to_image_bit_str(im)

		if is_dupe(i, image_bits_str, current_list):
			continue

		current_list.append(image_bits_str)
		save_image(im, instance, i)
		print '%s: New Image' % i
	
	display_results_count(current_list, image_bits_str, total_clicks)
		

def forever():
	while True:
		save_images()
		download_images('')

def loop():
	for i in xrange(1000):
		download_images('_' + i)

def main():
	global k
	k = KoC('greenspoon')
	forever()
	
if __name__ == "__main__":
	main()