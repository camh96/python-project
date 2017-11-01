from Ship import Ship

class Command():

	def __init__(self):
		self.ship1 = []
		self.ship2 = []

	def get_user_input(self):

		command = input('Please enter the command you wish to use: ')

		if command.split()[0] == 'place':
			#code for making ships

			orientation = command.split()[1]
			x = command.split()[2]
			y = command.split()[3]

			Ship(orientation,x,y).place_ship()


		elif command.split()[0] == 'show ships':
			Ship.ships_on_sea


		elif command.split()[0] == 'exit':
			sys.exit('Thanks for playing! ')
			
			return