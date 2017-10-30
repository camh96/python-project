from Grid import Grid

class Ship:

	def __init__(self, orientation, x, y):
		self.orientation = str(orientation)
		self.x = x
		self.y = y

	def place_ship(self):
		sea = Grid(5,5).make_grid()

		front = sea.index((self.x,self.y))
		mid = front+1
		rear = mid+1

		if self.orientation =='h':
			print ('Orientation is horizontal')
			print('{} {} {} are the coords'.format(sea[front], sea[mid], sea[rear]))

		elif self.orientation == 'v':
			print('Orientation is vertical')

		else:
			print('Orientation is invalid, please enter either h or v')
