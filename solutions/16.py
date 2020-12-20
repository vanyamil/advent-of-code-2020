INPUT_FILE = "../inputs/16.txt"

def process(f):
	# Rules
	rules = {}
	while True:
		line = f.readline()[:-1]
		if line is '':
			break
		
		nameIdx = line.find(':')
		orIdx = line.find(' or ', nameIdx)

		name = line[:nameIdx]
		range1 = tuple(map(int, line[nameIdx+2:orIdx].split('-')))
		range2 = tuple(map(int, line[orIdx+4:].split('-')))
		rules[name] = (range1, range2)

	# Your ticket
	f.readline()
	yourTicket = list(map(int, f.readline()[:-1].split(',')))

	# Next tickets
	f.readline()
	f.readline()
	tickets = list(map(lambda x: list(map(int, x.split(','))), f.readlines()))

	return rules, yourTicket, tickets

def step1(rules, yourTicket, tickets):
	_sum = 0

	for ticket in tickets:
		for number in ticket:
			bad = True
			for rule in rules.values():
				if number >= rule[0][0] and number <= rule[0][1] or number >= rule[1][0] and number <= rule[1][1]:
					bad = False
					break
			if bad:
				_sum += number

	print("Step 1: {0}".format(_sum))

def step2(rules, yourTicket, tickets):
	valids = []
	n = len(rules)

	# Select valids only
	for ticket in tickets:
		badTicket = False
		for number in ticket:
			bad = True
			for rule in rules.values():
				if number >= rule[0][0] and number <= rule[0][1] or number >= rule[1][0] and number <= rule[1][1]:
					bad = False
					break
			if bad:
				badTicket = True
				break

		if not badTicket:
			valids.append(ticket)

	# For each column:
	for col in range(n):
		possibleSet = set(rules.keys())
		notAllowed = set()
		# How does this ticket restrict it
		for ticket in valids:
			fieldValue = ticket[col]
			for ruleName in possibleSet:
				# Skip already confirmed bad
				if ruleName in notAllowed:
					continue
				# Check if this is bad
				if fieldValue < rules[ruleName][0][0] or fieldValue > rules[ruleName][1][1] or fieldValue > rules[ruleName][0][1] and fieldValue < rules[ruleName][1][0]:
					notAllowed.add(ruleName)
					# print("Adding " + ruleName + " as bad")

			# Check if we reached limit
			if len(notAllowed) is n - 1:
				break

		if len(notAllowed) is not n-1:
			print("Possible rules: ({0}) ".format(n - len(notAllowed)) + ",".join(possibleSet - notAllowed))
		else:
			print("Only possible rule is '{0}'".format(list(possibleSet - notAllowed)[0]))

	# Manually evaluated here
	print(yourTicket[2] * yourTicket[4] * yourTicket[7] * yourTicket[11] * yourTicket[14] * yourTicket[16])


if __name__ == '__main__':
	with open(INPUT_FILE) as f:
		(rules, yourTicket, tickets) = process(f)

	step1(rules, yourTicket, tickets)
	step2(rules, yourTicket, tickets)