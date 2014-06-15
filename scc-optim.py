import random
import math
import copy
from time import sleep
from collections import Counter




class Graph(object):

	def __init__(self,dic,reverse):

		self.dic = dic #copy.deepcopy(dic)
		self.reverse = reverse #copy.deepcopy(reverse)
		self.finished = []
		self.visited = {}
		self.leaders = {}

	def n(self):
		return len(self.dic.keys())

	def dfs(self, k, switch):

		stack = []
		if not self.visited[k]:
			stack = [k]
				
		while stack: # we still have there to go
			i = stack[-1]
			self.visited[i] = True

			gph = { True: self.reverse, False: self.dic }

			next_nodes = [ x for x in gph[switch][i] if not self.visited[x] ]

			if not next_nodes:

				if switch:
					self.finished.append(i)
				else:
					self.leaders[i] = k

				stack.pop()

			else:
				next = next_nodes.pop()
				stack.append(next)




	def explore(self):

		self.visited = { x:False for x in self.dic }
		
		for k in range(self.n(),0,-1):
			self.dfs(k,True)

		self.visited = { x:False for x in self.dic }

		while self.finished:
			k = self.finished.pop()
			self.dfs(k,False)


		
filename = "SCC-big.txt"
gdic = {}
grev = {}


with open(filename) as f:

	for line in f:
		tail,head = map(int, line.split())

		if tail not in gdic:
			gdic[tail] = []
		if head not in gdic:
			gdic[head] = []
		if tail not in grev:
			grev[tail] = []
		if head not in grev:
			grev[head] = []

		gdic[tail].append(head)
		grev[head].append(tail)

print "finished reading file"

og = Graph(gdic,grev)

og.explore()


count = Counter(og.leaders.values())
print count.most_common(5)
	 



		


