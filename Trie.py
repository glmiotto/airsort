import numpy as np
import pickle
import math

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
		self.numByteLength = None # Number of bytes of the pointer to root in disk
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
				print('Not Found!')
				return -1
		return curNode.getStart()
	def filterIDRec(self, curNode, IDs, ID):
		if curNode != None:
			if curNode.getStart() != -1:
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
	def saveTrieRec(self, curNode, f):
		if(curNode == None):
			return None
		for i in range(0, 10):
			byte = self.saveTrieRec(curNode.getChild(i), f)
			curNode.setChild(i, byte)
		nodeByte = f.tell()
		pickle.dump(curNode, f)
		return nodeByte
	def saveTrie(self, outDir):  # Save Trie in disk
		with open(outDir, 'wb') as f:
			rootStart = self.saveTrieRec(self.root, f)
			f.write(rootStart.to_bytes(math.ceil(rootStart.bit_length()/8), 'little'))
			self.numByteLength = math.ceil(rootStart.bit_length()/8)
			f.write(self.numByteLength.to_bytes(1, 'little')) # Max of 1 byte (0 - 255)
	def traverseTrie(self, data, file):  # Traverse a Trie saved in a file
		with open(file, 'rb') as f:
			f.seek(-1, 2)
			self.numByteLength = int.from_bytes(f.read(), 'little')
			f.seek(-1-self.numByteLength, 2)
			rootStart = int.from_bytes(f.read(self.numByteLength), 'little')
			f.seek(rootStart)
			curNode = pickle.load(f)
			for letter in data:
				number = int(letter)
				curNode = curNode.getChild(number)
				if curNode == None:
					print('Not Found')
					return -1
				f.seek(curNode)
				curNode = pickle.load(f)
			return curNode.getStart()
	def filterIDTrieRec(self, curNode, IDs, ID, f): 
		if curNode != None:
			if curNode.getStart() != -1:
				IDs.add(ID)
			for i in range(10):
				nextNode = curNode.getChild(i)
				if nextNode == None:
					continue
				f.seek(nextNode)
				nextNode = pickle.load(f)
				self.filterIDTrieRec(nextNode, IDs, ID + str(i), f)
	def filterIDTrie(self, data, file): # filter ID traversing Trie in a file
		with open(file, 'rb') as f:
			f.seek(-1, 2)
			self.numByteLength = int.from_bytes(f.read(), 'little')
			f.seek(-1-self.numByteLength, 2)
			rootStart = int.from_bytes(f.read(self.numByteLength), 'little')
			f.seek(rootStart)
			curNode = pickle.load(f)
			for letter in data:
				number = int(letter)
				curNode = curNode.getChild(number)
				if curNode == None:
					return set()
				f.seek(curNode)
				curNode = pickle.load(f)
			IDs = set()
			self.filterIDTrieRec(curNode, IDs, data, f)
			return IDs
# build Trie
'''	
Tree = Trie()
with open('oco.csv', 'r') as f:
	l = f.readline()
	while True:
		byte = f.tell()
		ID = f.readline().split('~')[0].strip('"')
		if(ID == ''):
			break
		Tree.addKey(ID, byte)

# get more information of this ID		
		
a = Tree.findKey('201208318138992')
		
with open('oco.csv', 'r') as f:
	f.seek(a)
	b = f.readline()
	print(b)

	
Tree.saveTrie('Trie.bin')


a = Tree.traverseTrie('201208318138992', 'Trie.bin')

with open('oco.csv', 'r') as f:
	f.seek(a)
	b = f.readline()
	print(b)


a = Tree.filterIDTrie('2012', 'Trie.bin')

print(a)
	
'''	
		
		
		