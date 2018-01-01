import filesCreation
import Trie
import supportFile
import pickle
import copy
import os.path


def createREADME():
    string = '''Os dados sobre ocorrência devem seguir os seguinte formato:
	"ocorrencia classificacao"~"ocorrencia tipo"~"ocorrencia latitude"~"ocorrencia longitude"~"ocorrencia cidade"~"ocorrencia uf"~"ocorrencia pais"~"ocorrencia aerodromo"~"ocorrencia dia"~"ocorrencia horario"~"investigacao aeronave liberada"~"investigacao status"~"divulgacao relatorio numero"~"divulgacao relatorio publicado"~"divulgacao dia publicacao"~"total recomendacoes"~"total aeronaves envolvidas"~"ocorrencia saida pista"~"ocorrencia dia extracao"
	cada informação deve estar entre aspas e separada de outra por um ~, por favor, separe a palavra dentro das aspas com espaços, os dados devem seguir a ordem acima substituindo pelo seus respectivos dados, caso não tenha dados sobre a informação, por favor, coloque três asteriscos(***).
	A mesma lógica segue para o dados das aeronaves, com a seguinte ordem:
	"aeronave matricula"~"aeronave operador categoria"~"aeronave tipo veiculo"~"aeronave fabricante"~"aeronave modelo"~"aeronave tipo icao"~"aeronave motor tipo"~"aeronave motor quantidade"~"aeronave pmd"~"aeronave pmd categoria"~"aeronave assentos"~"aeronave ano fabricacao"~"aeronave pais fabricante"~"aeronave pais registro"~"aeronave registro categoria"~"aeronave registro segmento"~"aeronave voo origem"~"aeronave voo destino"~"aeronave fase operacao"~"aeronave tipo operacao"~"aeronave nivel dano"~"total fatalidades"~"aeronave dia extracao"
	A matrícula da aeronave deve sem um valor diferente de *** '''
    with open('README.txt', 'w') as f:
        f.write(string)


def sortedIDs(treeFile):
    Tree = Trie.Trie(2000)
    Tree.inOrder(treeFile)


def sortedData(dicFile):
    supportFile.showSorted(dicFile)


def showRank(dicFile):
    supportFile.getTop(dicFile)


def filterIDTrie(ID, treeFile):
    Tree = Trie.Trie(2000)
    return (Tree.filterID(ID, treeFile))


def getInfoID(ID, treeFile):
    Tree = Trie.Trie(2000)
    a = Tree.findID(ID, treeFile)
    if (a == -1):
        return -1
    b = []
    with open('oco.bin', 'rb') as f:
        size = pickle.load(f)
        f.seek(a.getOco() * size)
        b.append(pickle.load(f))
    with open('anv.bin', 'rb') as f:
        size = pickle.load(f)
        for anv in a.getAnv():
            f.seek(anv * size)
            b.append(pickle.load(f))
    return b


def readNewData(treeFile):
    Tree = Trie.Trie(2000)
    ID = input('Insira o ID: ')
    a = 0
    if ID.isdigit():
        a = Tree.findID(ID, treeFile)
    while not ID.isdigit() or a != -1 or ID == '':
        print('ID Inválido')
        ID = input('Insira o ID: ')
        a = Tree.findID(ID, treeFile)
    data = input('Insira as informações da ocorrência conforme o README.txt\n').split('~')
    while len(data) != 19:
        data = input('Insira as informações da ocorrência conforme o README.txt\n').split('~')
    ocoList = [x.strip('\n').strip('"') for x in data]
    ocoList.insert(0, ID)
    anvList = []
    while True:
        data = input('Insira as informações da aeronave conforme o README.txt\n').split('~')
        while len(data) != 23 or data[0] == '***':
            data = input('Insira as informações da aeronave conforme o README.txt\n').split('~')
        l = [x.strip('\n').strip('"') for x in data]
        l.insert(0, ID)
        anvList.append(l)
        ans = input('0 - Parar\n1 - Adicionar nova aeronave com esse ID\nSua Escolha: ')
        while not ans.isdigit() or int(ans) < 0 or int(ans) > 1:
            print('Insira um número entre 0 e 1')
            ans = input('Sua Escolha: ')
        if ans == '0':
            break
    return ocoList, anvList


# ocoList no mesmo formato, anvList será uma lista de listas (pode ter + de um ID), ambos devem ter o mesmo ID
def addData(ocoList, anvList, treeFile):
    Tree = Trie.Trie(2000)
    a = Tree.findID(ocoList[0], treeFile)
    if (a != -1):  # can't add an existing ID
        return -1
    pos = supportFile.addInMainFile(ocoList, 'oco.bin')
    Tree.addID(ocoList[0], pos, treeFile)
    for anv in anvList:
        pos = supportFile.addInMainFile(anv, 'anv.bin')
        Tree.updateID(anv[0], None, pos, None, treeFile, 0)  # append
    l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin',
          'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin', 'fatalities.bin']
    l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin',
          'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin',
          'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
    l3 = [1, 2, 5, 6, 8, 10, 12, 3, 4, 5, 8, 10, 21, 22]
    if ocoList[10][:2].isdigit():
        hour = int(ocoList[10][:2])
        ocoList[10] = 'NOITE'
        if (hour < 6):
            ocoList[10] = 'MADRUGADA'
        elif (hour < 12):
            ocoList[10] = 'MANHÃ'
        elif (hour < 18):
            ocoList[10] = 'TARDE'
    for i in range(7):
        supportFile.addID(l2[i], l1[i], ocoList[l3[i]], ocoList[0])
    for anv in anvList:
        if anv[22].isdigit():
            if anv[22] == '0':
                anv[22] = 'NÃO'
            else:
                anv[22] = 'SIM'
        for i in range(7, len(l1)):
            supportFile.addID(l2[i], l1[i], anv[l3[i]], anv[0])


def updateList(l, infoFile):
    info = []
    s = copy.deepcopy(l)
    with open(infoFile, 'rb') as f:
        info = pickle.load(f)
    start = 0
    if (infoFile == 'infoAnv.bin'):
        start = 1
    while True:
        print('0 - Sair')
        for i in range(1, len(info) - start):
            print('{} - {} = {}'.format(i, info[i + start], s[i + start]))
        ans = input('Deseja alterar qual informação? Digite o número correspondente: ')
        while not ans.isdigit() or int(ans) < 0 or int(ans) > len(info) - start:
            ans = input('Deseja alterar qual informação? Digite o número correspondente: ')
        if ans == '0':
            break
        newData = input('Digite o dado corrigido: (*** se for indeterminado): ')
        s[int(ans) + start] = newData.upper()
    return s


def updateOco(ID, treeFile):
    Tree = Trie.Trie(2000)
    a = Tree.findID(ID, treeFile)
    if (a == -1):
        return -1
    d = []
    ocoList = []
    with open('oco.bin', 'r+b') as f:
        size = pickle.load(f)
        f.seek(a.getOco() * size)
        d = pickle.load(f)
        ocoList = updateList(d, 'infoOco.bin')
        f.seek(a.getOco() * size)
        pickle.dump(ocoList, f)
    l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin']
    l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin',
          'dicInvStatus.bin']
    l3 = [1, 2, 5, 6, 8, 10, 12]
    if ocoList[10][:2].isdigit():
        hour = int(ocoList[10][:2])
        ocoList[10] = 'NOITE'
        if (hour < 6):
            ocoList[10] = 'MADRUGADA'
        elif (hour < 12):
            ocoList[10] = 'MANHÃ'
        elif (hour < 18):
            ocoList[10] = 'TARDE'
    if d[10][:2].isdigit():
        hour = int(d[10][:2])
        d[10] = 'NOITE'
        if (hour < 6):
            d[10] = 'MADRUGADA'
        elif (hour < 12):
            d[10] = 'MANHÃ'
        elif (hour < 18):
            d[10] = 'TARDE'
    for i in range(len(l1)):
        if d[l3[i]] != ocoList[l3[i]]:
            supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)
            supportFile.addID(l2[i], l1[i], ocoList[l3[i]], ID)


def removeData(ID, treeFile):
    Tree = Trie.Trie(2000)
    a = Tree.findID(ID, treeFile)
    if (a == -1):
        return -1
    Tree.removeID(ID, treeFile)
    d = []
    last = 0
    with open('oco.bin', 'rb') as f:
        size = pickle.load(f)
        f.seek(a.getOco() * size)
        d = pickle.load(f)
        f.seek(-size, 2)
        last = f.tell() // size
    toUpdate = supportFile.removeInMainFile(a.getOco(), 'oco.bin')  # ID to update position
    if toUpdate != -1:
        Tree.updateID(toUpdate, a.getOco(), None, None, treeFile, 0)  # update oco position
    l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin']
    l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin',
          'dicInvStatus.bin']
    l3 = [1, 2, 5, 6, 8, 10, 12]
    if d[10][:2].isdigit():
        hour = int(d[10][:2])
        d[10] = 'NOITE'
        if (hour < 6):
            d[10] = 'MADRUGADA'
        elif (hour < 12):
            d[10] = 'MANHÃ'
        elif (hour < 18):
            d[10] = 'TARDE'
    for i in range(len(l1)):
        supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)  # remove in Posting List
    changed = False
    for data in a.getAnv():  # For each anv
        if not changed:
            anv = data
        changed = False
        d = []
        last = 0
        with open('anv.bin', 'rb') as f:
            size = pickle.load(f)
            f.seek(anv * size)
            d = pickle.load(f)
            f.seek(-size, 2)
            last = f.tell() // size
        toUpdate = supportFile.removeInMainFile(anv, 'anv.bin')  # ID to update Position
        if toUpdate != -1:
            if toUpdate != ID:
                Tree.updateID(toUpdate, None, anv, last, treeFile, 2)  # change anv
            else:
                changed = True
    l1 = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin',
          'fatalities.bin']
    l2 = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin',
          'dicHarm.bin', 'dicFatalities.bin']
    l3 = [3, 4, 5, 8, 10, 21, 22]
    if d[22].isdigit():
        if d[22] == '0':
            d[22] = 'NÃO'
        else:
            d[22] = 'SIM'
    for i in range(len(l1)):
        supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)  # remove in Posting List


    return 0


def updateAnv(ID, registry, treeFile):
    Tree = Trie.Trie(2000)
    a = Tree.findID(ID, treeFile)
    if (a == -1):
        return -1
    with open('anv.bin', 'r+b') as f:
        size = pickle.load(f)
        for anv in a.getAnv():
            f.seek(anv * size)
            d = pickle.load(f)
            if d[1] == registry:
                f.seek(anv * size)
                s = updateList(d, 'infoAnv.bin')
                pickle.dump(s, f)
                if (s[0] != d[0]):
                    return -1  # ID must be the same
                l1 = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin',
                      'fatalities.bin']
                l2 = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin', 'dicClass.bin',
                      'dicHarm.bin', 'dicFatalities.bin']
                l3 = [3, 4, 5, 8, 10, 21, 22]
                if s[22].isdigit():
                    if s[22] == '0':
                        s[22] = 'NÃO'
                    else:
                        s[22] = 'SIM'
                if d[22].isdigit():
                    if d[22] == '0':
                        d[22] = 'NÃO'
                    else:
                        d[22] = 'SIM'
                for i in range(len(l1)):
                    if (s[l3[i]] != d[l3[i]]):  # if they are different
                        # update PostingList
                        supportFile.removeID(l2[i], l1[i], d[l3[i]], ID)
                        supportFile.addID(l2[i], l1[i], s[l3[i]], ID)
                return 0
        return -1


if not os.path.isfile('oco.bin') or not os.path.isfile('anv.bin'):
    filesCreation.createFiles()
if not os.path.isfile('Trie.bin'):
    Trie.buildTrie()
if not os.path.isfile('README.txt'):
    createREADME()

#filesCreation.createFiles()
#Trie.buildTrie()
