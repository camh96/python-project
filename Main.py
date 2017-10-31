from Ship import Ship
from Grid import Grid
import gc

def make_ship():
	ship1 = Ship('h',1,1)
	ship2 = Ship('v',2,3)
	ship3 = Ship('v',0,4)

	return ship1,ship2,ship3

def float_ship():

	ship1.place_ship()
	ship2.place_ship()
	ship3.place_ship()

def get_grid():
	grid = Grid(5,5)
	grid = grid.make_grid
	return grid

def show_ships():
	for obj in gc.get_objects(): # use built in garbage collector to list instances of ship object
	    if isinstance(obj, Ship):
	        print ('Ship found at {}'.format(obj.place_ship()))