import itertools

class Grid:

	def __init__(self, x_size, y_size):
		self.x_size = x_size
		self.y_size = y_size

	def make_grid(self):
		grid = list(itertools.product(range(self.x_size), range(self.y_size)))
		return grid