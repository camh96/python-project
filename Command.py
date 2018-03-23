from Ship import Ship
from Welcome import Welcome
import re # regular expressions

class Command():

	def get_user_input(self):

		stillPlaying = True #set loop to true, until it is set to false upon exit

		while stillPlaying:

			command = input('\n\nBattleships >>> ')

			#if user enters nothing, will prompt for input, as empty strings are 'falsy'

			if not command:
				print('Enter something!') 
				continue
				
			if command.split()[0] == 'place':

				#code for making ships

				#uses a regular expression to check if string matches the pattern required.

				if(re.match(r'^[hv]\s[^\D]\s[^\D]', command[6:])):

					try:
						orientation = command.split()[1]
						x = command.split()[2]
						y = command.split()[3]
						
						if orientation == 'h' and int(y) > 2:
							print('The coordinates you have entered will put the ship out of bounds. Please try agian.')
							continue

						Ship().place_ship(orientation,x,y)
					except:
						print('Ship wont fit on the board, try again') #if ship not on board, ignore
						continue
				else:
					print('Input not valid, please user either h or v for orientation') # if it doesn't match the regex try again


			elif command.split()[0] == 'show':
				Ship.list_ships()

			elif command.split()[0] == 'help':
				Welcome.welcome_user()	

			elif command.split()[0] == 'visual':
				Vis.show_table()	

			elif command.split()[0] == 'exit':
				print('Thanks for playing! ') # if user types exit, break the loop
				stillPlaying = False
