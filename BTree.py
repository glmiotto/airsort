# B-Tree implementation without remove
import numpy as np

class BNode:
	def __init__(self, t, isLeaf): # t is the minimum number of keys in one node
		self.key = np.array([None]*2*t)
		self.child = np.array([None]*(2*t+1))
		self.size = 0
		self.isLeaf = isLeaf
	def getKey(self, index):
		return self.key[index]
	def addKey(self, index, data):
		for i in range(self.size-1, index-1, -1):
			self.key[i+1] = self.key[i]
		self.key[index] = data
		self.size += 1
	def setKey(self, index, data):
		self.key[index] = data
	def getChild(self, index):
		return self.child[index]
	def setChild(self, index, child):
		self.child[index] = child
	def getSize(self):
		return self.size
	def setSize(self, size):
		self.size = size
	def nodeIsLeaf(self):
		return self.isLeaf
	def setNotLeaf(self):
		self.isLeaf = False
	def print(self):
		print("Keys:", self.key, self.size)
		print("Children:", self.child)
		
		
class BTree:
	def __init__(self, t):
		self.root = BNode(t, True)
		self.t = t
	#addKey recursively guided by return value, if first tuple's return value is True, then the
	#parent needs to add the mid value in the node
	def addKeyRec(self, prevNode, node, data):
		if(node.nodeIsLeaf()):
			size = node.getSize()
			if(size < 2*self.t):
				index = 0
				while(index < size and data > node.getKey(index)):
					index += 1
				node.addKey(index, data)
				return (False, 0, None)
			else:
				lowMid = self.t-1
				highMid = self.t
				midNumber = data
				if(data < node.getKey(lowMid)):
					midNumber = node.getKey(lowMid)
					index = self.t-2
					while(index >= 0 and data < node.getKey(index)):
						node.setKey(index+1, node.getKey(index))
						index -= 1
					node.setKey(index+1, data)
				elif(data > node.getKey(highMid)):
					midNumber = node.getKey(highMid)
					index = self.t+1
					while(index < 2*self.t and data > node.getKey(index)):
						node.setKey(index-1, node.getKey(index))
						index += 1
					node.setKey(index-1, data)
				rightNode = BNode(self.t, node.nodeIsLeaf())
				for i in range(self.t, 2*self.t):
					rightNode.addKey(i-self.t, node.getKey(i))
					node.setKey(i, None)
				if prevNode == None:
					newRoot = BNode(self.t, False)
					self.root = newRoot
					newRoot.addKey(0, midNumber)
					newRoot.setChild(0, node)
					newRoot.setChild(1, rightNode)
				node.setSize(self.t)
				return (True, midNumber, rightNode)
		else:
			backRec = None
			size = node.getSize()
			index = 0
			if(data > node.getKey(size-1)):
				backRec = self.addKeyRec(node, node.getChild(size), data)
				index = size
			else:
				while(index < size and data > node.getKey(index)):
					index += 1
				backRec = self.addKeyRec(node, node.getChild(index), data)
			if(backRec[0]):
				keyToAdd = backRec[1]
				if(size < 2*self.t):
					if(index == size):
						node.addKey(size, keyToAdd)
						node.setChild(size+1, backRec[2])
					else:
						for i in range(size, index, -1):
							node.setChild(i+1, node.getChild(i))
						node.setChild(index+1, backRec[2])
						node.addKey(index, keyToAdd)
					return(False, 0, None)
				else:
					rightNode = BNode(self.t, node.nodeIsLeaf())
					midNumber = keyToAdd
					if(index < self.t):
						midNumber = node.getKey(self.t-1)
						for i in range(self.t, 2*self.t+1):
							rightNode.setChild(i-self.t, node.getChild(i))
							node.setChild(i, None)
						for i in range(self.t-1, index, -1):
							node.setKey(i, node.getKey(i-1))
							node.setChild(i+1, node.getChild(i))
						node.setChild(index+1, backRec[2])
						node.setKey(index, keyToAdd)
					elif(index > self.t):
						midNumber = node.getKey(self.t)
						rightNode.setChild(index-self.t, backRec[2])
						childIndex = self.t+1
						for i in range(0, self.t+1):
							if(rightNode.getChild(i) == None):
								rightNode.setChild(i, node.getChild(childIndex))
								node.setChild(childIndex, None)
								childIndex += 1
						for i in range(self.t, index-1):
							node.setKey(i, node.getKey(i+1))
						if index == 2*self.t:
							index -= 1
						node.setKey(index, keyToAdd)
					else:
						rightNode.setChild(0, backRec[2])
						for i in range(self.t+1, 2*self.t+1):
							rightNode.setChild(i-self.t, node.getChild(i))
							node.setChild(i, None)
					for i in range(self.t, 2*self.t):
						rightNode.addKey(i-self.t, node.getKey(i))
						node.setKey(i, None)
					if prevNode == None:
						newRoot = BNode(self.t, False)
						self.root = newRoot
						newRoot.addKey(0, midNumber)
						newRoot.setChild(0, node)
						newRoot.setChild(1, rightNode)
					node.setSize(self.t)
					return (True, midNumber, rightNode)
			else:
				return(False, 0, None)
	def addKey(self, data):
		self.addKeyRec(None, self.root, data) # function that adds key recursively, starting from root
	def inOrderRec(self, node): #in order traversal, like BST
		if(node.nodeIsLeaf()):
			for i in range(node.getSize()):
				print(node.getKey(i), end=' ')
		else:
			for i in range(node.getSize()):
				self.inOrderRec(node.getChild(i))
				print(node.getKey(i), end=' ')
			self.inOrderRec(node.getChild(node.getSize()))
	def inOrder(self):
		self.inOrderRec(self.root)
		print()
	def findRec(self, node, data): #find a value in B-Tree
		if(node.nodeIsLeaf()):
			for i in range(0, node.getSize()):
				if(node.getKey(i) == data):
					return True
			return False
		else:
			if(data > node.getKey(node.getSize()-1)):
				return self.findRec(node.getChild(node.getSize()), data)
			else:
				for i in range(node.getSize()):
					if(data < node.getKey(i)):
						return self.findRec(node.getChild(i), data)
					elif(data == node.getKey(i)):
						return True
	def find(self, data):
		return self.findRec(self.root, data)

tree = BTree(2)
tree.addKey(5)
tree.addKey(3)
tree.addKey(8)
tree.addKey(6)
tree.addKey(15)
tree.addKey(50)
tree.addKey(25)
tree.addKey(23)
tree.addKey(13)
tree.addKey(24)
tree.addKey(28)
tree.addKey(7)
tree.addKey(12)
tree.addKey(70)
tree.addKey(100)
tree.addKey(150)
tree.addKey(80)
tree.addKey(51)
tree.addKey(9)
tree.addKey(10)
tree.addKey(11)

tree.inOrder()

print(tree.find(85))


			