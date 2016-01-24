class Grid:
	def __init__(self):
		pass

	def _display(self, grid):
		# headers
		for i in range(len(grid[0]) + 1):
			if i == 0:
				# column for row numbers
				print "   ",
			else:
				# column headers
				print "{0:2d} ".format(i),
		print
		for i, row in enumerate(grid, 1):
			# row number
			print "{0:2d} ".format(i),
			for col in row:
				# row data
				if col == None: 	
					print " {0} ".format("."),
				else:
					print " {0} ".format(col),
			print

	def display(self, grid):
		self._display(grid)

instance = None

def create_instance(function):
	global instance
	if not instance:
		instance = Grid()
	return function

@create_instance
def display(grid):
	'''Grid must be a list of rows. Rows should be a list of column values.'''
	instance.display(grid)

def main():
	display([['','',''],['','',''],['a','b','c']])

if __name__ == '__main__':
	main()