from Ship import Ship
from Grid import Grid
from Command import Command
from itertools import chain

stillPlaying = True

while stillPlaying:
	Command().get_user_input()

def get_grid():
	grid = Grid(5,5)
	grid = grid.make_grid
	return grid