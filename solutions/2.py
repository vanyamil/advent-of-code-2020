INPUT_FILE = "../inputs/2.txt"

def step1():
	_sum = 0
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			[_range, letter, pw] = line.split()
			letter = letter[0]
			_range = list(map(int, _range.split('-')))
			_count = pw.count(letter)
			if _count >= _range[0] and _count <= _range[1]:
				_sum += 1

	print(_sum)

def step2():
	_sum = 0
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			[_range, letter, pw] = line.split()
			letter = letter[0]
			_range = list(map(int, _range.split('-')))
			_len = len(pw)
			has_first = _range[0] <= _len and pw[_range[0] - 1] is letter
			has_second = _range[1] <= _len and pw[_range[1] - 1] is letter
			if has_first ^ has_second:
				_sum += 1

	print(_sum)

if __name__ == '__main__':
	step1()
	step2()