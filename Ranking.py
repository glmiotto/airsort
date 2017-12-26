import pickle

# Showing ranking min(20, size of dictionary), preferable to use histogram

l1 = ['Classificação', 'Tipo', 'Cidade', 'UF', 'Aeródromo', 'Status Investigativo', 'Turno do Dia', 'Tipo de Veículo', 'Fabricante', 'Modelo', 'Quantidade de Motores', 'Porte da Aeronave', 'Dano', 'Presença de Fatalidades']
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
	
	