class PatternNumbers:
	def __init__(self):
		self.columns_file = 'columns.txt'
		self.rows_file = 'rows.txt'

	def _get_pattern_numbers_from_file(self, pattern_file):
		pattern_numbers = open(pattern_file)
		pattern_list = []
		for number in pattern_numbers:
			pattern_list.append(number.rstrip())
		pattern_numbers.close()
		return pattern_list

	def get_column_pattern(self):
		return self._get_pattern_numbers_from_file(self.columns_file)

	def get_row_pattern(self):
		return self._get_pattern_numbers_from_file(self.rows_file)

	def set_columns_file(self, file_name):
		self.columns_file = file_name

	def set_rows_file(self, file_name):
		self.rows_file = file_name

instance = None

def create_instance(function):
	global instance
	if not instance:
		instance = PatternNumbers()
	return function

@create_instance
def get_column_pattern():
	return instance.get_column_pattern()

@create_instance
def get_row_pattern():
	return instance.get_row_pattern()

@create_instance
def set_columns_file(file_name):
	instance.set_columns_file(file_name)

@create_instance
def set_rows_file(file_name):
	instance.set_rows_file(file_name)

def main():
	print get_column_pattern()
	print get_row_pattern()

if __name__ == '__main__':
	main()