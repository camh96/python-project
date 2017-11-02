from Grid import Grid
from Sea import Sea

class Ship:

	ships_on_sea = []

	def check_overlapping(placement):
		for x in placement:
			for y in Ship.ships_on_sea:
				if x in y:
					print('There is already a ship there, ships cannot overlap.')
					return False


	def place_ship(self, orientation, x, y):

		self.orientation = str(orientation)
		self.x = int(x)
		self.y = int(y)
		
		sea = Sea().make_sea(5,5)

		if ((self.x,self.y) not in sea):
			print('Ship does not fit on the board, try again.')
			return

		ship = sea.index((self.x,self.y))
	
		if self.orientation == 'h':

			if self.y >= 3:
				print('Ship doesn\'t fit within the board!')
				return

			placement = sea[ship:ship+3]

			check = Ship.check_overlapping(placement)

			if check != False:
				print ('Orientation is horizontal')
				print('Ship has been placed at {}'.format(placement))

				self.ships_on_sea.append(placement)

		elif self.orientation == 'v':

			mid = ship+5
			end = mid+5

			placement = [ sea[ship],sea[mid],sea[end] ]

			check = Ship.check_overlapping(placement)

			if check != False:
				print('Orientation is vertical')
				print('Ship placed at {}'.format( placement ))

				self.ships_on_sea.append(placement)

		else:
			print('Orientation is invalid, please enter either h or v')

	@staticmethod
	def list_ships():

		ships = Ship.ships_on_sea

		if not ships:
			print('No ships added! You can add one using "place [orientation] [x] [y] like: h 1 0"')

		else:
			print('Ships found at: ')

			for items in ships:
				print('Ship at {}'.format(items))

