INPUT_FILE = "../inputs/9.txt"
WINDOW_SIZE = 25

def tryPairSum(lst, num):
	for i in range(WINDOW_SIZE):
		for j in range(i + 1, WINDOW_SIZE):
			if lst[i] + lst[j] == num:
				return True

	return False

def step1():
	curLine = 0
	lst = []

	with open(INPUT_FILE) as f:
		for line in f.readlines():
			if line[-1] is '\n':
				line = line[:-1]
			num = int(line)
			# Circular array logic
			if curLine < WINDOW_SIZE:
				lst.append(num)
			else:
				if tryPairSum(lst, num):
					lst[curLine % WINDOW_SIZE] = num
				else:
					print("Invalid number is " + str(num))
					return num

			curLine += 1

# 166022427 too low
def step2(limit):
	accs = []
	nums = []
	with open(INPUT_FILE) as f:
		for line in f.readlines():
			if line[-1] is '\n':
				line = line[:-1]
			num = int(line)
			nums.append(num)

			for i in range(len(accs)):
				accs[i] += num
				if accs[i] == limit:
					print("Idx is {0}, length is {1}".format(i, len(nums)))
					(down, up) = (min(nums[i:]), max(nums[i:]))
					print("Max is {0}, min is {1}, sum is {2}".format(up, down, up + down))
					return

			accs.append(num)

if __name__ == '__main__':
	num = step1()
	step2(num)