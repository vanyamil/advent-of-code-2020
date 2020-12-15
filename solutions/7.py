INPUT_FILE = "../inputs/7.txt"
NO_COLOR = "no other"
GOAL_COLOR = "shiny gold"

# This is a dope graph problem
# Build a directed graph, edges from sub-bags to super-bags (inside to outside)
# Then make a spanning tree rooted at "shiny gold" node
# Number of nodes in tree -1 (for the root - really hope this has no cycles and thus infinite bags) is our number for part 1

# Instead of spanning tree, assuming actual graph is acyclic, can probably do a merge-find approach
# But then need it to be "sorted" w.r.t. depth to "shiny gold", or be a directed merge-find (which I've worked on previously!)

class Node:
	def __init__(self, _id, data = None):
		self._id = _id
		self.data = data
		self.edges = set()

class Edge:
	def __init__(self, src, dst, data = None):
		self.src = src
		self.dst = dst
		self.data = data

	@staticmethod
	def make(src, dst, data = None):
		e = Edge(src, dst, data)
		src.edges.add(e)
		return e

class Graph:
	def __init__(self):
		self.nodes = dict()
		self.edges = set()

	def makeNode(self, _id, nodeData = None):
		if _id not in self.nodes:
			node = Node(_id, nodeData)
			self.nodes[_id] = node
		return self.nodes[_id]

	def makeEdge(self, srcNode, dstNode, edgeData = None):
		e = Edge.make(srcNode, dstNode, edgeData)
		self.edges.add(e)
		return e

def dfs(graph, start):
	found = set([start])
	queue = list(start.edges)

	while len(queue) > 0:
		curEdge = queue.pop()
		curNode = curEdge.dst
		found.add(curNode)
		for subEdge in curNode.edges:
			if subEdge.dst not in found:
				queue.append(subEdge)

	return found

# Edge contains true -> edges from superbag to subbag
# Edge contains false -> edges from subbag to superbag
def processFile(f, edge_contains):
	graph = Graph()
	# Add the "root" node
	graph.makeNode(GOAL_COLOR)
	# Read file
	for line in f.readlines():
		# `[color] bags contain (no other bags|1 [color] bag|N [color] bags)(,(no other bags|1 [color] bag|N [color] bags))*
		# Split on ' bag'
		# 0: [color]
		# 1: s contain (no other|N [color])
		# 2+: (s), N [color]
		# last: (s).
		arr = line.split(' bag')
		here_color = arr[0]
		here_node = graph.makeNode(here_color)
		first_entry = arr[1][10:] # skip `s contain `
		if first_entry == NO_COLOR:
			continue

		(num, color) = first_entry.split(' ', 1)
		color_node = graph.makeNode(color)
		if edge_contains:
			graph.makeEdge(here_node, color_node, int(num))
		else:
			graph.makeEdge(color_node, here_node, int(num))

		for idx in range(2, len(arr) - 1):
			entry = arr[idx]
			if entry[0] is 's':
				entry = entry[3:]
			else:
				entry = entry[2:]
			(num, color) = entry.split(' ', 1)
			color_node = graph.makeNode(color)
			if edge_contains:
				graph.makeEdge(here_node, color_node, int(num))
			else:
				graph.makeEdge(color_node, here_node, int(num))

	return graph

def countNumBags(graph, _id):
	# Recursive DFS approach
	_sum = 0
	for edge in graph.nodes[_id].edges:
		num = edge.data
		next_color = edge.dst._id
		_sum += num * (1 + countNumBags(graph, next_color)) # Could benefit from memoization
	return _sum

def step1():
	with open(INPUT_FILE) as f:
		graph = processFile(f, False)

	print("Count: " + str(len(dfs(graph, graph.nodes[GOAL_COLOR])) - 1))
	print("Edge count: " + str(len(graph.edges)))

def step2():
	with open(INPUT_FILE) as f:
		graph = processFile(f, True)

	print("Count: " + str(countNumBags(graph, GOAL_COLOR)))

if __name__ == '__main__':
	step1()
	step2()