import pickle

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

def fatalitiesFile():
	Dic = {'SIM' : 0, 'NÃO' : 1}
	PostingList = [[], []]
	with open('anv.csv', 'r') as inputDir:
		l = inputDir.readline() # first line is trash
		with open('fatalities.bin', 'wb') as outputDir:
			with open('dicFatalities.bin', 'wb') as dicDir:
				for line in inputDir:
					data = line.split('~')[22].strip('"')
					ID = line.split('~')[0].strip('"')
					classification = 'NÃO'
					if(data != '0'):
						classification = 'SIM'
					index = Dic[classification]
					PostingList[index].append(ID)
				for data in Dic.keys():
					index = Dic[data]
					PostingList[index] = set(PostingList[index])
					pickle.dump([data, outputDir.tell(), len(PostingList[index])], dicDir)
					pickle.dump(PostingList[index], outputDir)
				info = 0
				info = info.to_bytes(1, 'little')
				dicDir.write(info)
						
	'''Data = 'NÃO'
	with open('dicFatalities.bin', 'rb') as f:
		with open('fatalities.bin', 'rb') as f2:
			try:
				l = set()
				data = pickle.load(f)
				while Data != data[0]:
					data = pickle.load(f)
				f2.seek(data[1])
				l = l.union(set(pickle.load(f2)))
			except:
				print('Not found in dictionary!')'''

def dayShiftFile():
	Dic = {'MADRUGADA' : 0, 'MANHÃ' : 1, 'TARDE' : 2, 'NOITE' : 3}
	PostingList = [[], [], [], []]
	with open('oco.csv', 'r') as inputDir:
		l = inputDir.readline() # first line is trash
		with open('dayShift.bin', 'wb') as outputDir:
			with open('dicDayShift.bin', 'wb') as dicDir:
				for line in inputDir:
					data = line.split('~')[10].strip('"')
					ID = line.split('~')[0].strip('"')
					hour = int(data[:2])
					classification = 'NOITE'
					if(hour < 6):
						classification = 'MADRUGADA'
					elif(hour < 12):
						classification = 'MANHÃ'
					elif(hour < 18):
						classification = 'TARDE'
					index = Dic[classification]
					PostingList[index].append(ID)
				for data in Dic.keys():
					index = Dic[data]
					PostingList[index] = set(PostingList[index])
					pickle.dump([data, outputDir.tell(), len(PostingList[index])], dicDir)
					pickle.dump(PostingList[index], outputDir)
				info = 0
				info = info.to_bytes(1, 'little')
				dicDir.write(info)
						
	'''Data = 'MANHÃ'
	with open('dicDayShift.bin', 'rb') as f:
		with open('dayShift.bin', 'rb') as f2:
			try:
				l = set()
				data = pickle.load(f)
				while Data != data[0]:
					data = pickle.load(f)
				f2.seek(data[1])
				l = l.union(set(pickle.load(f2)))
				print(len(l))
			except:
				print('Not found in dictionary!')'''
					
def createFile(inDir, outDir, dictionaryDir, number, search, unknow):
	Dic = {}
	PostingList = []
	with open(inDir, 'r') as inputDir:
		l = inputDir.readline() # first line is trash
		with open(outDir, 'wb') as outputDir:
			with open(dictionaryDir, 'wb') as dicDir:
				i = 0
				for line in inputDir:
					data = line.split('~')[number].strip('"')
					ID = line.split('~')[0].strip('"')
					if data == '###!' or data == '####':
						data = '****'
					if data not in Dic.keys():
						Dic[data] = i
						PostingList.append([])
						i += 1
					index = Dic[data]
					PostingList[index].append(ID)
				if unknow != None:
					PostingList[Dic[unknow]] = set(PostingList[Dic[unknow]])
					pickle.dump([unknow, outputDir.tell(), len(PostingList[Dic[unknow]])], dicDir)
					pickle.dump(PostingList[Dic[unknow]], outputDir)
					del Dic[unknow]		
				for data in Dic.keys():
					index = Dic[data]
					PostingList[index] = set(PostingList[index])
					pickle.dump([data, outputDir.tell(), len(PostingList[index])], dicDir)
					pickle.dump(PostingList[index], outputDir)
				info = 1
				if unknow == None:
					info = 0
				info = info.to_bytes(1, 'little')
				dicDir.write(info)
	'''# Searching	in file			
	Data = search
	with open(dictionaryDir, 'rb') as f:
		with open(outDir, 'rb') as f2:
			try:
				l = set()
				data = pickle.load(f)
				if(unknow != None):
					f2.seek(data[1])
					l = set(pickle.load(f2))
				while Data != data[0]:
					data = pickle.load(f)
				f2.seek(data[1])
				l = l.union(set(pickle.load(f2)))
				print(len(l))
			except:
				print('Not found in dictionary!')'''

'''			
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
	createFile(inDir, l1[i], l2[i], l3[i], l4[i], l5[i])

dayShiftFile()
fatalitiesFile()

'''				