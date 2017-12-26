import pickle
import Trie
import filesCreation

# Create Inverted Indexes!
# The last byte of dictionary has 0 or 1 and can be interpreted as:
# 0 - First element in dictionary is not unknow information
# 1 - First element in dictionary is unknow (you should include it)
# To read the last byte you just do this:
# f.seek(-1,2)
# a = int.from_bytes(f.read(), 'little')
# f.seek(0) to rewind

# Creation of Dictionary File + Postings
# Read with pickle.load() method
# Dictionary file has a list with two elements:
# - First = Element to be Searched
# - Second = Byte that starts in the posting file
# Posting List has all the ID's
def createFiles():			
	l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'invStatus.bin', 'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin']
	l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin']
	l3 = [1, 2, 5, 6, 8, 12, 3, 4, 5, 8, 10, 21]
	l4 = ['ACIDENTE', 'FALHA DO MOTOR EM VOO', 'NÃO IDENTIFICADA', 'SC', 'SJOG', 'ATIVA', 'HELICÓPTERO', 'AIRBUS INDUSTRIE', '56-C', 'QUADRIMOTOR', 'LEVE', 'SUBSTANCIAL']
	l5 = [None, 'INDETERMINADA', 'NÃO IDENTIFICADA', '***', '****', None, 'INDETERMINADA', '***', '***', '***', '***', 'INDETERMINADO']
	for i in range(len(l1)):
		inDir = None
		if (i < 6):
			inDir = 'oco.csv'
		else:
			inDir = 'anv.csv'
		filesCreation.createFile(inDir, l1[i], l2[i], l3[i], l4[i], l5[i])
	filesCreation.dayShiftFile()
	filesCreation.fatalitiesFile()


# Showing ranking min(20, size of dictionary), preferable to use histogram

def showRank():
	l1 = ['Classificação', 'Tipo de Falha', 'Cidade', 'UF', 'Aeródromo', 'Status Investigativo', 'Turno do Dia', 'Tipo de Veículo', 'Fabricante', 'Modelo', 'Quantidade de Motores', 'Porte da Aeronave', 'Dano', 'Presença de Fatalidades']
	l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicInvStatus.bin', 'dicDayShift.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
	for i in range(len(l2)):
		with open(l2[i], 'rb') as dic:
			size = 0
			try:
				dic.seek(-1, 2)
				hasNeutral = int.from_bytes(dic.read(), 'little')
				word = []
				dic.seek(0)
				cur = pickle.load(dic)
				if(hasNeutral == 1):
					word.append((int(cur[2]), 'INDETERMINAÇÃO'))
				else:
					word.append((int(cur[2]), cur[0]))
				size += int(cur[2])
				while True:
					cur = pickle.load(dic)
					word.append((int(cur[2]), cur[0]))
					size += int(cur[2])
			except:
				word.sort(reverse=True)
				if i == 0:
					print('\n\n{} {} {}\n\n'.format('*'*33, 'OCORRÊNCIAS', '*'*33))
				elif i == 7:
					print('\n\n{} {} {}\n\n'.format('*'*33, 'AERONAVES', '*'*33))
				print('{}:\n'.format(l1[i]))
				for i in range(min(len(word), 10)):
					print('{:>30} = {:5.2f}%'.format(word[i][1], word[i][0]/size*100))
				if i != 0 and i != 7:
					print('-'*80)
				continue
				
def createTrieFile():
	Tree = Trie.Trie()
	with open('oco.csv', 'r') as f:
		l = f.readline()
		while True:
			byte = f.tell()
			ID = f.readline().split('~')[0].strip('"')
			if(ID == ''):
				break
			Tree.addKey(ID, byte)
		Tree.saveTrie('Trie.bin')

def printInfo(info):
	data = '"codigo_ocorrencia"~"ocorrencia_classificacao"~"ocorrencia_tipo"~"ocorrencia_latitude"~"ocorrencia_longitude"~"ocorrencia_cidade"~"ocorrencia_uf"~"ocorrencia_pais"~"ocorrencia_aerodromo"~"ocorrencia_dia"~"ocorrencia_horario"~"investigacao_aeronave_liberada"~"investigacao_status"~"divulgacao_relatorio_numero"~"divulgacao_relatorio_publicado"~"divulgacao_dia_publicacao"~"total_recomendacoes"~"total_aeronaves_envolvidas"~"ocorrencia_saida_pista"~"ocorrencia_dia_extracao"'
	info = [x.strip('\n').strip('"') for x in info.split('~')]
	data = [x.strip('"') for x in data.split('~')]
	for i in range(len(data)):
		print('{:>30} - {}'.format(data[i], info[i]))
		
def filterID():
	print('Busca do ID\n')
	IDs = set()
	ID = input('ID da ocorrência parcial ou total: ')
	print()
	Tree = Trie.Trie()
	if(len(ID) == 15):
		byte = Tree.traverseTrie(ID, 'Trie.bin')
		if byte != -1:	
			with open('oco.csv', 'r') as f:
				f.seek(byte)
				info = f.readline()
				printInfo(info)
			return True
		else:
			print('ID não encontrado')
			return False
	else:
		IDs = IDs.union(Tree.filterIDTrie(ID, 'Trie.bin'))
		if(len(IDs) == 0):
			print('Nenhum ID com esse prefixo encontrado')
			return False
		elif(len(IDs) == 1):
			for one in IDs:
				ID = one
			byte = Tree.traverseTrie(ID, 'Trie.bin')
			with open('oco.csv', 'r') as f:
				f.seek(byte)
				info = f.readline()
				printInfo(info)
			return True
		else:
			ans = '2'
			print('Remaining IDs:\n')
			for ID in IDs:
				print(ID)
			print()
			while ans != '0' and ans != '1':
				ans = input('0 - Filtrar mais\n1 - Sei o meu ID\nSua Escolha: ')
			if(ans == '1'):
				ID = input('ID: ')
				while ID not in IDs:
					ID = input('ID: ')
				byte = Tree.traverseTrie(ID, 'Trie.bin')	
				with open('oco.csv', 'r') as f:
					f.seek(byte)
					info = f.readline()
					printInfo(info)
				return True
			l = ['Classificação', 'Tipo de Falha', 'Cidade', 'UF', 'Aeródromo', 'Status Investigativo', 'Turno do Dia', 'Tipo de Veículo', 'Fabricante', 'Modelo', 'Quantidade de Motores', 'Porte da Aeronave', 'Dano', 'Presença de Fatalidades']
			l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicInvStatus.bin', 'dicDayShift.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
			l3 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'invStatus.bin', 'dayShift.bin', 'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin', 'fatalities.bin']
			while len(IDs) > 1 and len(l) > 0:
				ans = -1
				while(ans < 0 or ans >= len(l)):
					print('0 - Sair')
					for j in range(len(l)):
						print('{} - {}'.format(j+1, l[j]))
					ans = input('Escolha uma opção para filtrar: ')
					if ans.isdigit():
						ans = int(ans)
					else:
						print('{0}Você não digitou um número{0}'.format('*'*20))
						ans = -1
				if ans == 0:
					break
				else:
					l.pop(ans-1)
					Data = input('Info: ')
					with open(l2[ans-1], 'rb') as f:
						with open(l3[ans-1], 'rb') as f2:
							try:
								lis = set()
								f.seek(-1, 2)
								unknow = int.from_bytes(f.read(), 'little')
								f.seek(0)
								data = pickle.load(f)
								if(unknow == 1):
									f2.seek(data[1])
									lis = set(pickle.load(f2))
								while Data != data[0]:
									data = pickle.load(f)
								f2.seek(data[1])
								lis = lis.union(set(pickle.load(f2)))
								IDs.intersection_update(lis)
							except:
								print('Não há nenhum dado com esse filtro')
					l2.pop(ans-1)
					l3.pop(ans-1)
					print('Remaining IDs:\n')
					for ID in IDs:
						print(ID)
					print()
					if(len(IDs) > 1):
						ans = '2'
						while ans != '0' and ans != '1':
							ans = input('0 - Filtrar mais\n1 - Sei o meu ID\nSua Escolha: ')
						if(ans == '1'):
							ID = input('ID: ')
							while ID not in IDs:
								ID = input('ID: ')
							byte = Tree.traverseTrie(ID, 'Trie.bin')	
							with open('oco.csv', 'r') as f:
								f.seek(byte)
								info = f.readline()
								printInfo(info)
							return True
			if(len(IDs) > 0):
				with open('oco.csv', 'r') as f:
					for data in IDs:
						print()
						byte = Tree.traverseTrie(data, 'Trie.bin')
						f.seek(byte)
						info = f.readline()
						printInfo(info)
						print()
			else:
				print('Nenhum ID foi encontrado')
					
createFiles()
showRank()
createTrieFile()
filterID()


	