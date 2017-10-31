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

			placement = sea[ship:ship+3]

			print ('Orientation is horizontal')
			print('Ship has been placed at {}'.format(placement))

			return placement

		elif self.orientation == 'v':

			mid = ship+5
			end = mid+5

			placement = [ sea[ship],sea[mid],sea[end] ]

			print('Orientation is vertical')
			print('Ship placed at {}'.format( placement ))

			return placement
			

		else:
			print('Orientation is invalid, please enter either h or v')
