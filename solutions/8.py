INPUT_FILE = "../inputs/8.txt"

# Process input
def bootTheCode(lines):
	curLine = 0
	read = set()
	acc = 0

	while curLine < len(lines):
		if curLine in read:
			return (curLine, acc, read)

		read.add(curLine)
		arr = lines[curLine].split()

		if arr[0] == "acc":
			acc += int(arr[1])
			curLine += 1
		elif arr[0] == "jmp":
			curLine += int(arr[1])
		else:
			curLine += 1

	return (curLine, acc, read)

def step1():
	with open(INPUT_FILE) as f:
		lines = f.readlines()
		print(bootTheCode(lines)[1])

def step2():
	with open(INPUT_FILE) as f:
		lines = f.readlines()

	(_, _, originalRead) = bootTheCode(lines)
	for lineNum in originalRead:
		# Change line
		curLine = lines[lineNum]
		curOp = curLine[:3]
		lines[lineNum] = ("jmp" if curOp == "nop" else "nop") + curLine[3:]
		(curNum, acc, read) = bootTheCode(lines)
		if curNum >= len(lines):
			print(acc)
			return
		lines[lineNum] = curLine

	print("no fix found")


if __name__ == '__main__':
	step1()
	step2()