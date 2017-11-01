from Ship import Ship
from Grid import Grid
from Command import Command
from itertools import chain

# def make_ship():
# 	ship1 = Ship('h',1,1)
# 	ship2 = Ship('v',2,3)

# 	return ship1,ship2

for x in range(1,4):
	Command().get_user_input()

def get_grid():
	grid = Grid(5,5)
	grid = grid.make_grid
	return grid