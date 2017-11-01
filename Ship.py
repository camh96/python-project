from Grid import Grid
from Sea import Sea

class Ship:

	ships_on_sea = []

	def place_ship(self, orientation, x, y):

		self.orientation = str(orientation)
		self.x = int(x)
		self.y = int(y)
		
		sea = Grid(5,5).make_grid()

		if((self.x,self.y) not in sea):
			print('Ship does not fit on the board, try again.')
			return

		ship = sea.index((self.x,self.y))
	
		if self.orientation =='h':

			placement = sea[ship:ship+3]

			print ('Orientation is horizontal')
			print('Ship has been placed at {}'.format(placement))

			self.ships_on_sea.append(placement)

		elif self.orientation == 'v':

			mid = ship+5
			end = mid+5

			placement = [ sea[ship],sea[mid],sea[end] ]

			print('Orientation is vertical')
			print('Ship placed at {}'.format( placement ))

			self.ships_on_sea.append(placement)

		else:
			print('Orientation is invalid, please enter either h or v')

	@staticmethod
	def list_ships():

		ships = Ship.ships_on_sea

		for items in ships:
			print('Ship at {}'.format(items))

