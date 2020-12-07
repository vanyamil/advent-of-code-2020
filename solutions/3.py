INPUT_FILE = "../inputs/3.txt"
WIDTH = 31
TREE = '#'

def checkSlope(lines, right, down):
	_count = 0
	x = 0
	y = 0
	for line in lines:
		# Skip any mid lines if we move more than one line down
		if y % down is not 0:
			y += 1
			continue

		if line[x] is TREE:
			_count += 1
		y += 1
		x = (x + right) % WIDTH

	return _count

def step1():
	with open(INPUT_FILE) as f:
		print(checkSlope(f.readlines(), 3, 1))

def step2():
	with open(INPUT_FILE) as f:
		lines = f.readlines()

	prod = 1

	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	for (right, down) in slopes:
		prod *= checkSlope(lines, right, down)

	print(prod)

if __name__ == '__main__':
	step1()
	step2()