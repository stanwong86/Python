# coding: utf-8

import MySQLdb
import atexit

db = None

def requires_db(decorated_function):
	def new_func(*args, **kwargs):
		global db
		if not db:
			db = MySQLdb.connect(host="127.0.0.1",port=3306,user="stan",passwd="stan",db="koc")
		return decorated_function(*args)
	return new_func

@requires_db
def select(where_clause=''):
	cursor = db.cursor()
	cursor.execute("SELECT * FROM letters %s" % where_clause)
	data = cursor.fetchall()
	cursor.close()
	return data

@requires_db
def insert(letter, value):
	cursor = db.cursor()
	sql = "insert into letters VALUES(null, '%s', '%s')" % (letter, value)
	
	try:
		number_of_rows = cursor.execute(sql)
	except Exception, e:
		return e
	print 'Inserted %s rows' % number_of_rows
	db.commit()   # you need to call commit() method to save
	cursor.close()

@requires_db
def delete(where_clause=''):
	cursor = db.cursor()
	if not where_clause:
		return

	sql = "delete from letters %s" % (where_clause)
	
	try:
		number_of_rows = cursor.execute(sql)
	except Exception, e:
		return e
	print 'Deleted %s rows' % number_of_rows
	db.commit()   # you need to call commit() method to save
	cursor.close()

def exit_handler():
	if db:
		db.close()

atexit.register(exit_handler)

def main():
	#print select()
	#	insert('a', '1001101001101010101001101010100101101010101001')
	print select()

if __name__ == "__main__":
	main()