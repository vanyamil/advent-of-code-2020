from typing import Tuple

INPUT_FILE = "../inputs/13.txt"

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python
def extendedGCD(a: int, b: int) -> Tuple[int, int, int]:
	"""return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
	x0, x1, y0, y1 = 0, 1, 1, 0
	while a != 0:
		(q, a), b = divmod(b, a), a
		y0, y1 = y1, y0 - q * y1
		x0, x1 = x1, x0 - q * x1
	return b, x0, y0

# Return x^-1 mod n, aka a number y between 0 and n-1 such that xy = 1 mod n
def modularInverse(x, n):
	_num = extendedGCD(x, n)[1]
	while _num < 0:
		_num += n
	return _num

def step1():
	with open(INPUT_FILE) as f:
		num = int(f.readline())
		busses = [int(x) for x in f.readline().split(',') if x is not 'x']

	mins = 0
	while True:
		for x in busses:
			if num % x is 0:
				print(mins * x)
				return
		mins += 1
		num += 1

def step2():
	with open(INPUT_FILE) as f:
		f.readline() # Skip first line
		busses = [(int(x) if x is not 'x' else x) for x in f.readline().split(',')]

	quotient = (0, 1) # We want 0 mod 1 aka any integer
	for idx in range(len(busses)):
		x = busses[idx]
		if x is 'x':
			continue

		# CRT Local problem - we need -idx mod x AND num mod product of all previous
		residue = (x * x - idx) % x # Guarantee it's positive
		n1inv = modularInverse(quotient[1], x)
		k = ((residue - quotient[0]) * n1inv) % x
		new_prod = quotient[1] * x
		result = k * quotient[1] + quotient[0]
		quotient = (result, new_prod)
		print(quotient)

if __name__ == '__main__':
	step1()
	step2()