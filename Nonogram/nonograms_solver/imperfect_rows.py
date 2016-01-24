class ImperfectRows:
	def set_rows(self, nonogram):
		self.set_imperfect_row(nonogram.row_pattern, nonogram.grid[0])
		# TODO: Need to permute the second number

	def set_imperfect_row(self, pattern_numbers, row):
		index = 0
		row_count = len(row)
		
		for pattern_number in pattern_numbers:
			if index == row_count:
				print 'out of index'
			index = self.set_pattern_number_in_row(row, index, pattern_number)

	def fill_row_with_pattern(self, row, index, pattern_number):
		row_count = len(row)
		remaining_slots = row_count - index
		if int(pattern_number) <= remaining_slots:
			for unused in range(1, int(pattern_number)+1):
				if index < row_count:
					row[index] = 'Y'
					index += 1
			if index < row_count:
				row[index] = 'x'
				index += 1
		return index

	def set_pattern_number_in_row(self, row, current_index, pattern_number):
		row_count = len(row)
		for index in range(current_index, row_count):
			if row[index] == '' or row[index] == 'x':
				index = self.fill_row_with_pattern(row, index, pattern_number)
				return index
			elif row[index] == 'Y':
				row[index] = 'x'
				index += 1
				return self.fill_row_with_pattern(row, index, pattern_number)
		return current_index