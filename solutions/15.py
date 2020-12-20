def sim(inp, limit = 2020):
	
	lastNum = inp[-1]
	idx = len(inp)
	inp = inp[:-1]

	lastRead = dict(zip(inp, range(1, idx + 1)))
	prevRead = dict()

	while idx < limit:
		if lastNum not in lastRead:
			lastRead[lastNum] = idx
			lastNum = 0
		else:
			prevRead[lastNum] = lastRead[lastNum]
			temp = idx - lastRead[lastNum]
			lastRead[lastNum] = idx
			lastNum = temp
		idx += 1

	print(lastNum)

if __name__ == '__main__':
	sim([5, 2, 8, 16, 18, 0, 1])
	# step1([0, 3, 6], 11)
	sim([5, 2, 8, 16, 18, 0, 1], 30000000)