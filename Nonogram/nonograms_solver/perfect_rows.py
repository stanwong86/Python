class PerfectRows:
	def set_rows(self, row_pattern, grid_row):
		pattern_numbers = row_pattern.split()
		grid_row_length = len(grid_row)
		
		index = 0
		for pattern_number in pattern_numbers:
			for unused in range(int(pattern_number)):
				grid_row[index] = 'Y'
				index += 1
			if index >= grid_row_length:
				break
			grid_row[index] = 'X'
			index += 1
		return grid_row

	def is_perfect(self, row_pattern, grid_row):
		pattern_numbers = row_pattern.split()
		grid_row_length = len(grid_row)
		pattern_capacity = self._get_pattern_capacity(pattern_numbers)
		if pattern_capacity == grid_row_length:
			return True
		return False

	def _get_pattern_capacity(self, pattern_numbers):
		white_space_count = len(pattern_numbers) - 1
		sum = int(reduce(lambda a, b: int(a) + int(b), pattern_numbers)) 
		sum += white_space_count
		return sum