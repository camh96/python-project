class Welcome():

	@staticmethod
	def welcome_user():
		print('\n\nWelcome to the battleships CLI game. To get started: \nPlace a ship by using the place command:')
		print('place [orientation] [x] [y], where [orientation] is h or v, and [x] [y] are numbers 1-4')
		print('Make sure to include a space after every character. If you get it wrong just try again.')
		print('To show ships that are on the board, use the keyword "show" ')
		print('If you get stuck at all and want to see this message again, use the command "help" \n\n')