import pickle
import math
import os.path

class TrieNode:
	def __init__(self):
		self.oco = -1 # posição em oco.bin, é -1 caso não exista
		self.anv = [] # listas das posições em oco.bin, é vazia caso não exista
		self.parent = [-1, -1] # pointer to parent (in disk)
		self.child = [None]*10
	def getOco(self):
		return self.oco
	def setOco(self, info):
		self.oco = info
	def getAnv(self):
		return self.anv
	def appendAnv(self, info):
		self.anv.append(info)
	def removeAnv(self, anv):
		self.anv.remove(anv)
	def updateAnv(self, anv, oldAnv):
		self.anv[self.anv.index(oldAnv)] = anv
	def getParent(self):
		return self.parent
	def setParent(self, a, b):
		self.parent[0] = a
		self.parent[1] = b
	def getChild(self, index):
		return self.child[index]
	def setChild(self, index, node):
		self.child[index] = node
	def print(self):
		print('OcoID:', self.oco)
		print('Anv: ', end='')
		for i in self.anv:
			print(i, end=' ')
		print()
		print(self.child)
		print(self.parent)
		
class Trie:
	def __init__(self, blockSize):
		self.root = TrieNode()
		self.blockSize = blockSize
	def addID(self, ID, oco, file):
		try:
			if not os.path.isfile(file): # create Trie (blocksize and root)
				with open(file, 'wb') as f:
					bytesToAdd = self.blockSize - len(pickle.dumps(self.blockSize))
					pickle.dump(self.blockSize, f)
					f.write(bytearray(bytesToAdd))
					bytesToAdd = self.blockSize - len(pickle.dumps(self.root))
					pickle.dump(self.root, f) # raiz é o primeiro, depois do tamanho de cada bloco
					f.write(bytearray(bytesToAdd))
			with open(file, 'r+b') as f:
				size = pickle.load(f)
				pos = 1
				f.seek(pos*size)
				curNode = pickle.load(f) # root
				for letter in ID:
					number = int(letter)
					childPos = curNode.getChild(number) 
					if childPos != None:
						f.seek(childPos*size)
						curNode = pickle.load(f)
						pos = childPos
					else: # adicionar novo caminho
						f.seek(0, 2)
						newPos = f.tell()//size # new node's position in file
						new = TrieNode()
						new.setParent(pos, number)
						bytesToAdd = size - len(pickle.dumps(new))
						pickle.dump(new, f)
						f.write(bytearray(bytesToAdd))
						f.seek(pos*size)
						curNode.setChild(number, newPos)
						pickle.dump(curNode, f)
						curNode = new
						pos = newPos
				f.seek(pos*size)
				curNode.setOco(oco)
				pickle.dump(curNode, f)
		except:
			return -1
	# se não desejar atualizar oco, coloque None
	# infoAnv faz coisas diferentes com anv:
	# 0 - append anv na lista, se não estiver na lista
	# 1 - remove anv da lista, se houver
	# 2 - troca oldAnv por anv, se oldAnv já existir
	def updateID(self, ID, oco, anv, oldAnv, file, infoAnv):
		try:
			with open(file, 'r+b') as f:
				size = pickle.load(f)
				pos = 1
				f.seek(pos*size)
				curNode = pickle.load(f) # root
				for letter in ID:
					number = int(letter)
					childPos = curNode.getChild(number)
					if childPos == None: # ID doesn't exists
						return -1
					f.seek(childPos*size)
					curNode = pickle.load(f)
					pos = childPos
				f.seek(pos*size)
				if(oco != None):
					curNode.setOco(oco)
				if infoAnv == 0:
					if anv not in curNode.getAnv():
						curNode.appendAnv(anv)
				elif infoAnv== 1:
					if anv in curNode.getAnv():
						curNode.removeAnv(anv)
				else:
					if oldAnv in curNode.getAnv():
						curNode.updateAnv(anv, oldAnv)
				pickle.dump(curNode, f)
		except:
			return -1
		
	def findID(self, ID, file):  # Traverse a Trie saved in a file
		try:
			with open(file, 'rb') as f:
				size = pickle.load(f)
				pos = 1
				f.seek(pos*size)
				curNode = pickle.load(f) # root
				for letter in ID:
					number = int(letter)
					childPos = curNode.getChild(number) 
					if childPos == None:
						return -1
					f.seek(childPos*size)
					curNode = pickle.load(f)
					pos = childPos
				if(curNode.getOco() != -1):
					return curNode
				else:
					return -1
		except:
			return -1
			
	def filterIDRec(self, curNode, IDs, ID, f, size): 
		if curNode != None:
			if curNode.getOco() != -1:
				IDs.add(ID)
			for i in range(10):
				childNode = curNode.getChild(i)
				if childNode == None:
					continue
				f.seek(childNode*size)
				nextNode = pickle.load(f)
				self.filterIDRec(nextNode, IDs, ID + str(i), f, size)
				
	def filterID(self, ID, file): # filter ID traversing Trie in a file
		try:
			with open(file, 'rb') as f:
				size = pickle.load(f)
				f.seek(1*size)
				curNode = pickle.load(f) # root
				for letter in ID:
					number = int(letter)
					childPos = curNode.getChild(number)
					if childPos == None:
						return set()
					f.seek(childPos*size)
					curNode = pickle.load(f)
				IDs = set()
				self.filterIDRec(curNode, IDs, ID, f, size)
				return IDs
		except:
			return set()
	def removeID(self, ID, file): # Melhor verificar se existe antes de remover
		try:
			nodeToRemove = -1
			with open(file, 'r+b') as f:
				size = pickle.load(f)
				pos = 1
				f.seek(pos*size)
				curNode = pickle.load(f) # root
				for letter in ID:
					number = int(letter)
					childPos = curNode.getChild(number) 
					if childPos == None:
						return -1
					f.seek(childPos*size)
					curNode = pickle.load(f)
					pos = childPos
				if(curNode.getOco() == -1): # se ID não existe
					return -1
				nodeToRemove = curNode
				while True:
					for i in range(10):
						if curNode.getChild(i) != None:
							break
					# remove the current node(sem outro caminho)
					parentInfo = curNode.getParent()
					if parentInfo[0] == -1: #Can't delete root
						break
					f.seek(parentInfo[0]*size)
					parent = pickle.load(f)
					f.seek(parentInfo[0]*size)
					parent.setChild(parentInfo[1], None)
					pickle.dump(parent, f)
					curNode = parent
					f.seek(-size, 2) # colocar o último na posição do que foi removido
					last = pickle.load(f)
					f.seek(-size, 2)
					f.truncate()
					f.seek(size*pos) # posição para colocar o que era o último
					pickle.dump(last, f)
					parentInfo = last.getParent()
					f.seek(parentInfo[0]*size)
					parent = pickle.load(f)
					f.seek(parentInfo[0]*size)
					parent.setChild(parentInfo[1], pos)
					pickle.dump(parent, f)
				return nodeToRemove
		except:
			return -1
				
				

def buildTrie():
	Tree = Trie(2000)
	try:
		with open('oco.bin', 'rb') as f:
			size = pickle.load(f)
			i = 1
			while True:
				f.seek(size*i)
				data = pickle.load(f)
				Tree.addID(data[0], i, 'Trie.bin')
				i += 1
	except:
		None
	try:
		with open('anv.bin', 'rb') as f:
			size = pickle.load(f)
			i = 1
			while True:
				f.seek(size*i)
				data = pickle.load(f)
				Tree.updateID(data[0], None, i, None, 'Trie.bin', 0) # append method
				a = Tree.findID(data[0], 'Trie.bin')
				i += 1
	except:
		None

Tree = Trie(2000)

buildTrie()
'''
print(len(Tree.filterID('2009', 'Trie.bin')))

a = Tree.removeID('200908213725671', 'Trie.bin')
a.print()

print(Tree.findID('200908213725671', 'Trie.bin'))

print(len(Tree.filterID('2009', 'Trie.bin')))
'''
