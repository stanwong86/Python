from perfect_rows import PerfectRows
from imperfect_rows import ImperfectRows

class NonogramsSolver:
	def __init__(self):
		self.perfect_rows = PerfectRows()
		self.imperfect_rows = ImperfectRows()

	def solve(self, nonogram):
		self.permutate_rows(nonogram)
		
	def permutate_rows(self, nonogram):
		row_length = len(nonogram.row_pattern)
		for row_index in range(row_length):
			row_pattern = nonogram.row_pattern[row_index]
			grid_row = nonogram.grid[row_index]
			if self.perfect_rows.is_perfect(row_pattern, grid_row):
				self.perfect_rows.set_rows(row_pattern, grid_row)
			else:
				#self.imperfect_rows.set_rows(nonogram)
				pass

def main():
	pass

if __name__ == '__main__':
	main()