INPUT_FILE = "../inputs/17.txt"
EMPTY = '.'
OCCUPIED = '#'
NEIGHBORHOOD = [-1, 0, 1]
DIRS = [(x, y, z) for x in NEIGHBORHOOD for y in NEIGHBORHOOD for z in NEIGHBORHOOD]

def div_round_up(a : int, b : int) -> int:
	'''Returns ceil(a / b) without going out of integers'''
	(result, residue) = divmod(a, b)
	return result if residue is 0 else result + 1

class NDList:
	def __init__(self, shape, defaultVal = None):
		if type(shape) is not tuple:
			raise TypeError('The shape must be a tuple, {0} given'.format(type(shape)))

		self.shape = shape
		self._dims = len(shape)

		self._size = 1
		self._multipliers = []
		for x in shape:
			self._size *= x
			self._multipliers = [x * y for y in self._multipliers] + [1]
		self._contents = [defaultVal] * self._size

	def __getitem__(self, idx):
		trueIdx = self._testIdx(idx)
		return self._contents[trueIdx]

	def __setitem__(self, idx, val):
		trueIdx = self._testIdx(idx)
		self._contents[trueIdx] = val

	def __len__(self):
		return self._size

	def __delitem__(self, key):
		self[key] = None

	def __iter__(self):
		return iter(self._contents)

	def _testShape(self, tup):
		if type(tup) is not tuple:
			raise TypeError('The index must be a tuple, {0} given'.format(type(tup)))
		if len(tup) is not self._dims:
			raise IndexError('The tuple must have {0} values, {1} received'.format(self._dims, len(tup)))
		for i in tup:
			if type(i) is not int:
				raise TypeError('The index must be an integer tuple')

	def _testIdx(self, idx):
		self._testShape(idx)

		result = 0
		for i in range(self._dims):
			if idx[i] < 0 or idx[i] >= self.shape[i]:
				raise IndexError('Incorrect index at dimension {0}: {1}'.format(i, idx[i]))
			result += self._multipliers[i] * idx[i]

		return result

	def idxGenerate(self, start = None, stop = None, step = None):
		if start is None:
			start = (0, ) * self._dims
		if stop is None:
			stop = self.shape
		if step is None:
			step = (1, ) * self._dims
		if 0 in step:
			raise ValueError('Slice step cannot be zero!')

		# Stop is exclusive : <
		curr = start
		while True:
			yield curr
			found = False
			# What's the furthest dimension we can step through?
			for i in range(self._dims - 1, -1, -1):
				if (curr[i] + step[i] - stop[i]) * (1 if step[i] > 0 else -1) < 0:
					found = True
					break
			# If we get out of here without finding, stop
			if not found:
				break
			
			# Increase at i, reset all below to start
			curr = curr[:i] + (curr[i] + step[i],) + start[i+1:]

	def slice(self, start = None, stop = None, step = None):
		if start is None:
			start = (0, ) * self._dims
		if stop is None:
			stop = self.shape
		if step is None:
			step = (1, ) * self._dims

		self._testIdx(start)
		self._testShape(stop)
		self._testShape(step)

		# Determine shape
		shape = tuple(div_round_up(stop[i] - start[i], step[i]) for i in range(self._dims))
		result = NDList(shape)
		result._contents = list(self[idx] for idx in self.idxGenerate(start, stop, step))
		return result

	def fill(self, items, start, stop):
		self._testShape(start)
		self._testIdx(stop)
		
		_num = 1
		for i in range(self._dims):
			_num *= (stop[i] - start[i])

		if len(items) is not _num:
			raise ValueError('{0} items have been provided, but the reserved space has space for {1} items.'.format(len(items), _num))

		# Iterate over the indices?
		for (item, idx) in zip(items, self.idxGenerate(start, stop)):
			self[idx] = item

	def clone(self):
		result = NDList(self.shape)
		result._contents = list(self.flatview())
		return result

	def flatview(self):
		return self._contents

class CellAutomata:
	def __init__(self, grid, rule):
		self.grid = grid
		self.rule = rule

	def simulate(self):
		# Deep copy
		backup = self.grid.clone()
		cnt = 0
		# Iterate
		for (key, el) in zip(self.grid.idxGenerate(), self.grid.flatview()):
			new_el = self.rule(el, key, backup)
			self.grid[key] = new_el
			if new_el != el:
				cnt += 1
		# Return num of changes
		return cnt

def conwayRule(el, key, grid):
	minKey = tuple(max(0, num - 1) for num in key)
	maxKey = tuple(min(grid.shape[i], key[i] + 2) for i in range(len(key)))

	cnt = grid.slice(minKey, maxKey).flatview().count(OCCUPIED)
	if el is OCCUPIED:
		# Stays active only if 2 or 3 neighbors (aka 3 or 4 in this count)
		return OCCUPIED if cnt is 3 or cnt is 4 else EMPTY
	else:
		# Becomes active if exactly 3 neighbors
		return OCCUPIED if cnt is 3 else EMPTY

def process(f):
	rows = [list(line[:-1]) for line in f.readlines()]
	shape = (len(rows), len(rows[0]))
	flatrows = [item for row in rows for item in row]
	grid = NDList(shape)
	grid._contents = flatrows
	return grid

def step1(startGrid):
	trueShape = (startGrid.shape[0] + 12, 13, startGrid.shape[1] + 12)
	trueGrid = NDList(trueShape, EMPTY)
	trueGrid.fill(startGrid, (6, 6, 6), (6 + startGrid.shape[0], 7, 6 + startGrid.shape[1]))
	ca = CellAutomata(trueGrid, conwayRule)
	for _ in range(6):
		ca.simulate()
	print(ca.grid.flatview().count(OCCUPIED))

def step2(startGrid):
	trueShape = (startGrid.shape[0] + 12, 13, startGrid.shape[1] + 12, 13)
	trueGrid = NDList(trueShape, EMPTY)
	trueGrid.fill(startGrid, (6, 6, 6, 6), (6 + startGrid.shape[0], 7, 6 + startGrid.shape[1], 7))
	ca = CellAutomata(trueGrid, conwayRule)
	for _ in range(6):
		ca.simulate()
	print(ca.grid.flatview().count(OCCUPIED))

if __name__ == '__main__':
	with open(INPUT_FILE) as f:
		startGrid = process(f)

	step1(startGrid)
	step2(startGrid)