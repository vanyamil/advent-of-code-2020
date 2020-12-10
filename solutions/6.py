INPUT_FILE = "../inputs/6.txt"

def step1():
	curSet = set()
	_sum = 0
	_count = 0
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			# End of group
			if len(line) < 2:
				_sum += len(curSet)
				_count += 1
				curSet.clear()

			# Otherwise, parse 
			for ch in line[:-1]:
				curSet.add(ch)

		# Last group
		_sum += len(curSet)
		_count += 1

	print("Sum: " + str(_sum))
	print("Count: " + str(_count))

def step2():
	curSet = set()
	localSet = set()
	_sum = 0
	_count = 0
	_fresh = True
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			# End of group
			if len(line) < 2:
				_sum += len(curSet)
				_count += 1
				curSet.clear()
				_fresh = True
				continue

			# Otherwise, parse 
			localSet.clear()
			for ch in line[:-1]:
				localSet.add(ch)

			if _fresh:
				curSet |= localSet
				_fresh = False
			else:
				curSet &= localSet

		# Last group
		_sum += len(curSet)
		_count += 1

	print("Sum: " + str(_sum))
	print("Count: " + str(_count))

if __name__ == '__main__':
	step1()
	step2()