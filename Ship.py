from Grid import Grid

class Ship:

	def __init__(self, orientation, x, y):
		self.orientation = str(orientation)
		self.x = x
		self.y = y

	def place_ship(self):
		sea = Grid(5,5).make_grid()

		ship = sea.index((self.x,self.y))

		if self.orientation =='h':
			print ('Orientation is horizontal')
			print('Coords are {}'.format(sea[ship:ship+3]))

		elif self.orientation == 'v':
			print('Orientation is vertical')

		else:
			print('Orientation is invalid, please enter either h or v')
