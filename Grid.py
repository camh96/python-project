import itertools

class Grid:

	def __init__(self, x_size, y_size):
		self.x_size = x_size
		self.y_size = y_size 

	def make_grid():
		grid = list(itertools.product(range(x_size), range(y_size)))
		return grid

	print(make_grid())


