INPUT_FILE = "../inputs/1.txt"

def step1():
	with open(INPUT_FILE) as f:
		nums = sorted(map(int, f.readlines()))

	for x in nums:
		if 2020 - x in nums:
			print(x * (2020 - x))
			return

	print("No pair found!")

def step2():
	with open(INPUT_FILE) as f:
		nums = sorted(map(int, f.readlines()))

	for i in range(len(nums)):
		x = nums[i]
		for j in range(i + 1, len(nums)):
			y = nums[j]
			if (2020 - x - y) in nums:
				print(x * y * (2020 - x - y))
				return

	print("No triple found!")

if __name__ == '__main__':
	step1()
	step2()