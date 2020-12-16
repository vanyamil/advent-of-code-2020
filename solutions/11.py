INPUT_FILE = "../inputs/11.txt"
FLOOR = '.'
SEAT_OCC = '#'
SEAT_EMPTY = 'L'
DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class CellAutomata:
	def __init__(self, grid, rule):
		self.grid = grid
		self.rule = rule
		self.size = (len(grid), len(grid[0]))
		print("Grid size: {0}x{1}".format(*self.size))

	def simulate(self):
		# Deep copy
		backup = [[el for el in row] for row in self.grid]
		cnt = 0
		# Iterate
		for row in range(self.size[0]):
			for col in range(self.size[1]):
				new_el = self.rule(backup, self.size, row, col)
				self.grid[row][col] = new_el
				if backup[row][col] != new_el:
					cnt += 1
		# Return num of changes
		return cnt

def seatEvolution1(grid, size, row, col):
	if grid[row][col] is FLOOR:
		return FLOOR
	
	if grid[row][col] is SEAT_EMPTY:
		for x in range(max(0, row - 1), min(row + 2, size[0])):
			for y in range(max(0, col - 1), min(col + 2, size[1])):
				if grid[x][y] is SEAT_OCC:
					return SEAT_EMPTY
		return SEAT_OCC

	if grid[row][col] is SEAT_OCC:
		cnt = 0
		for x in range(max(0, row - 1), min(row + 2, size[0])):
			for y in range(max(0, col - 1), min(col + 2, size[1])):
				if x is row and y is col:
					continue
				if grid[x][y] is SEAT_OCC:
					cnt += 1
		return SEAT_OCC if cnt < 4 else SEAT_EMPTY

def findNextSeat(grid, size, row, col, dir_):
	curRow = row + dir_[0]
	curCol = col + dir_[1]
	while curRow >= 0 and curRow < size[0] and curCol >= 0 and curCol < size[1]:
		if grid[curRow][curCol] is not FLOOR:
			return grid[curRow][curCol]
		curRow += dir_[0]
		curCol += dir_[1]

	# Reached end of grid
	return FLOOR

def seatEvolution2(grid, size, row, col):
	if grid[row][col] is FLOOR:
		return FLOOR
	
	if grid[row][col] is SEAT_EMPTY:
		for dir_ in DIRS:
			foundSeat = findNextSeat(grid, size, row, col, dir_)
			if foundSeat is SEAT_OCC:
				return SEAT_EMPTY

		return SEAT_OCC

	if grid[row][col] is SEAT_OCC:
		cnt = 0
		for dir_ in DIRS:
			foundSeat = findNextSeat(grid, size, row, col, dir_)
			if foundSeat is SEAT_OCC:
				cnt += 1
				if cnt >= 5:
					return SEAT_EMPTY
		return SEAT_OCC

def step1():
	with open(INPUT_FILE) as f:
		grid = [list(x[:-1]) for x in f.readlines()]
	ca = CellAutomata(grid, seatEvolution1)
	cnt = 1
	iter_ = 1
	while cnt > 0:
		cnt = ca.simulate()
		print("Iteration {0}, {1} changes".format(iter_, cnt))
		iter_ += 1

	for row in ca.grid:
		for el in row:
			if el is SEAT_OCC:
				cnt += 1

	print("Count: {0}".format(cnt))

def step2():
	with open(INPUT_FILE) as f:
		grid = [list(x[:-1]) for x in f.readlines()]
	ca = CellAutomata(grid, seatEvolution2)
	cnt = 1
	iter_ = 1
	while cnt > 0:
		cnt = ca.simulate()
		print("Iteration {0}, {1} changes".format(iter_, cnt))
		iter_ += 1

	for row in ca.grid:
		for el in row:
			if el is SEAT_OCC:
				cnt += 1

	print("Count: {0}".format(cnt))

if __name__ == '__main__':
	# step1()
	step2()