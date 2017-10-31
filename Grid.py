import itertools

class Grid:

	def __init__(self, x_size, y_size):
		self.x_size = x_size
		self.y_size = y_size

	def make_grid(self):
		#use itertools to generate a list of values to represent to grid area, 0,0 to 4,4
		grid = list(itertools.product(range(self.x_size), range(self.y_size)))
		return grid