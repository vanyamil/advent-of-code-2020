INPUT_FILE = "../inputs/5.txt"

def transform(_str):
	_str = (_str.replace('F', '0')
		.replace('B', '1')
		.replace('L', '0')
		.replace('R', '1'))

	return int(_str, 2)

def step1():
	_max = 0

	with open(INPUT_FILE) as f:
		for line in f.readlines():
			num = transform(line[:-1])
			if num > _max:
				_max = num

	print(_max)

def step2():
	l = []

	with open(INPUT_FILE) as f:
		for line in f.readlines():
			num = transform(line[:-1])
			l.append(num)

	l.sort()
	# Faster to read it yourself than write code to find it!
	print(l)

if __name__ == '__main__':
	step1()
	step2()