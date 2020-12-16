INPUT_FILE = "../inputs/10.txt"

def step1():
	with open(INPUT_FILE) as f:
		sorted_list = list(sorted(map(lambda x: int(x[:-1]), f.readlines())))

	sorted_list.append(sorted_list[-1] + 3)
	sorted_list.insert(0, 0)
	ones, threes = 0, 0
	for i in range(len(sorted_list) - 1):
		diff = sorted_list[i+1] - sorted_list[i]
		if diff is 1:
			ones += 1
		elif diff is 3:
			threes += 1

	print("Step 1: {0}".format(ones * threes))
	return sorted_list

def step2(lst):
	# Find where in sorted list elements can be removed
	# Non-intersecting regions of those numbers lead to multiplied possibilities
	# We know for sure that any 3-diff leads to both numbers being locked
	# As does a 2 + 2 diff in 3 numbers
	# AKA we must have 1 diffs involved

	# 1 - 2, 2 - 4, 3 - 7

if __name__ == '__main__':
	lst = step1()
	step2(lst)