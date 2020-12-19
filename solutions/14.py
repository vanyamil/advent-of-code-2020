INPUT_FILE = "../inputs/14.txt"

def intersect(val, mask):
	str_ = list(bin(val)[2:].zfill(36))
	res_ = []
	for idx in range(36):
		res_.append(str_[idx] if mask[idx] is 'X' else mask[idx])
	return int(''.join(res_), 2)

def intersectAddress(address, mask):
	str_ = bin(address)[2:].zfill(36)
	res_ = []
	# Modify str_ to include mask Xs
	trueStr = []
	for idx in range(36):
		if mask[idx] is '0':
			trueStr.append(str_[idx])
		else:
			trueStr.append(mask[idx])
	st = [''.join(trueStr)]
	
	while len(st) > 0:
		curr = st.pop()
		idx = curr.find('X')
		if idx < 0:
			res_.append(curr)
		else:
			st.append(curr[:idx] + '0' + curr[idx+1:])
			st.append(curr[:idx] + '1' + curr[idx+1:])
	return res_

def step1():
	mask = list() # First line always mask
	memory = dict()

	with open(INPUT_FILE) as f:
		for line in f.readlines():
			# Mask
			if line[1] is 'a':
				mask = list(line[7:-1])
			else:
				endIdx = line.index(']')
				address = int(line[4:endIdx])
				val = int(line[endIdx+4:-1])
				trueVal = intersect(val, mask)
				memory[address] = trueVal

	print(sum(memory.values()))

def step2():
	mask = list() # First line always mask
	memory = dict()

	with open(INPUT_FILE) as f:
		for line in f.readlines():
			# Mask
			if line[1] is 'a':
				mask = list(line[7:-1])
			else:
				endIdx = line.index(']')
				address = int(line[4:endIdx])
				trueAddresses = intersectAddress(address, mask)
				val = int(line[endIdx+4:-1])
				for x in trueAddresses:
					memory[x] = val

	print(sum(memory.values()))

if __name__ == '__main__':
	step1()
	step2()