import pattern_numbers
import grid as grid_mod
import nonograms_solver

class Nonograms:
	def __init__(self):
		self.column_pattern = None
		self.row_pattern = None
		self.grid = None

	def initialize_blank_grid(self):
		self.initialize_pattern_numbers()
		grid = []
		grid_length = len(self.column_pattern)
		for i in range(grid_length):
			blank_row = ['' for i in range(grid_length)]
			grid.append(blank_row)
		self.grid = grid

	def initialize_pattern_numbers(self):
		self.column_pattern = pattern_numbers.get_column_pattern()
		self.row_pattern = pattern_numbers.get_row_pattern()

def main():
	game = Nonograms()
	game.initialize_blank_grid()
	grid_mod.display(game.grid)

	nonograms_solver.solve(game)
	grid_mod.display(game.grid)

if __name__ == '__main__':
	main()