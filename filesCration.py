import pickle

def createMainFiles(inputDir, infoDir, outputDir, blockSize):
	with open(outputDir, 'wb') as f: 
		with open(inputDir, 'r') as oco:
			with open(infoDir, 'wb') as info:
				l = [x.strip('\n').strip('"') for x in oco.readline().split('~')]
				pickle.dump(l, info)
			bytesToAdd = blockSize - len(pickle.dumps(blockSize))
			pickle.dump(blockSize, f)
			f.write(bytearray(bytesToAdd))
			for line in oco:
				l = [x.strip('\n').strip('"') for x in line.split('~')]
				bytesToAdd = blockSize - len(pickle.dumps(l))
				pickle.dump(l, f)
				f.write(bytearray(bytesToAdd))

def createInvertedIndexFile(inputDir, outputDir, dictionaryDir, index, blockSize, dicBlockSize, unknow):
	with open(outputDir, 'wb') as outDir:
		with open(dictionaryDir, 'wb') as dicDir:
			None
	Dic = {}
	PostingList = []
	curIndex = []
	toUpdate = []
	indexSize = []
	S = set()
	with open(inputDir, 'rb') as inDir:
		with open(outputDir, 'r+b') as outDir:
			bytesToAdd = blockSize - len(pickle.dumps(blockSize))
			pickle.dump(blockSize, outDir)
			outDir.write(bytearray(bytesToAdd))
			with open(dictionaryDir, 'r+b') as dicDir:
				bytesToAdd = dicBlockSize - len(pickle.dumps(dicBlockSize))
				pickle.dump(dicBlockSize, dicDir)
				dicDir.write(bytearray(bytesToAdd))
				block = 1
				dicIndex = 0
				fileIndex = 1
				fileDicIndex = 1
				size = pickle.load(inDir)
				try:
					while True:
						inDir.seek(block*size)
						l = pickle.load(inDir)
						ID = l[0]
						if inputDir == 'anv.bin':
							if ID not in S:
								S.add(ID)
							else: # Don't add the same ID more than one time
								block += 1
								continue
						data = l[index]
						if data == '###!' or data == '####':
							data = '****'
						if data not in Dic:
							Dic[data] = dicIndex
							dicIndex += 1
							PostingList.append([-1]*32)
							curIndex.append(0)
							toUpdate.append(-1)
							indexSize.append(0)
						current = Dic[data]
						indexSize[current] += 1
						if(curIndex[current] < 29):
							PostingList[current][curIndex[current]] = ID
							curIndex[current] += 1
						else:
							backPointer = -1
							dicPointer = -1
							if(toUpdate[current] != -1):
								PostingList[current][30] = toUpdate[current]
								outDir.seek(toUpdate[current]*blockSize)
								r = pickle.load(outDir)
								outDir.seek(toUpdate[current]*blockSize)
								r[29] = fileIndex
								pickle.dump(r, outDir)
								outDir.seek(0, 2) # end of file
							else:
								PostingList[current][31] = fileDicIndex
								bytesToAdd = dicBlockSize - len(pickle.dumps([data, fileIndex]))
								pickle.dump([data, fileIndex], dicDir)
								dicDir.write(bytearray(bytesToAdd))
								fileDicIndex += 1
							bytesToAdd = blockSize - len(pickle.dumps(PostingList[current]))
							pickle.dump(PostingList[current], outDir)
							outDir.write(bytearray(bytesToAdd))
							toUpdate[current] = fileIndex
							PostingList[current] = [ID]+[-1]*31
							curIndex[current] = 1
							fileIndex += 1
						block += 1
				except:
					try:
						for key in Dic.keys():
							current = Dic[key]
							if PostingList[current] != -1:
								if toUpdate[current] != -1:
									PostingList[current][30] = toUpdate[current]
									outDir.seek(toUpdate[current]*blockSize)
									r = pickle.load(outDir)
									outDir.seek(toUpdate[current]*blockSize)
									r[29] = fileIndex
									pickle.dump(r, outDir)
									outDir.seek(0, 2) # end of file
								else:
									PostingList[current][31] = fileDicIndex
									bytesToAdd = dicBlockSize - len(pickle.dumps([key, fileIndex]))
									pickle.dump([key, fileIndex], dicDir)
									dicDir.write(bytearray(bytesToAdd))
									fileDicIndex += 1
								bytesToAdd = blockSize - len(pickle.dumps(PostingList[current]))
								pickle.dump(PostingList[current], outDir)
								outDir.write(bytearray(bytesToAdd))
								fileIndex += 1
						i = 1
						numberUnknow = -1
						while True:
							dicDir.seek(i*dicBlockSize)
							l = pickle.load(dicDir)
							if(l[0] == unknow):
								numberUnknow = i
							dicDir.seek(i*dicBlockSize)
							l.append(indexSize[Dic[l[0]]])
							pickle.dump(l, dicDir)
							i += 1
					except:
						bytesToAdd = dicBlockSize - len(pickle.dumps(numberUnknow))
						pickle.dump(numberUnknow, dicDir)
						dicDir.write(bytearray(bytesToAdd))

def dayShiftFile(index, blockSize, dicBlockSize):
	with open('dayShift.bin', 'wb') as outDir:
		with open('dicDayShift.bin', 'wb') as dicDir:
			None
	Dic = {}
	PostingList = []
	curIndex = []
	toUpdate = []
	indexSize = []
	with open('oco.bin', 'rb') as inDir:
		with open('dayShift.bin', 'r+b') as outDir:
			bytesToAdd = blockSize - len(pickle.dumps(blockSize))
			pickle.dump(blockSize, outDir)
			outDir.write(bytearray(bytesToAdd))
			with open('dicDayShift.bin', 'r+b') as dicDir:
				bytesToAdd = dicBlockSize - len(pickle.dumps(dicBlockSize))
				pickle.dump(dicBlockSize, dicDir)
				dicDir.write(bytearray(bytesToAdd))
				block = 1
				dicIndex = 0
				fileIndex = 1
				fileDicIndex = 1
				size = pickle.load(inDir)
				try:
					while True:
						inDir.seek(block*size)
						l = pickle.load(inDir)
						ID = l[0]
						data = l[index]
						hour = int(data[:2])
						data = 'NOITE'
						if(hour < 6):
							data = 'MADRUGADA'
						elif(hour < 12):
							data = 'MANHÃ'
						elif(hour < 18):
							data = 'TARDE'
						if data not in Dic:
							Dic[data] = dicIndex
							dicIndex += 1
							PostingList.append([-1]*32)
							curIndex.append(0)
							toUpdate.append(-1)
							indexSize.append(0)
						current = Dic[data]
						indexSize[current] += 1
						if(curIndex[current] < 29):
							PostingList[current][curIndex[current]] = ID
							curIndex[current] += 1
						else:
							if(toUpdate[current] != -1):
								PostingList[current][30] = toUpdate[current]
								outDir.seek(toUpdate[current]*blockSize)
								r = pickle.load(outDir)
								outDir.seek(toUpdate[current]*blockSize)
								r[29] = fileIndex
								pickle.dump(r, outDir)
								outDir.seek(0, 2) # end of file
							else:
								PostingList[current][31] = fileDicIndex
								bytesToAdd = dicBlockSize - len(pickle.dumps([data, fileIndex]))
								pickle.dump([data, fileIndex], dicDir)
								dicDir.write(bytearray(bytesToAdd))
								fileDicIndex += 1
							bytesToAdd = blockSize - len(pickle.dumps(PostingList[current]))
							pickle.dump(PostingList[current], outDir)
							outDir.write(bytearray(bytesToAdd))
							toUpdate[current] = fileIndex
							PostingList[current] = [ID]+[-1]*31
							curIndex[current] = 1
							fileIndex += 1
						block += 1
				except:
					try:
						for key in Dic.keys():
							current = Dic[key]
							if PostingList[current] != -1:
								if toUpdate[current] != -1:
									PostingList[current][30] = toUpdate[current]
									outDir.seek(toUpdate[current]*blockSize)
									r = pickle.load(outDir)
									outDir.seek(toUpdate[current]*blockSize)
									r[29] = fileIndex
									pickle.dump(r, outDir)
									outDir.seek(0, 2) # end of file
								else:
									PostingList[current][31] = fileDicIndex
									bytesToAdd = dicBlockSize - len(pickle.dumps([key, fileIndex]))
									pickle.dump([key, fileIndex], dicDir)
									dicDir.write(bytearray(bytesToAdd))
									fileDicIndex += 1
								bytesToAdd = blockSize - len(pickle.dumps(PostingList[current]))
								pickle.dump(PostingList[current], outDir)
								outDir.write(bytearray(bytesToAdd))
								fileIndex += 1
						i = 1
						while True:
							dicDir.seek(i*dicBlockSize)
							l = pickle.load(dicDir)
							dicDir.seek(i*dicBlockSize)
							l.append(indexSize[Dic[l[0]]])
							pickle.dump(l, dicDir)
							i += 1
					except:
						bytesToAdd = dicBlockSize - len(pickle.dumps(-1))
						pickle.dump(-1, dicDir)
						dicDir.write(bytearray(bytesToAdd))

def fatalitiesFile(index, blockSize, dicBlockSize):
	with open('fatalities.bin', 'wb') as outDir:
		with open('dicFatalities.bin', 'wb') as dicDir:
			None
	Dic = {}
	PostingList = []
	curIndex = []
	toUpdate = []
	indexSize = []
	S = set()
	with open('anv.bin', 'rb') as inDir:
		with open('fatalities.bin', 'r+b') as outDir:
			bytesToAdd = blockSize - len(pickle.dumps(blockSize))
			pickle.dump(blockSize, outDir)
			outDir.write(bytearray(bytesToAdd))
			with open('dicFatalities.bin', 'r+b') as dicDir:
				bytesToAdd = dicBlockSize - len(pickle.dumps(dicBlockSize))
				pickle.dump(dicBlockSize, dicDir)
				dicDir.write(bytearray(bytesToAdd))
				block = 1
				dicIndex = 0
				fileIndex = 1
				fileDicIndex = 1
				size = pickle.load(inDir)
				try:
					while True:
						inDir.seek(block*size)
						l = pickle.load(inDir)
						ID = l[0]
						if ID not in S:
							S.add(ID)
						else: # Don't add the same ID more than one time
							block += 1
							continue
						data = l[index]
						if data == '0':
							data = 'NÃO'
						else:
							data = 'SIM'
						if data not in Dic:
							Dic[data] = dicIndex
							dicIndex += 1
							PostingList.append([-1]*32)
							curIndex.append(0)
							toUpdate.append(-1)
							indexSize.append(0)
						current = Dic[data]
						indexSize[current] += 1
						if(curIndex[current] < 29):
							PostingList[current][curIndex[current]] = ID
							curIndex[current] += 1
						else:
							if(toUpdate[current] != -1):
								PostingList[current][30] = toUpdate[current]
								outDir.seek(toUpdate[current]*blockSize)
								r = pickle.load(outDir)
								outDir.seek(toUpdate[current]*blockSize)
								r[29] = fileIndex
								pickle.dump(r, outDir)
								outDir.seek(0, 2) # end of file
							else:
								PostingList[current][31] = fileDicIndex
								bytesToAdd = dicBlockSize - len(pickle.dumps([data, fileIndex]))
								pickle.dump([data, fileIndex], dicDir)
								dicDir.write(bytearray(bytesToAdd))
								fileDicIndex += 1
							bytesToAdd = blockSize - len(pickle.dumps(PostingList[current]))
							pickle.dump(PostingList[current], outDir)
							outDir.write(bytearray(bytesToAdd))
							toUpdate[current] = fileIndex
							PostingList[current] = [ID]+[-1]*31
							curIndex[current] = 1
							fileIndex += 1
						block += 1
				except:
					try:
						for key in Dic.keys():
							current = Dic[key]
							if PostingList[current] != -1:
								if toUpdate[current] != -1:
									PostingList[current][30] = toUpdate[current]
									outDir.seek(toUpdate[current]*blockSize)
									r = pickle.load(outDir)
									outDir.seek(toUpdate[current]*blockSize)
									r[29] = fileIndex
									pickle.dump(r, outDir)
									outDir.seek(0, 2) # end of file
								else:
									PostingList[current][31] = fileDicIndex
									bytesToAdd = dicBlockSize - len(pickle.dumps([key, fileIndex]))
									pickle.dump([key, fileIndex], dicDir)
									dicDir.write(bytearray(bytesToAdd))
									fileDicIndex += 1
								bytesToAdd = blockSize - len(pickle.dumps(PostingList[current]))
								pickle.dump(PostingList[current], outDir)
								outDir.write(bytearray(bytesToAdd))
								fileIndex += 1
						i = 1
						while True:
							dicDir.seek(i*dicBlockSize)
							l = pickle.load(dicDir)
							dicDir.seek(i*dicBlockSize)
							l.append(indexSize[Dic[l[0]]])
							pickle.dump(l, dicDir)
							i += 1
					except:
						bytesToAdd = dicBlockSize - len(pickle.dumps(-1))
						pickle.dump(-1, dicDir)
						dicDir.write(bytearray(bytesToAdd))

def createFiles():
	createMainFiles('oco.csv', 'infoOco.bin', 'oco.bin', 500)
	createMainFiles('anv.csv', 'infoAnv.bin', 'anv.bin', 500)
	l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'invStatus.bin', 'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin']
	l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin', 'dicHarm.bin']
	l3 = [1, 2, 5, 6, 8, 12, 3, 4, 5, 8, 10, 21]
	#l4 = ['ACIDENTE', 'FALHA DO MOTOR EM VOO', 'NÃO IDENTIFICADA', 'SC', 'SJOG', 'ATIVA', 'HELICÓPTERO', 'AIRBUS INDUSTRIE', '56-C', 'QUADRIMOTOR', 'LEVE', 'SUBSTANCIAL']
	l5 = [None, 'INDETERMINADA', 'NÃO IDENTIFICADA', '***', '****', None, 'INDETERMINADA', '***', '***', '***', '***', 'INDETERMINADO']
	for i in range(len(l1)):
		inDir = None
		if (i < 6):
			inDir = 'oco.bin'
		else:
			inDir = 'anv.bin'
		createInvertedIndexFile(inDir, l1[i], l2[i], l3[i], 1000, 100, l5[i])
	dayShiftFile(10, 1000, 100)
	fatalitiesFile(22, 1000, 100)

createFiles()

