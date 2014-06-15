import random
import math
import copy
from time import sleep
from collections import Counter




class Graph(object):

	def __init__(self,dic,reverse):
		self.dic = copy.deepcopy(dic)
		self.reverse = copy.deepcopy(reverse)
		self.finished = []
#		self.visited = []
		self.leaders = {}

	def n(self):
		return len(self.dic.keys())

	def dfs(self, k):

		stack = [k]
		
		while stack: # we still have there to go
			i = stack[-1]
#			print "i=",i,'stack=',stack

			next_nodes = [ x for x in self.reverse[i] if x not in stack if x not in self.finished ]

			if not next_nodes:
				self.finished.append(i)
				stack.pop()

			else:
				next = next_nodes.pop()
				stack.append(next)



	def explore(self):
		for k in range(self.n(),0,-1):
			print k
			if k not in self.finished:
				self.dfs(k)
			else:
				print "in finished"

	def dfs_ii(self,k):
		stack = [k]
		
		while stack: # we still have there to go
			i = stack[-1]
#			print "i=",i,'stack=',stack

			next_nodes = [ x for x in self.dic[i] if x not in stack if x not in self.leaders ]

			if not next_nodes:
				self.leaders[i] = k
				stack.pop()

			else:
				next = next_nodes.pop()
				stack.append(next)


	def explore_ii(self):
#		for k in self.finished[::-1]:
#			if k not in self.leaders:
#				self.dfs_ii(k)
		while self.finished:
			k = self.finished.pop()
			if k not in self.leaders:
				self.dfs_ii(k)




		
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

#gdic, grev = grev, gdic # we used reversed graph as input
og = Graph(gdic,grev)
#og = Graph(grev,gdic)

og.explore()
og.explore_ii()



#print [ll.index(i)+1 for i in range(1,10)]


count = Counter(og.leaders.values())
print count.most_common(5)
	 



		


