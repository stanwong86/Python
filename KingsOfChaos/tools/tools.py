# coding: utf-8
import sys
import os
import datetime
import inspect
from shutil import copyfile

def read_file(filename):
	with open(filename, 'r') as myfile:
		data = myfile.read()
	return data

def append_to_file(filename, data):
	with open(filename, "a") as text_file:
		text_file.write(data)
	return filename

def create_directory(directory):
	folder = os.path.join(os.getcwd(), directory)
	if not os.path.exists(folder):
		os.makedirs(folder)

def _raise_exception(function):
	raise Exception('{} needs to be implemented in tools package.'.format(function))

def write_to_file(filename, data):
	filename = write_to_file_silently(filename,data)
	print('\nGenerated {}\n'.format(filename))

def write_to_file_silently(filename, data):
	with open(filename, "w") as text_file:
		text_file.write(data)
	return filename

def log(msg, silent=False):
	if not silent:
		print(msg)
	date = datetime.datetime.now().strftime("%Y%m%d")
	date_time = datetime.datetime.now().strftime("%X")
	file_path = inspect.stack()[-1][1]
	file_name = file_path.split('\\')
	sub_fname = file_name[-1].split('.')[0]

	create_directory('log')
	fname = 'log/{}_{}.log'.format(sub_fname, date)
	with open(fname, "a") as text_file:
		text_file.write(date_time + '|' + msg + '\n')

def get_local_filename(fname):
	name, ext = fname.rsplit('.', 1)
	local_fname = '{}.mine.{}'.format(name, ext)
	if not os.path.isfile(local_fname):
		if not os.path.isfile(fname):
			sys.exit('Could not find file name {%s}' % (local_fname))
		copyfile(fname, local_fname)
	return local_fname
