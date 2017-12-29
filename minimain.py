import filesCreation
import Trie
import supportFile
import pickle
import copy


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

def readNewData(treeFile):
	Tree = Trie.Trie(2000)
	Data = []
	info = []
	with open('infoOco.bin', 'rb') as f:
		info = pickle.load(f)
	ID = input('Insira o ID: ')
	a = 0
	if ID.isdigit():
		a = Tree.findID(ID, treeFile)
	while not ID.isdigit() or a != -1:
		print('Invalid ID')
		ID = input('Insira o ID: ')
	ocoList.append(ID)
	d = {2 : 'INDETERMINADA', 5 : 'NÃO IDENTIFICADA', 6 : '***', 8 : '****'}
	for i in range(1, len(info)):
		print(info[i])
		ans = input('1 - Dado conhecido\n2 - Dado desconhecido')
		while not ans.isdigit() and int(ans) < 1 or int(ans) > 2:
			ans = input('1 - Dado conhecido\n2 - Dado desconhecido\nSua Resposta: ')
		if(ans == '2'):
			if i in d.keys():
				ocoList.append(d[i])
			else:
				ocoList.append('***')
		else:
			ans = input('Insira seu dado: ')
			ocoList.append(ans)
	d2 = {3 : 'INDETERMINADA', 4 : '***', 5 : '***', 8 : '***', 10 : '***', 21 : 'INDETERMINADO'}
	anvList = []
	while True:
		ans = input('0 - Sair\n1 - Inserir Aeronave\nSua Resposta: ')
		while not ans.isdigit() and int(ans) < 0 or int(ans) > 1:
			ans = input('0 - Sair\n1 - Inserir Aeronave\nSua Resposta: ')
		if ans == 0:
			if len(anvList == 0):
				anvList.append([])
				break
		else:
			lis = []
			infoAnv = []
			with open('infoAnv.bin', 'rb') as f:
				infoAnv = pickle.load(f)
			lis[0].append(ID)
			for i in range(1, len(infoAnv)):
				print(infoAnv[i])
				ans = input('1 - Dado conhecido\n2 - Dado desconhecido')
				while not ans.isdigit() and int(ans) < 1 or int(ans) > 2:
					ans = input('1 - Dado conhecido\n2 - Dado desconhecido\nSua Resposta: ')
				if(ans == '2'):
					if i in d2.keys():
						lis.append(d2[i])
					else:
						lis.append('***')
				else:
					ans = input('Insira seu dado: ')
					lis.append(ans)
			anvList.append(lis)
	return [ocoList, anvList]
	
		
#ocoList no mesmo formato, anvList será uma lista de listas (pode ter + de um ID), ambos devem ter o mesmo ID
def addData(ocoList, anvList, treeFile):
	Tree = Trie.Trie(2000)
	a = Tree.findID(ocoList[0], treeFile)
	if(a != -1) # can't add an existing ID
		return -1
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
			
def updateList(l, infoFile):
	info = []
	s = copy.deepcopy(l)
	with open(infoFile, 'rb') as f:
		info = pickle.load(f)
	while True:
		print('0 - Sair')
		for i in range(1, len(info)):
			print('{} - {}'.format(i, info[i]))
		ans = input('Deseja alterar qual informação? Digite o número correspondente: ')
		while not ans.isdigit() and (int(ans) < 0 or int(ans) > len(info)):
			ans = input('Deseja alterar qual informação? Digite o número correspondente: ')
		if ans == '0':
			break
		newData = input('Digite o dado corrigido: ')
		s[int(ans)] = newData
	return s
	
def updateOco(ID, treeFile):
	Tree = Trie.Trie(2000)
	a = Tree.findID(ID, treeFile)
	if(a == -1):
		return -1
	d = []
	ocoList = []
	with open('oco.bin', 'r+b') as f:
		size = pickle.load(f)
		f.seek(a.getOco()*size)
		d = pickle.load(f)
		ocoList = updateList(d, 'infoOco.bin')
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
	toUpdate = supportFile.removeInMainFile(a.getOco(), 'oco.bin') # ID to update position
	Tree.updateID(toUpdate, a.getOco(), None, None, treeFile, 0) # update oco position
	l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin']
	l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicInvStatus.bin']
	l3 = [1, 2, 5, 6, 8, 10, 12]
	for i in range(len(l1)):
		supportFile.removeID(l2[i], l1[i], d[l3[i]], ID) # remove in Posting List
	for anv in a.getAnv(): # For each anv
		d = []
		last = 0
		with open('anv.bin', 'rb') as f:
			size = pickle.load(f)
			f.seek(anv*size)
			d = pickle.load(f)
			f.seek(-size, 2)
			last = f.tell()//size
		toUpdate = supportFile.removeInMainFile(anv, 'anv.bin') # ID to update Position
		Tree.updateID(toUpdate, None, anv, last, treeFile, 2) # change anv
		l1 = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin', 'fatalities.bin']
		l2 = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
		l3 = [3, 4, 5, 8, 10, 21, 22]
		for i in range (len(l1)):
			supportFile.removeID(l2[i], l1[i], d[l3[i]], ID) # remove in Posting List
			
			
def updateAnv(ID, registry, treeFile):
	Tree = Trie.Trie(2000)
	a = Tree.findID(ID, treeFile)
	if (a == -1):
		return -1
	with open('anv.bin', 'r+b') as f:
		size = pickle.load(f)
		for anv in a.getAnv():
			f.seek(anv*size)
			d = pickle.load(f)
			if d[1] == registry:
				f.seek(anv*size)
				s = updateList(d, 'infoAnv.bin')
				pickle.dump(s, f)
				if(s[0] != d[0]):
					return -1 # ID must be the same
				l1 = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin', 'fatalities.bin']
				l2 = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
				l3 = [3, 4, 5, 8, 10, 21, 22]
				for i in range (len(l1)):
					if(s[l3[i]] != d[l3[i]]): # if they are different
						# update PostingList
						supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)
						supportFile.addID(l2[i], l1[i], s[l3[i]], ID)
				break

#filesCreation.createFiles()
#Trie.buildTrie()


updateAnvList(['2151616465464'])

'''a = getInfoID('201106206058374', 'Trie.bin')
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
	if i < 7:
		if '201106206058374' in supportFile.getIDs(l2[i], l1[i], a[l3[i]]):
			print('Erro')
	else:
		if '201106206058374' in supportFile.getIDs(l2[i], l1[i], b[0][l3[i]]):
			print('Erro')'''