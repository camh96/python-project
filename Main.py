from Ship import Ship
from Grid import Grid
from Command import Command
from itertools import chain

stillPlaying = True

while stillPlaying:
	cmd = Command().get_user_input()

	if cmd == 'exit':
		break
		stillPlaying = False

print('Hello')