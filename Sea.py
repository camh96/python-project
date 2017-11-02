from Grid import Grid

class Sea:

	def make_sea(self, x_size, y_size): 
		
		self.x_size = x_size
		self.y_size = y_size

		grid_area = Grid(x_size, y_size)
		
		return grid_area.make_grid()
