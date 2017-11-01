from Ship import Ship
import os
import re

class Command():

	def get_user_input(self):

		stillPlaying = True #set loop to true, until it is set to false upon exit

		while stillPlaying:

			command = input('Battleships >>> ')

			#if user enters nothing, will prompt for input, as empty strings are 'falsy'

			if not command:
				print('Enter something!') 
				continue

			if command.split()[0] == 'place':

				#code for making ships

				#uses a regular expression to check if string matches the pattern required.

				#TODO: if 

				if(re.match(r'^[hv]\s[^\D]\s[^\D]', command[6:])): """regex explained: if there is either h or v after 6 characters, followed by a space, a number, a space
																	then another number, then it is valid place command """
					orientation = command.split()[1]
					x = command.split()[2]
					y = command.split()[3]
					Ship().place_ship(orientation,x,y)
				else:
					print('Input invalid, please try again') # if it doesn't match the regex try again


			elif command.split()[0] == 'show':
				print(Ship.list_ships()) """use the static show method on ships to list all ships, 
											since its static we don't need an instance to call the method"""


			elif command.split()[0] == 'exit':
				print('Thanks for playing! ') # if user types exit, break the loop
				stillPlaying = False
