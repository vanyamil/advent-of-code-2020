INPUT_FILE = "../inputs/12.txt"
NORTH = (0, 1)
SOUTH = (0, -1)
EAST = (1, 0)
WEST = (-1, 0)
DIRS = {'N': NORTH, 'E': EAST, 'S': SOUTH, 'W': WEST}
DIRS_LIST = [NORTH, EAST, SOUTH, WEST]
START_WP = (10, 1)

def calcMove(curPos, curDir, move):
	type_ = move[0]
	num_ = int(move[1:])
	if type_ in DIRS:
		curPos = (curPos[0] + num_ * DIRS[type_][0], curPos[1] + num_ * DIRS[type_][1])
	elif type_ is 'F':
		curPos = (curPos[0] + num_ * curDir[0], curPos[1] + num_ * curDir[1])
	else:
		num_ /= 90
		if type_ is 'L':
			num_ = -num_
		curIdx = (DIRS_LIST.index(curDir) + 4 + int(num_)) % 4
		curDir = DIRS_LIST[curIdx]

	return (curPos, curDir)

def calcWPMove(curPos, curWP, move):
	type_ = move[0]
	num_ = int(move[1:])
	if type_ in DIRS:
		curWP = (curWP[0] + num_ * DIRS[type_][0], curWP[1] + num_ * DIRS[type_][1])
	elif type_ is 'F':
		curPos = (curPos[0] + num_ * curWP[0], curPos[1] + num_ * curWP[1])
	else:
		num_ = int(num_ / 90)
		if type_ is 'L':
			num_ = 4 - num_
		
		curWP = [
			lambda x, y: (x, y),
			lambda x, y: (y, -x),
			lambda x, y: (-x, -y),
			lambda x, y: (-y, x)
		][num_](*curWP)

	return (curPos, curWP)

def step1():
	curDir = EAST
	curPos = (0, 0)
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			line = line[:-1]
			(curPos, curDir) = calcMove(curPos, curDir, line)

	print(abs(curPos[0]) + abs(curPos[1]))

def step2():
	curWP = START_WP
	curPos = (0, 0)
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			line = line[:-1]
			(curPos, curWP) = calcWPMove(curPos, curWP, line)

	print(abs(curPos[0]) + abs(curPos[1]))

if __name__ == '__main__':
	step1()
	step2()