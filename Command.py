from Ship import Ship

class Command():

	def __init__(self):
		self.ship1 = []
		self.ship2 = []

	def get_user_input(self):

		command = input('>>> ')

		if command.split()[0] == 'place':
			#code for making ships

			orientation = command.split()[1]
			x = command.split()[2]
			y = command.split()[3]

			Ship().place_ship(orientation,x,y)


		elif command.split()[0] == 'show':
			print(Ship.list_ships())


		elif command.split()[0] == 'exit':
			print('Thanks for playing! ')
			stillPlaying = False
			break
