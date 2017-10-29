import itertools

class Grid:

	def make_grid():

		grid = list(itertools.product(range(5), range(5)))

		return grid

	print(make_grid())

