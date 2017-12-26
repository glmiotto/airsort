import numpy as np

class TrieNode:
	def __init__(self):
		self.start = -1 # -1 doesn't exist, is the byte of oco.csv otherwise
		self.child = np.array([None]*10)
	def getStart(self):
		return self.start
	def setStart(self, info):
		self.start = info
	def getChild(self, index):
		return self.child[index]
	def setChild(self, index, node):
		self.child[index] = node
	def print(self):
		print(self.child)

class Trie:
	def __init__(self):
		self.root = TrieNode()
	def addKey(self, data, info):
		curNode = self.root
		for letter in data:
			number = int(letter)
			newNode = curNode.getChild(number)
			if(newNode == None):
				newNode = TrieNode()
				curNode.setChild(number, newNode)
			curNode = newNode
		curNode.setStart(info)
	def findKey(self, data): # full ID
		curNode = self.root
		for letter in data:
			number = int(letter)
			curNode = curNode.getChild(number)
			if(curNode == None):
				print('Not Found!\n')
				return -1
		return curNode.start
	def filterIDRec(self, curNode, IDs, ID):
		if curNode != None:
			if curNode.start != -1:
				IDs.add(ID)
			for i in range(10):
				self.filterIDRec(curNode.getChild(i), IDs, ID + str(i))
	def filterID(self, data):
		curNode = self.root
		for letter in data:
			number = int(letter)
			curNode = curNode.getChild(number)
			if(curNode == None):
				return set()
		IDs = set()
		self.filterIDRec(curNode, IDs, data)
		return IDs
	def clearRec(self, curNode):
		if curNode != None:
			for i in range(10):
				self.clearRec(curNode.getChild(i))
			curNode.setStart(-1)
			del curNode
	def clear(self):
		self.clearRec(self.root)
	
Tree = Trie()
with open('oco.csv', 'r') as f:
	l = f.readline()
	while True:
		byte = f.tell()
		ID = f.readline().split('~')[0].strip('"')
		if(ID == ''):
			break
		ID = ID
		Tree.addKey(ID, byte)


	
	
	
	
	
	
	
	
	
	
		
		
		