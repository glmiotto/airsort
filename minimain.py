import filesCreation
import Trie
import supportFile
import pickle


def sortedIDs(treeFile):
	Tree = Trie.Trie(2000)
	Tree.inOrder(treeFile)
	
def sortedData(dicFile):
	supportFile.showSorted(dicFile)

def showRank(dicFile):
	supportFile.getTop(dicFile)
	
def getInfoID(ID, treeFile):
	Tree = Trie.Trie(2000)
	a = Tree.findID(ID, treeFile)
	if(a == -1):
		return -1
	b = []
	with open('oco.bin', 'rb') as f:
		size = pickle.load(f)
		f.seek(a.getOco()*size)
		b.append(pickle.load(f))
	with open('anv.bin', 'rb') as f:
		size = pickle.load(f)
		for anv in a.getAnv():
			f.seek(anv*size)
			b.append(pickle.load(f))
	return b
	
#ocoList no mesmo formato, anvList será uma lista de listas (pode ter + de um ID), ambos devem ter o mesmo ID
def addData(ocoList, anvList, treeFile):
	Tree = Trie.Trie(2000)
	pos = supportFile.addInMainFile(ocoList, 'oco.bin')
	Tree.addID(ocoList[0], pos, treeFile)
	for anv in anvList:
		pos = supportFile.addInMainFile(anv, 'anv.bin')
		Tree.updateID(anv[0], None, pos, None, treeFile, 0) # append
	l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin', 'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin', 'fatalities.bin']
	l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
	l3 = [1, 2, 5, 6, 8, 10, 12, 3, 4, 5, 8, 10, 21, 22]
	for i in range(7):
		supportFile.addID(l2[i], l1[i], ocoList[l3[i]], ocoList[0])
	for anv in anvList:
		for i in range(7, len(l1)):
			supportFile.addID(l2[i], l1[i], anv[l3[i]], anv[0])
			
def updateOco(ID, ocoList, treeFile):
	Tree = Trie.Trie(2000)
	a = Tree.findID(ID, treeFile)
	if(a == -1):
		return -1
	d = []
	with open('oco.bin', 'rb') as f:
		size = pickle.load(f)
		f.seek(a.getOco()*size)
		d = pickle.load(f)
		f.seek(a.getOco()*size)
		pickle.dump(ocoList, f)
	l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin']
	l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicInvStatus.bin']
	l3 = [1, 2, 5, 6, 8, 10, 12]
	for i in range(l1):
		if l[l3[i]] != ocoList[l3[i]]:
			supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)
			supportFile.addID(l2[i], l1[i], ocoList[l3[i]], ID)
	
def removeData(ID, treeFile):
	Tree = Trie.Trie(2000)
	a = Tree.findID(ID, treeFile)
	if(a == -1):
		return -1
	Tree.removeID(ID, treeFile)
	d = []
	last = 0
	with open('oco.bin', 'rb') as f:
		size = pickle.load(f)
		f.seek(a.getOco()*size)
		d = pickle.load(f)
		f.seek(-size, 2)
		last = f.tell()//size
	print(a.getOco())
	toUpdate = supportFile.removeInMainFile(a.getOco(), 'oco.bin')
	print(toUpdate == str(toUpdate))
	print(toUpdate)
	b = Tree.findID(toUpdate, 'Trie.bin')
	print(b)
	Tree.updateID(toUpdate, None, a.getOco(), last, treeFile, 2) # update oco position
	b = Tree.findID(toUpdate, 'Trie.bin')
	print(b)
	l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin']
	l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicInvStatus.bin']
	l3 = [1, 2, 5, 6, 8, 10, 12]
	for i in range(len(l1)):
		supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)
	for anv in a.getAnv():
		d = []
		last = 0
		with open('anv.bin', 'rb') as f:
			size = pickle.load(f)
			f.seek(anv*size)
			d = pickle.load(f)
			f.seek(-size, 2)
			last = f.tell()//size
		toUpdate = supportFile.removeInMainFile(anv, 'anv.bin')
		Tree.updateID(toUpdate, None, anv, last, treeFile, 2) # change anv
		l1 = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin', 'fatalities.bin']
		l2 = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
		l3 = [3, 4, 5, 8, 10, 21, 22]
		for i in range (len(l1)):
			supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)

filesCreation.createFiles()
Trie.buildTrie()

'''
a = getInfoID('201106206058374', 'Trie.bin')
#print(a)
removeData('201106206058374', 'Trie.bin')
b = getInfoID('201106206058374', 'Trie.bin')
#print(b)

b = a[1:]
a = a[0]
		
l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin', 'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin', 'fatalities.bin']
l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
l3 = [1, 2, 5, 6, 8, 10, 12, 3, 4, 5, 8, 10, 21, 22]

for i in range(len(l1)):
	#print(i)
	if i < 7:
		if '201106206058374' in supportFile.getIDs(l2[i], l1[i], a[l3[i]]):
			print('Erro')
	else:
		if '201106206058374' in supportFile.getIDs(l2[i], l1[i], b[0][l3[i]]):
			print('Erro')'''