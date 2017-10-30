class Ship:

	def __init__(self, orientation, x, y, size):
		self.orientation = str(orientation)
		self.x = x
		self.y = y
		self.size = size

	@property
	def place_ship(self):
		return self.orientation