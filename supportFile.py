import pickle
import copy
import locale
# this reads the environment and inits the right locale
locale.setlocale(locale.LC_ALL, "")

# função auxiliar para imprimir todo o arquivo
def printall(file):
	a = 0
	try:
		with open(file, 'rb') as f:
			size = pickle.load(f)
			i = 1
			while True:
				f.seek(i*size)
				l = pickle.load(f)
				print(i, l)
				i += 1
	except:
		return

# coloca todos dados do dicionário, ordena em ordem crescente e imprime
def showSorted(dicFile):
	try:
		l = []
		with open(dicFile, 'rb') as dic:
			size = pickle.load(dic)
			i = 1
			while True:
				dic.seek(i*size)
				d = pickle.load(dic)
				l.append(d[0])
				i += 1
	except:
		l.sort(key=locale.strxfrm)
		for item in l:
			print(item)
		return

# coloca todos dados do dicionário, ordena em ordem crescente e retorna a lista
def returnSorted(dicFile):
	try:
		l = []
		with open(dicFile, 'rb') as dic:
			size = pickle.load(dic)
			i = 1
			while True:
				dic.seek(i*size)
				d = pickle.load(dic)
				l.append(d[0])
				i += 1
	except:
		l.sort(key=locale.strxfrm)

		return l

# Pega o Top 10 em % do dicionário(usando o 3 campo que é o tamanho de cada um)
def getTop(dicFile):
	try:
		with open(dicFile, 'rb') as dic:
			data = []
			size = pickle.load(dic)
			i = 1
			qty = 0
			while True:
				dic.seek(size*i)
				l = pickle.load(dic)
				data.append([int(l[2]), l[0]])
				qty += int(l[2])
				i += 1
	except:
		if(len(data) > 0):
			data.sort(reverse=True)
			for i in range(min(10, len(data))):
				if data[i][1] == '***':
					data[i][1] = 'INDETERMINAÇÃO'
				print('{:>30} = {:5.2f}%'.format(data[i][1], data[i][0]/qty*100))
		else:
			print('Arquivo sem dado')

# Pega todos ID's que pertencem ao dado
def getIDs(dicFile, dataFile, data):
	try:	
		with open(dicFile, 'rb') as dic:
			with open(dataFile, 'rb') as f:
				size = pickle.load(dic)
				fsize = pickle.load(f)
				IDs = set()
				dic.seek(-size, 2) # ler último bloco
				neutralValue = pickle.load(dic)
				if(neutralValue != -1): # aqui pega os índices que são deconhecidos (potencialmente está incluso no dado)
					dic.seek(neutralValue*size)
					neutral = pickle.load(dic)
					f.seek(neutral[1]*fsize)
					neutral = pickle.load(f)
					IDs = IDs.union(set(neutral[:29]))
					while neutral[29] != -1:
						f.seek(neutral[29]*fsize)
						neutral = pickle.load(f)
						IDs = IDs.union(set(neutral[:29]))
				i = 1
				while True:
					dic.seek(size*i)
					l = pickle.load(dic)
					if(l[0] == data): # pega todos os ID's que estão nesse dicionário
						i = l[1]
						f.seek(fsize*i)
						l = pickle.load(f)
						IDs = IDs.union(set(l[:29]))
						while(l[29] != -1):
							i = l[29]
							f.seek(fsize*i)
							l = pickle.load(f)
							IDs = IDs.union(set(l[:29]))
						if -1 in IDs:
							IDs.remove(-1)
						return IDs	# retorna todos ID's desse filtro
					i += 1
	except:
		return set()

# adiciona um ID no arquivo de Posting
def addID(dicFile, dataFile, data, ID):
	try:
		with open(dicFile, 'r+b') as dic:
			with open(dataFile, 'r+b') as f:
				size = pickle.load(dic)
				i = 1
				while True:
					dic.seek(size*i)
					l = pickle.load(dic)
					if(l[0] == data): # se encontrou no dicionário, acrescenta 1 nesse dado
						dic.seek(size*i)
						l[2] += 1
						pickle.dump(l, dic)
						fsize = pickle.load(f)
						i = l[1]
						f.seek(fsize*i)
						l = pickle.load(f)
						while(l[29] != -1): # vai até o final da lista
							i = l[29]
							f.seek(fsize*i)
							l = pickle.load(f)
						if(l[28] == -1): # adiciona, no final, se tem espaço
							l[l.index(-1)] = ID
							#print(l)
							f.seek(fsize*i)
							pickle.dump(l, f)
							return
						else: # cria um novo bloco e faz o antigo apontar para o novo no campo 29 e o novo apontar para o antigo, no campo 30
							f.seek(0, 2) # vai para o final
							l[29] = f.tell()//fsize # pega o bloco que se deve apontar n bytes/tamanho do bloco, divisão inteira
							newList = [ID] + [-1]*31
							newList[30] = i
							bytesToAdd = fsize - len(pickle.dumps(newList))
							pickle.dump(newList, f)
							f.write(bytearray(bytesToAdd))
							f.seek(fsize*i)
							pickle.dump(l, f)
							return 
					i += 1
	except:
		try:
			# cria um novo campo no dicionário, se não encontrar e adiciona no arquivo de Posts
			with open(dicFile, 'r+b') as dic:
				with open(dataFile, 'r+b') as f:
					size = pickle.load(dic)
					dic.seek(-size, 2)
					neutralValue = pickle.load(dic)
					fsize = pickle.load(f)
					f.seek(0, 2)
					new = f.tell()//fsize
					newD = dic.tell()//size
					bytesToAdd = fsize - len(pickle.dumps([ID]+[-1]*30+[newD]))
					pickle.dump([ID]+[-1]*30+[newD], f)
					f.write(bytearray(bytesToAdd))
					dic.seek(-size, 2)
					bytesToAdd = size - len(pickle.dumps([data, new, 1]))
					pickle.dump([data, new, 1], dic)
					dic.write(bytearray(bytesToAdd))
					if data == '***': # se o valor for desconhecido, acrescenta ele no dicionário e armazena sua localização no último bloco
						neutralValue = newD
					bytesToAdd = size - len(pickle.dumps(neutralValue))
					pickle.dump(neutralValue, dic)
					dic.write(bytearray(bytesToAdd))
		except:
			return

# remove um ID no arquivo de Posting
def removeID(dicFile, dataFile, data, ID):
	try:
		with open(dicFile, 'r+b') as dic:
			with open(dataFile, 'r+b') as f:
				size = pickle.load(dic)
				i = 1
				while True:
					dic.seek(size*i)
					l = pickle.load(dic)
					if(l[0] == data):
						dic.seek(size*i)
						j = l[1]
						if(l[2] > 1): # diminui um no tamanho do dicionário
							l[2] -= 1
							pickle.dump(l, dic)
						else: # se vai zerar, então tira ele do dicionário
							dic.seek(-(2*size), 2)
							indexDic = dic.tell()//size
							#print(ID)
							if(indexDic != i): # se ele não é o último, então coloca o último na posição vaga
								new = pickle.load(dic)
								dic.seek(size*i)
								pickle.dump(new, dic)
							dic.seek(-size, 2)
							val = pickle.load(dic)
							dic.seek(-(2*size), 2)
							if(val == i): # se o campo neutro, foi removido
								val = -1
							elif(val == indexDic): # se o campo neutro foi deslocado
								val = i
							#print(val)
							pickle.dump(val, dic) # coloca o indíce do campo neutro para cima
							dic.seek(-size, 2)
							dic.truncate()
						fsize = pickle.load(f)
						f.seek(fsize*j)
						l = pickle.load(f)
						while(ID not in l[:29]): # encontrar ID na lista de postings
							j = l[29]
							f.seek(fsize*j)
							l = pickle.load(f)
						indexID = l.index(ID)
						if indexID == 0 and l[indexID+1] == -1: # se a lista contém, um único ID, então pode removê-la
							if(l[30] != -1): # não apontar para lista removida
								f.seek(l[30]*fsize)
								pointer = pickle.load(f)
								pointer[29] = -1
								f.seek(l[30]*fsize)
								pickle.dump(pointer, f)
							f.seek(-fsize, 2) # trazer último para espaço vago
							new = pickle.load(f)
							f.seek(-fsize, 2)
							f.truncate()
							if(new[30] != -1): # atualizar a lista que aponta para essa nova lista que mudou de lugar, se tiver
								f.seek(new[30]*fsize)
								toUpdate = pickle.load(f)
								toUpdate[29] = j
								f.seek(new[30]*fsize)
								pickle.dump(toUpdate, f)
							if(new[31] != -1): # atualizar o campo do dicionário que aponta para o ínicio da lista, se for o primeiro
								dic.seek(new[31]*size)
								b = pickle.load(dic)
								dic.seek(new[31]*size)
								b[1] = j
								pickle.dump(b, dic)
							#print(j)
							f.seek(j*fsize) # coloca o último nesse lugar
							#print(new)
							pickle.dump(new, f)
							return 
						else:
							if l[29] == -1: # se a lista não tem mais segmento, então troca o ID com o último e seta o último para -1(não existe)
								last = l.index(-1)-1
								l[indexID] = l[last]
								l[last] = -1
								f.seek(j*fsize)
								pickle.dump(l, f)
								return
							else: # senão, busca o último da lista, e coloca no lugar do ID removido
								a = copy.deepcopy(l)
								newj = a[29]
								while(a[29] != -1):
									newj = a[29]
									f.seek(fsize*newj)
									a = pickle.load(f)
								last = a.index(-1)-1
								if last > 0: # se a lista não foi removida por completo, então apenas coloca o último na posição do ID removido
									l[indexID] = a[last]
									a[last] = -1
									f.seek(newj*fsize)
									pickle.dump(a, f)
									f.seek(j*fsize)
									pickle.dump(l, f)
									return 
								else: # se a última lista vai ser removida
									l[indexID] = a[last]
									f.seek(j*fsize)
									pickle.dump(l, f)
									toUpdate = a[30]
									f.seek(toUpdate*fsize)
									a = pickle.load(f)
									a[29] = -1
									f.seek(toUpdate*fsize)
									a = pickle.dump(a, f)
									f.seek(-fsize, 2)
									a = pickle.load(f)
									f.seek(-fsize, 2)
									f.truncate()
									f.seek(newj*fsize) # coloca o último na posição da lista removida
									pickle.dump(a, f)
									if a[30] != -1: # atualiza quem aponta para lista movida
										f.seek(a[30]*fsize)
										b = pickle.load(f)
										f.seek(a[30]*fsize)
										b[29] = newj
										pickle.dump(b, f)
									elif a[31] != -1: # atualiza o dicionário para a lista movida, se for a primeira
										dic.seek(a[31]*size)
										b = pickle.load(dic)
										dic.seek(a[31]*size)
										b[1] = newj
										pickle.dump(b, dic)
									return
					i += 1
	except:
		return

# adicionar ocorrência ou aeronave, apenas adiciona no final do arquivo
def addInMainFile(l, file):
	try:
		with open(file, 'r+b') as f:
			size = pickle.load(f)
			f.seek(0, 2)
			pos = f.tell()//size
			bytesToAdd = size - len(pickle.dumps(l))
			pickle.dump(l, f)
			f.write(bytearray(bytesToAdd))
			return pos
	except:
		return -1

# remover ocorrência ou aeronave, apenas troca o último com o removido
def removeInMainFile(index, file):
	try:
		with open(file, 'r+b') as f:
			size = pickle.load(f)
			f.seek(-size, 2)
			lastIndex = f.tell()//size
			if lastIndex == index: # if removes the last
				f.truncate()
				return -1
			data = pickle.load(f)
			f.seek(-size, 2)
			f.truncate()
			f.seek(size*index)
			pickle.dump(data, f)
			return data[0] # return the ID of this new position
	except:
		return -1
		

#showSorted('dicUF.bin')
#print(len(getIDs('dicUF.bin', 'UF.bin', 'RR')))
#removeInMainFile(6236, 'oco.bin')
#printall('oco.bin')
	
'''
printall('type.bin')
print('*'*1000)
removeID('dicType.bin', 'type.bin', 'COMBUSTÍVEL', '201711061312157')
printall('dicType.bin')
printall('type.bin')
removeID('dicType.bin', 'type.bin', 'INDETERMINADO', '201712142055195') 
print('*'*1000)
printall('dicType.bin')
printall('type.bin')
'''

'''l = ['201705081607406', '201212265644125', '200807154929894', '201604272030187', '201412233311507', '201603071405371', '201401278814115', '200601279918299', '201106302635465', '200804254915087', '201008286552068', '201212101171503', '201307033573604', '201707121918319', '201201051092581', '201004284310396', '201308234758453', '201505087360446', '201210105117902', '200707163902019', '201111244775751', '201703232208022', '201102081839406', '201112216010340', '200712228250564', '201410072593829', '200710089293807', '201007095350319', '201305315141885']
for ID in l:
	printall('UF.bin')
	removeID('dicUF.bin', 'UF.bin', 'RS', ID)
	print('*'*100)'''
