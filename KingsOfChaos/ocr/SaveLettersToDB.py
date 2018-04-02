import sys
import os
import re
import requests
sys.path.append('../sql')
from PIL import Image
sys.path.append('C:\\dev\\python\\KingsOfChaos')
import tools
from sql_util import *
import time
from Tkinter import Tk, Label, Button

def get_image_bits_from_image_name(img_name):
	im = Image.open(img_name, 'r')
	image_bits = list(im.getdata())
	image_bits_str = ''.join(map(str, image_bits))
	return image_bits_str

def db_insert_image_bits_str(letter_to_save, image_bits_str):
	results = select("where letter_bits='%s'" % (image_bits_str))
	if results:
		print 'Letter Bits for {%s} already exists.' % letter_to_save
	else:
		result = insert(letter_to_save, image_bits_str)
		if result:
			print result[1]
		return True

def save_letters_to_database(letter_to_save, mypath, img_names):
	letter_inserted_count = 0
	for img_name in img_names:
		print 'Processing %s' % img_name
		img_path = os.path.join(mypath, img_name)
		image_bits_str = get_image_bits_from_image_name(img_path)

		if len(image_bits_str) != 79200:
			print 'Length {%s} does not match {%s}' % (len(image_bits_str), 79200)
			sys.exit(0)
		
		if db_insert_image_bits_str(letter_to_save, image_bits_str):
			letter_inserted_count += 1
	print 'Inserted %s letters' % (letter_inserted_count)
	

def remove_letters_to_database():
	''' not working '''
	letter_inserted_count = 0
	for i in xrange(1, 999):
		img_name = 'ocr/letters/letter%s.png' % i
		image_bits_str = get_image_bits_from_image_name(img_name)
		delete('where letter_bits=%s' % (image_bits_str))

def get_time():
	return time.strftime("%H%M%S")
	
def move_files_to_folder(letter, mypath, img_names):
	current_time = get_time()
	for i in xrange(len(img_names)):
		old_file_path = os.path.join(mypath, img_names[i])
		new_file_path = os.path.join(mypath, letter, '%s_%s_%s.png' % (letter, current_time, i))
		os.rename(old_file_path, new_file_path)
	print 'Files Moved to folder {%s}' % letter

def popup():
	root = Tk()
	root.title("Say Hello")
	label = Label(root, text="Pop Up")
	label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
	button = Button(root, text="OK", command=lambda: root.destroy())
	button.pack(side="bottom", fill="none", expand=True)
	root.mainloop()

def save_images():
	popup()
	letter_to_save = raw_input('Letter to Save: ')
	if letter_to_save not in 'kingchaos ':
		sys.exit('Unknown Letter {%s}' % letter_to_save)

	mypath = 'C:/Users/stanley.wong/Documents/Python_Scripts/Prototypes/KingsOfChaos/ocr/letters'
	img_names = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.find('.png') > -1]

	save_letters_to_database(letter_to_save, mypath, img_names)
	move_files_to_folder(letter_to_save, mypath, img_names)

def save_letters_manually(group_to_save, letter_to_save):
	mypath = 'C:/Users/stanley.wong/Documents/Python_Scripts/Prototypes/KingsOfChaos/ocr/letters'
	onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.find('.png') > -1]
	existing_groups = []
	img_names = []
	for f in onlyfiles:
		group = f.split('_')[1]
		if group_to_save == group:
			img_names.append(f)

		if group in existing_groups:
			continue	

		existing_groups.append(group)

	print len(existing_groups)
	print len(onlyfiles)
	print img_names

	save_letters_to_database(letter_to_save, mypath, img_names)
	move_files_to_folder(letter_to_save, mypath, img_names)

def main():
	save_images()
	#remove_letters_to_database()

if __name__ == "__main__":
	main()