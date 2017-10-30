from Grid import Grid

class Ship:

	def __init__(self, orientation, x, y):
		self.orientation = str(orientation)
		self.x = x
		self.y = y

	# @property
	def place_ship(self):
		return self.orientation, self.x, self.y