INPUT_FILE = "../inputs/4.txt"
REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def testCurPass1(curPass):
	for key in REQUIRED_KEYS:
		if key not in curPass:
			return False

	return True

def testCurPass2(curPass):
	# Do tests
	for key in REQUIRED_KEYS:
		if key not in curPass:
			return False

	byr = int(curPass['byr'])
	if byr < 1920 or byr > 2002:
		return False

	iyr = int(curPass['iyr'])
	if iyr < 2010 or iyr > 2020:
		return False

	eyr = int(curPass['eyr'])
	if eyr < 2020 or eyr > 2030:
		return False

	hgt = curPass['hgt']
	if len(hgt) < 4:
		return False
	if hgt[-2:] == 'cm':
		try:
			hgtnum = int(hgt[:-2])
			if hgtnum < 150 or hgtnum > 193:
				return False
		except:
			return False
	elif hgt[-2:] == 'in':
		try:
			hgtnum = int(hgt[:-2])
			if hgtnum < 59 or hgtnum > 76:
				return False
		except:
			return False
	else:
		return False

	hcl = curPass['hcl']
	# Could regex here but need package, just bothersome
	if len(hcl) is not 7 or hcl[0] is not '#':
		return False
	try:
		_ = int(hcl[1:], 16)
	except:
		return False

	ecl = curPass['ecl']
	if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False

	pid = curPass['pid']
	if len(pid) is not 9 or not pid.isnumeric():
		return False

	return True

def compute(testPass):
	_curPass = {}
	_sum = 0
	_count = 0
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			# End of passport
			if len(line) < 2:
				_sum += testPass(_curPass)
				_count += 1
				_curPass = {}

			# Otherwise, parse fields
			parts = map(lambda s : tuple(s.split(':')), line.split())
			_curPass.update(parts)

		# Last passport
		_sum += testPass(_curPass)
		_count += 1

	print("Sum: " + str(_sum))
	print("Count: " + str(_count))

# 209 too low
def step1():
	compute(testCurPass1)

def step2():
	compute(testCurPass2)

if __name__ == '__main__':
	step1()
	step2()