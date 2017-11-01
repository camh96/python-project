from Ship import Ship
from Grid import Grid
from Command import Command
from itertools import chain

stillPlaying = True

while stillPlaying:
	cmd = Command().get_user_input()

	if cmd == 'exit':
		stillPlaying = False

def get_grid():
	grid = Grid(5,5)
	grid = grid.make_grid
	return grid