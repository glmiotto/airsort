import sys
from PyQt5 import QtGui, QtCore, QtWidgets

import airsortUI as design
import qdarkstyle

import supportFile
import mainFunctions

import numpy
import pickle
import datetime
import locale
# this reads the environment and inits the right locale
locale.setlocale(locale.LC_ALL, "")


class example(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)


class MainWIndow(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.setWindowTitle("AirSort - O Sort Amigo")
        self.setWindowIcon(QtGui.QIcon('doggo.png'))

        self.textRegAero = [self.tae0CodOco, self.tae1Matricula, self.tae2CategOperador,
                            self.tae3TipoAero, self.tae4Fabricante, self.tae5Modelo, self.tae6TipoICAO,
                            self.tae7TipoMotor, self.tae8QtdMotores, self.tae9PesoMax, self.tae11NumAssentos,
                            self.tae13PaisFabric, self.tae14PaisRegistro, self.tae15RegCategoria, self.tae16RegSegmento,
                            self.tae17VooOrigem, self.tae18VooDestino, self.tae19FaseOperacao, self.tae20TipoOperacao,
                            self.tae22Fatalidades]
        self.textRegOco = [self.toc0CodOco, self.toc2TipoOco, self.toc3LatitudeOco, self.toc4LongitudeOco,
                           self.toc5CidadeOco, self.toc8AerodromeOco, self.toc13NumRelatOco, self.toc16Recomend]



        self.initializeInsereRemoveTab()

        lll = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin',
         'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin',
         'fatalities.bin']

        self.menuVariablesOco = [self.dropEstado, self.dropCidade, self.dropAerodromo, self.dropTurno, self.dropTipoOcorrencia, self.dropClassificacao]
        self.menuVariablesOcoBin = ['UF.bin', 'city.bin', 'aerodrome.bin', 'dayShift.bin', 'type.bin', 'classification.bin']
        self.menuVariablesOcoDictBin = ['dicUF.bin', 'dicCity.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicType.bin', 'dicClassification.bin']

        self.menuVariablesAero = [self.dropTipoAeronave, self.dropFabricante, self.dropModelo, self.dropQtdMotores, self.dropCategoriaPeso, self.dropDano]
        self.menuVariablesAeroBin = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin','fatalities.bin']
        self.menuVariablesAeroDictBin = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin','dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']


        listaTipoOco = supportFile.returnSorted('dicType.bin')
        self.dropTipoOcorrencia.addItems(listaTipoOco)

        self.dropClassificacao.addItems(supportFile.returnSorted('dicClassification.bin'))

        listaTurnoDia = supportFile.returnSorted('dicDayShift.bin')
        turnos = {"MADRUGADA":0, "MANHÃ":1, "TARDE":2, "NOITE":3} #garante a ordem intuitiva dos turnos (caso nao tenha todos)
        listaTurnoDia = sorted(listaTurnoDia, key=lambda x: (x not in turnos, turnos.get(x), None))
        self.dropTurno.addItems(listaTurnoDia)

        listaCatPesos = supportFile.returnSorted('dicClass.bin')
        pesos = {"***":0, "LEVE":1, "MÉDIA":2, "MÉDIO":3, "PESADA":4, "PESADO":5}  # garante a ordem intuitiva
        listaCatPesos = sorted(listaCatPesos, key=lambda x: (x not in pesos, pesos.get(x), None))
        self.dropCategoriaPeso.addItems(listaCatPesos)

        listaTipoAero = supportFile.returnSorted('dicVeicType.bin')
        self.dropTipoAeronave.addItems(listaTipoAero)

        listaDano = supportFile.returnSorted('dicHarm.bin')
        damages = {"***":0, "NENHUM":1, "LEVE":2, "SUBSTANCIAL":3, "DESTRUÍDA":4, "DESTRUÍDO":5}
        listaDano = sorted(listaDano, key=lambda x: (x not in damages, damages.get(x), None))
        self.dropDano.addItems(listaDano)



        #listaAerodromo = supportFile.returnSorted('dicAerodrome.bin')
        #self.dropAerodromo.addItems(listaAerodromo)

        listaQtdMotores = supportFile.returnSorted('dicQtyEngine.bin')
        motors = {"***":0, "SEM TRAÇÃO":1, "MONOMOTOR":2, "BIMOTOR":3, "TRIMOTOR":4, "QUADRIMOTOR":5}  # garante a ordem intuitiva
        listaQtdMotores = sorted(listaQtdMotores, key=lambda x: (x not in motors, motors.get(x), None))
        self.dropQtdMotores.addItems(listaQtdMotores)


        listaUF = supportFile.returnSorted('dicUF.bin')
        self.dropEstado.clear()
        self.dropEstado.addItem('Qualquer')
        self.dropEstado.addItems(listaUF)

        # se trocar estado, troca a selecao de cidades e aerodromos
        self.dropCidade.setEnabled(False)  # Não pode selecionar, só Qualquer
        self.dropAerodromo.setEnabled(False)  # Não pode selecionar, só Qualquer
        self.dropEstado.currentIndexChanged['QString'].connect(self.onUFSelected)


        listaFabricantes = supportFile.returnSorted('dicManufacturer.bin')
        self.dropFabricante.clear()
        self.dropFabricante.addItem('Qualquer')
        self.dropFabricante.addItems(listaFabricantes)

        # se trocar Fabricante, troca a selecao de modelos
        self.dropModelo.setEnabled(False)  # Não pode selecionar, só Qualquer
        self.dropFabricante.currentIndexChanged['QString'].connect(self.onFabricanteSelected)



        # usa regex para validar entradas ao linebox de codigo ID
        # para até 35 digitos numericos (embora tenham 15 - pois podem ser inseridas novas IDs mais longas mais tarde)
        self.regexNum35 = QtCore.QRegExp("[0-9]\\d{0,34}")
        self.onlyDigits = QtGui.QRegExpValidator(self.regexNum35)
        self.textCodigo.setValidator(self.onlyDigits)

        # Bind ações de menu (Sair/Exit e Sobre/About)
        self.actionSair.triggered.connect(self.shutDown)
        self.actionSobre.triggered.connect(self.aboutWindow)

        # Bind os botoes de Limpar dados de busca e Buscar com dados atuais
        self.limparButton.clicked.connect(self.onLimparButtonClicked)
        self.buscarButton.clicked.connect(self.onBuscarButtonClicked)

        # Bind as duas tabelas ao doubleclick para abrir raw data
        self.tableResultadosOco.itemDoubleClicked.connect(self.onResultDoubleClick)
        self.tableResultadosAero.itemDoubleClicked.connect(self.onResultDoubleClick)

        # Bind a troca de data e hora de começo do período (From) à data e hora mínimas
        # que poderão ser escolhidas no calendário de fim do período (To)
        self.dateTimeFrom.dateTimeChanged.connect(self.onDTFromChanged)



    def onDTFromChanged(self, dt):
        self.dateTimeTo.setMinimumDateTime(dt)

    def onResultDoubleClick(self, item):

        table = self.sender()

        row = item.row()
        id = table.item(row, 0)
        id = id.text()

        #Ocorrencia
        dados = mainFunctions.getInfoID(id, 'Trie.bin')
        textOco = 'Ocorrência\n\n'
        with open('infoOco.bin', 'rb') as f:
            info = pickle.load(f)
            for i in range(len(info)):
                textOco += '{} = {}\n'.format(info[i], dados[0][i])
        #Aeros
        textAero = "\nAeronaves Envolvidas\n"
        with open('infoAnv.bin', 'rb') as f:
            info = pickle.load(f)
            for i in range(1, len(dados)):
                textAero += '\nAeronave {}:\n'.format(i)
                for j in range(len(info)):
                    textAero += '{} = {}\n'.format(info[j], dados[i][j])

        self.rawWindow = QtWidgets.QTextEdit()
        self.rawWindow.setReadOnly(True)
        self.rawWindow.setPlainText(textOco+textAero)
        self.rawWindow.setWindowTitle('\nOcorrência ID {} (raw data)\n'.format(id))
        self.rawWindow.setFixedWidth(500)
        self.rawWindow.setFixedHeight(600)
        self.rawWindow.show()


    def onFabricanteSelected(self):
        # Troca de fabricante implica troca na selecao de modelos

        maker = self.dropFabricante.currentText()

        if (maker != "Qualquer"):
            self.dropModelo.clear()
            self.dropModelo.addItem('Qualquer')
            listaModels = supportFile.getIDs('dicModelsByManufacturer.bin', 'modelsByManufacturer.bin', maker)
            print(maker, listaModels)
            listaModels = sorted(listaModels, key=locale.strxfrm)  # Sort baseado na lingua local (because acentos)
            print(maker, listaModels)
            self.dropModelo.addItems(listaModels)
            self.dropModelo.setEnabled(True)  # Pode selecionar agora

        else: # Se for Qualquer ou ***, presume-se modelo Qualquer
            self.dropModelo.clear()
            self.dropModelo.addItem('Qualquer')
            self.dropModelo.setEnabled(False) # Não pode selecionar, só Qualquer


    # Troca de Estado
    def onUFSelected(self):

        uf = self.dropEstado.currentText() # Novo dado escolhido em Estado

        if (uf != "***") and (uf != "Qualquer"): # Se for UF válido
            self.dropCidade.clear()
            self.dropCidade.addItem('Qualquer')
            listaCidades = supportFile.getIDs('dicCitiesByUF.bin', 'citiesByUF.bin', uf)
            listaCidades = sorted(listaCidades, key=locale.strxfrm) # Sort baseado na lingua local (because acentos)
            self.dropCidade.addItems(listaCidades)
            self.dropCidade.setEnabled(True) # Pode selecionar

            self.dropAerodromo.clear()
            self.dropAerodromo.addItem("Qualquer")
            listaAerodromos = supportFile.getIDs('dicAerodromesByUF.bin', 'aerodromesByUF.bin', uf)
            listaAerodromos = sorted(listaAerodromos, key=locale.strxfrm)
            self.dropAerodromo.addItems(listaAerodromos)
            self.dropAerodromo.setEnabled(True)  # Pode selecionar

        else: # Se for Qualquer ou ***, presume-se cidade Qualquer
            self.dropCidade.clear()
            self.dropCidade.addItem('Qualquer')
            self.dropCidade.setEnabled(False) # Não pode selecionar, só Qualquer

            self.dropAerodromo.clear()
            self.dropAerodromo.addItem('Qualquer')
            self.dropAerodromo.setEnabled(False)  # Não pode selecionar, só Qualquer

    def onLimparButtonClicked(self):

        # Reseta todos os drop down menus para o índice 0, com a opção "Qualquer"
        for v in self.menuVariablesOco:
            v.setCurrentIndex(0)
        for v in self.menuVariablesAero:
            v.setCurrentIndex(0)

        # Limpa a entrada do ID
        self.textCodigo.setText("")

        # Limpa button groups:
        self.butInvQqr.setChecked(True)
        self.butFatalQqr.setChecked(True)

        # Reseta calendário FROM para seu mínimo e o TO para a data atual no sistema do usuário
        self.dateTimeFrom.setDateTime(self.dateTimeFrom.minimumDateTime())
        self.dateTimeTo.setDateTime(self.dateTimeTo.dateTime().currentDateTime())



    def onBuscarButtonClicked(self):

        categorias = ['Classificação:', 'Tipo:', 'Cidade:', 'Estado:', 'Aeródromo:', 'Turno do Dia:', 'Status Investigativo:',
             'Tipo de Veículo:', 'Fabricante:', 'Modelo:', 'Quantidade de Motores:', 'Classe:', 'Dano:',
             'Presença de Fatalidades:']
        l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin',
              'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin',
              'fatalities.bin']
        dictionaryFiles = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin',
              'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin',
              'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']


        IDs = set()

        strIDParcial = self.textCodigo.displayText()
        #if strIDParcial != "":  #tem ID numerico

        IDs = IDs.union(mainFunctions.filterIDTrie(strIDParcial, 'Trie.bin'))

        for i,v in enumerate(self.menuVariablesOco):
            if v.currentText() != "Qualquer":
                IDs = IDs.intersection(supportFile.getIDs(self.menuVariablesOcoDictBin[i], self.menuVariablesOcoBin[i], v.currentText()))

        textinvest = self.butgroupInvestigacao.checkedButton().text().upper()
        if textinvest != 'QUALQUER':
            IDs = IDs.intersection(supportFile.getIDs('dicInvStatus.bin', 'invStatus.bin', textinvest))

        for i,v in enumerate(self.menuVariablesAero):
            if v.currentText() != "Qualquer":
                IDs = IDs.intersection(supportFile.getIDs(self.menuVariablesAeroDictBin[i], self.menuVariablesAeroBin[i], v.currentText()))

        textfatal = self.butgroupFatalidades.checkedButton().text().upper()
        if textfatal == "FATAL":
            IDs = IDs.intersection(supportFile.getIDs('dicFatalities.bin', 'fatalities.bin', "SIM"))
        elif textfatal == "NÃO FATAL":
            IDs = IDs.intersection(supportFile.getIDs('dicFatalities.bin', 'fatalities.bin', "NÃO"))

        startdate = datetime.datetime.combine(self.dateTimeFrom.date().toPyDate(), self.dateTimeFrom.time().toPyTime())
        enddate = datetime.datetime.combine(self.dateTimeTo.date().toPyDate(), self.dateTimeTo.time().toPyTime())

        # ID, Classificacao, TipoOco, Cidade, UF, Aerodromo, Dia e Hora, Turno do Dia, Invest Status, # Aeronaves
        listaIndicesOco = [0, 1, 2, 5, 6, 8, "dh", "turno", 12, 17]

        dictionaryFiles = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin',
                           'dicDayShift.bin',
                           'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin',
                           'dicQtyEngine.bin',
                           'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']
        listaIndicesRankOco = [1,2,5,6,8]


        #da um clear na table anterior
        self.tableResultadosOco.setSortingEnabled(False)  # evita bug esquisito que mantem row vazias se estiver sorted
        for x in reversed(range(self.tableResultadosOco.rowCount())):
            self.tableResultadosOco.removeRow(x)
        #self.tableResultadosOco.setRowCount(0)
        IDkeepers = []
        ranksOco = []
        sortedOptionsOco = []
        for dicfile in dictionaryFiles[0:7]:
            sortedOptionsOco.append(supportFile.returnSorted(dicfile))
            ranksOco.append([0]*len(sortedOptionsOco[-1]))

        for id in IDs:

            dados = mainFunctions.getInfoID(id, 'Trie.bin')

            date = dados[0][9]
            time = dados[0][10]

            #print(date)
            #print(time)

            datatempo = datetime.datetime.combine(datetime.date(int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2]) ),
                                                  datetime.time(int(time.split(":")[0]), int(time.split(":")[1]), int(time.split(":")[2]) ))
            if startdate <= datatempo <= enddate:
                IDkeepers.append(id)

                dh = date + " " + time
                horahora = int(time.split(":")[0])
                if horahora >= 18:
                    turno = "NOITE"
                elif horahora >= 12:
                    turno = "TARDE"
                elif horahora >= 6:
                    turno = "MANHÃ"
                else:
                    turno = "MADRUGADA"

                # ID, Classificacao, TipoOco, Cidade, UF, Aerodromo, Dia e Hora, Turno do Dia, Invest Status, # Aeronaves
                #listaIndicesOco = [0, 1, 2, 5, 6, 8, "dh", "turno", 12, 17]
                #Rankings Oco

                for i in range(5):
                    for k,item in enumerate(sortedOptionsOco[i]):
                        if dados[0][ listaIndicesRankOco[i]] == item:
                            ranksOco[i][k] += 1
                            break

                for k,item in enumerate(sortedOptionsOco[5]):
                    if turno == item:
                        ranksOco[5][k] +=1
                        break

                for k, item in enumerate(sortedOptionsOco[6]):
                    if dados[0][ 12 ] == item: # indice Status investig
                        ranksOco[6][k] += 1
                        break



                #rankOcoClassif = [0]*self.dropClassificacao.count()
                #for i in range()
                #    if dados[0][1] ==

                #Tabela Oco
                rowPosition = self.tableResultadosOco.rowCount()
                self.tableResultadosOco.insertRow(rowPosition)
                for i, j in enumerate(listaIndicesOco):
                    if j != "dh" and j != "turno":
                        self.tableResultadosOco.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dados[0][j]))
                    elif j == "dh":

                        self.tableResultadosOco.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dh))
                        i += 1
                        self.tableResultadosOco.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(turno))


        self.tableResultadosOco.setSortingEnabled(True)
        self.tableResultadosOco.sortItems(0, QtCore.Qt.AscendingOrder)

        textao = ""
        textao += "Dados de Ocorrência:\n\n"

        total = len(IDkeepers)

        if total == 0:
            textao = "Sem resultados de ocorrência"
        else:

            for i, catigoria in enumerate(categorias[0:7]):
                textao += '\n{}:\n'.format(catigoria)

                argindices = numpy.argsort(ranksOco[i])[::-1]
                if len(argindices) <= 10:
                    for indice in argindices:
                        textao += '{} {} ({:.2f}%)\n'.format((sortedOptionsOco[i][indice]+':').ljust(80), ranksOco[i][indice], ranksOco[i][indice]*100/total)
                else:
                    for indice in argindices[:10]:
                        textao += '{} {} ({:.2f}%)\n'.format((sortedOptionsOco[i][indice]+':').ljust(80), ranksOco[i][indice], ranksOco[i][indice]*100/total)



        IDs = IDkeepers
        ranksAero = []
        sortedOptionsAero = []
        for dicfile in dictionaryFiles[7:]:
            sortedOptionsAero.append(supportFile.returnSorted(dicfile))
            ranksAero.append([0] * len(sortedOptionsAero[-1]))


        ## TABLE AERONAVES
        # ID, TipoAero, Fabricante, Modelo, Qtd Motores, Classe, Dano, Fatalidades
        listaIndicesAero = [0, 3,4,5,8, 10, 21,22]

        # clearzera
        self.tableResultadosAero.setSortingEnabled(False)  # evita bug esquisito que mantem row vazias se estiver sorted
        for x in reversed(range(self.tableResultadosAero.rowCount())):
            self.tableResultadosAero.removeRow(x)

        totalAero = 0

        # self.menuVariablesAero = [self.dropTipoAeronave, self.dropFabricante, self.dropModelo, self.dropQtdMotores, self.dropCategoriaPeso, self.dropDano]
        #

        for id in IDs:
            dados = mainFunctions.getInfoID(id, 'Trie.bin')
            if len(dados) == 2:

                # continua insercao e catalogo
                totalAero += 1

                # ID, TipoAero, Fabricante, Modelo, Qtd Motores, Classe, Dano, Fatalidades
                # listaIndicesAero = [0, 3, 4, 5, 8, 10, 21, 22]

                # Rank aero

                for i in range(6):
                    for j, item in enumerate(sortedOptionsAero[i]):
                        if dados[1][listaIndicesAero[i + 1]] == item:
                            ranksAero[i][j] += 1
                            break

                # fatalidade sim ou nao
                for j, item in enumerate(sortedOptionsAero[6]):
                    if (dados[1][22] not in ['***', '0']) and item == "SIM":
                        ranksAero[6][j] += 1
                        break
                    elif (dados[1][22] in ['***', '0']) and item == "NÃO":
                        ranksAero[6][j] += 1
                        break

                rowPosition = self.tableResultadosAero.rowCount()
                self.tableResultadosAero.insertRow(rowPosition)
                for i, j in enumerate(listaIndicesAero):
                    self.tableResultadosAero.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dados[1][j]))
            elif len(dados) > 2:
                for k in range(1,len(dados)):

                    itemOk = True
                    for i, v in enumerate(self.menuVariablesAero):

                        if v.currentText().upper() not in ["QUALQUER"]:
                            if dados[k][listaIndicesAero[i+1]] != v.currentText().upper():
                                itemOk = False
                                break

                    if self.butgroupFatalidades.checkedButton().text().upper() != "QUALQUER":
                        if dados[k][22] != self.butgroupFatalidades.checkedButton().text().upper():
                            itemOk = False

                    if itemOk:

                        #continua insercao e catalogo
                        totalAero += 1

                        # ID, TipoAero, Fabricante, Modelo, Qtd Motores, Classe, Dano, Fatalidades
                        #listaIndicesAero = [0, 3, 4, 5, 8, 10, 21, 22]

                        #Rank aero

                        for i in range(6):
                            for j, item in enumerate(sortedOptionsAero[i]):
                                if dados[k][listaIndicesAero[i+1]] == item:
                                    ranksAero[i][j] += 1
                                    break

                        # fatalidade sim ou nao
                        for j, item in enumerate(sortedOptionsAero[6]):
                            if (dados[k][22] not in ['***', '0']) and item == "SIM":
                                ranksAero[6][j] += 1
                                break
                            elif (dados[k][22] in ['***', '0']) and item == "NÃO":
                                ranksAero[6][j] += 1
                                break


                        rowPosition = self.tableResultadosAero.rowCount()
                        self.tableResultadosAero.insertRow(rowPosition)
                        for i, j in enumerate(listaIndicesAero):
                            self.tableResultadosAero.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dados[k][j]))
            # ignora se nao tem aeronave inscrita


        self.tableResultadosAero.setSortingEnabled(True)
        self.tableResultadosAero.sortItems(0, QtCore.Qt.AscendingOrder)

        if totalAero > 0:

            textao += "\n\nDados de Aeronaves:\n"
            for i, catigoria in enumerate(categorias[7:]):
                textao += '\n{}:\n'.format(catigoria)

                argindices = numpy.argsort(ranksAero[i])[::-1]

                if len(argindices) <= 10:
                    for indice in argindices:
                        textao += '{} {} ({:.2f}%)\n'.format((sortedOptionsAero[i][indice]+':').ljust(80), ranksAero[i][indice], ranksAero[i][indice]*100/totalAero)
                else:
                    for indice in argindices[:10]:
                        textao += '{} {} ({:.2f}%)\n'.format((sortedOptionsAero[i][indice]+':').ljust(80), ranksAero[i][indice], ranksAero[i][indice]*100/totalAero)

        else:
            textao += "\nSem resultados de aeronave.\n"


        print(textao)
        self.rankingBox.setPlainText(textao)



    def initializeInsereRemoveTab(self):

        self.regexNum35 = QtCore.QRegExp("[0-9]\\d{0,34}")
        self.only35Digits = QtGui.QRegExpValidator(self.regexNum35)
        self.toc0CodOco.setValidator(self.only35Digits)
        self.tae0CodOco.setValidator(self.only35Digits)


        self.regexNum6 = QtCore.QRegExp("[0-9]\\d{0,5}")
        self.only6Digits = QtGui.QRegExpValidator(self.regexNum6)
        self.tae9PesoMax.setValidator(self.only6Digits)
        self.tae11NumAssentos.setValidator(self.only6Digits)
        self.tae22Fatalidades.setValidator(self.only6Digits)
        self.toc16Recomend.setValidator(self.only6Digits)



        self.regexAlpha35 = QtCore.QRegExp("[^\W\d_]\\{0,34}")
        self.only35Alpha = QtGui.QRegExpValidator(self.regexAlpha35)
        #self.toc5CidadeOco.setValidator(self.only35Alpha)
        #self.tae8QtdMotores.setValidator(self.only35Alpha)
        #self.tae13PaisFabric.setValidator(self.only35Alpha)
        #self.tae14PaisRegistro.setValidator(self.only35Alpha)

        #self.textRegAero = [self.tae0CodOco, self.tae1Matricula, self.tae2CategOperador,
        #                    self.tae3TipoAero, self.tae4Fabricante, self.tae5Modelo, self.tae6TipoICAO,
        #                    self.tae7TipoMotor, self.tae8QtdMotores, self.tae9PesoMax, self.tae11NumAssentos,
        #                    self.tae13PaisFabric, self.tae14PaisRegistro, self.tae15RegCategoria, self.tae16RegSegmento,
        #                    self.tae17VooOrigem, self.tae18VooDestino, self.tae19FaseOperacao, self.tae20TipoOperacao,
        #                    self.tae22Fatalidades]

        for v in self.textRegOco:
            v.setClearButtonEnabled(True)


        #self.textRegOco = [self.toc0CodOco, self.toc2TipoOco, self.toc3LatitudeOco, self.toc4LongitudeOco,
        #                   self.toc5CidadeOco, self.toc8AerodromeOco, self.toc13NumRelatOco, self.toc16Recomend]

        for v in self.textRegAero:
            v.setClearButtonEnabled(True)


        self.coc14RelatPublOco.stateChanged.connect(self.onRelatorioPublicadoChanged)
        self.coc15TemDataRelat.stateChanged.connect(self.onTemDataRelatorioChanged)

        self.limparRegOco.clicked.connect(self.onLimparRegOcoClicked)
        self.limparRegAero.clicked.connect(self.onLimparRegAeroClicked)
        self.registrarRegOco.clicked.connect(self.onRegistrarRegOcoClicked)
        self.registrarRegAero.clicked.connect(self.onRegistrarRegAeroClicked)
        self.removerRegOco.clicked.connect(self.onRemoverRegOcoClicked)

        self.toc13NumRelatOco.setText("")
        self.toc13NumRelatOco.setEnabled(False)
        self.dtoc15DataPublicRelat.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dtoc15DataPublicRelat.setEnabled(False)
        self.coc15TemDataRelat.setChecked(False)
        self.groupBoxPublicacao.setEnabled(False)

        self.coc15TemDataRelat.setChecked(False)
        self.coc14RelatPublOco.setChecked(False)


    def onRemoverRegOcoClicked(self):

        # Checar se ID ja existe
        id = self.toc0CodOco.displayText()
        dados = mainFunctions.getInfoID(id, 'Trie.bin')

        if id == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)

            msg.setWindowTitle("Campo Obrigatório Vazio")
            msg.setText("Preencha o código identificador da ocorrência.\n")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            msg.exec()
            return

        if dados != -1:  # se não retornou -1, então já existe.

            yn = QtWidgets.QMessageBox.question(self, 'Deletar Ocorrência?',

                                                "Deseja deletar os dados de ocorrência e de aeronaves associados ao código ID informado?\n"
                                                "(NOTA: Esta ação é irreversível! Os dados correntes serão permanentemente descartados)",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if yn == QtWidgets.QMessageBox.No:
                pass
            else:
                retornoRem = mainFunctions.removeData(id, 'Trie.bin')
                if retornoRem == -1:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)

                    msg.setWindowTitle("Erro de remoção")
                    msg.setText("Não foi possível deletar o registro da ocorrência especificada no banco de dados.\n")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    msg.exec()
                    return
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)

                    msg.setWindowTitle("Remoção bem sucedida")
                    msg.setText("Registro de ocorrência deletado com sucesso.\n")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    msg.exec()
                    return


        else:  # nao existe essa ID;
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)

            msg.setWindowTitle("Ocorrência não encontrada")
            msg.setText("Não existe ocorrência com o código ID informado no banco de dados.\n")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            msg.exec()
            return




    def onTemDataRelatorioChanged(self):

        if self.coc15TemDataRelat.isChecked():

            self.dtoc15DataPublicRelat.setEnabled(True)
        else:
            self.dtoc15DataPublicRelat.setDateTime(QtCore.QDateTime.currentDateTime())
            self.dtoc15DataPublicRelat.setEnabled(False)

    def onRelatorioPublicadoChanged(self):

        if self.coc14RelatPublOco.isChecked():

            self.toc13NumRelatOco.setEnabled(True)
            self.groupBoxPublicacao.setEnabled(True)

        else:
            self.toc13NumRelatOco.setText("")
            self.toc13NumRelatOco.setEnabled(False)
            self.coc15TemDataRelat.setChecked(False)
            self.groupBoxPublicacao.setEnabled(False)


    def onRegistrarRegOcoClicked(self):

        # Mandou registrar os dados em Ocorrencia
        # Checar se ID ja existe
        id = self.toc0CodOco.displayText()
        dados = mainFunctions.getInfoID(id, 'Trie.bin')

        if id == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)

            msg.setWindowTitle("Campo Obrigatório Vazio")
            msg.setText("Preencha o código identificador da ocorrência.\n")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            msg.exec()
            return

        if dados != -1:  # se não retornou -1, então já existe.

            yn = QtWidgets.QMessageBox.question(self, 'Atualizar Dados?',
                                                "Já existe registro para o código identificador especificado.\n"
                                                "Deseja sobrescrevê-lo com os novos dados informados?\n"
                                                "(NOTA: Esta ação é irreversível! Os dados correntes serão permanentemente descartados)",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if yn == QtWidgets.QMessageBox.No:
                pass
            else:
                self.dadosOcoLista, self.dadosOcoStringFinal = self.novaStringOcorrencia()

                ret = mainFunctions.updateOcoWithDataString(id,'Trie.bin', self.dadosOcoLista)
                if ret == -1:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)

                    msg.setWindowTitle("Erro de atualização")
                    msg.setText("Não foi possível atualizar o registro da ocorrência especificada no banco de dados.\n")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    msg.exec()
                    return
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)

                    msg.setWindowTitle("Atualização bem sucedida")
                    msg.setText("Registro de ocorrência atualizado com sucesso.\n")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    msg.exec()
                    return

        else: # nao existe essa ID; fazer uma nova sem perguntas
            self.dadosOcoLista, self.dadosOcoStringFinal = self.novaStringOcorrencia()
            ret = mainFunctions.addOcoData(self.dadosOcoLista,'Trie.bin')

            if ret == -1:

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)

                msg.setWindowTitle("Erro de inserção")
                msg.setText("Não foi possível inserir a nova ocorrência no banco de dados.\n")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                msg.exec()
                return

            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)

                msg.setWindowTitle("Inserção bem-sucedida")
                msg.setText("Nova ocorrência registrada com sucesso.\n")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                msg.exec()


    def onRegistrarRegAeroClicked(self):

        # Mandou registrar os dados em Aeronave
        # Checar se ID e Matricula de Aeronave ja existem nos registros
        id = self.tae0CodOco.displayText()
        matr = self.tae1Matricula.displayText().upper()
        dados = mainFunctions.getInfoID(id, 'Trie.bin')

        if id == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)

            msg.setWindowTitle("Campo Obrigatório Vazio")
            msg.setText("Preencha o código identificador da ocorrência associada à aeronave.\n")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            msg.exec()
            return
        elif matr == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)

            msg.setWindowTitle("Campo Obrigatório Vazio")
            msg.setText("Preencha a matrícula de identificação da aeronave.\n")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            msg.exec()
            return

        if dados != -1:  # se não retornou -1, então já existe ocorrencia. Checar se existe matricula
            achouIndex = -1
            for i in range(1,len(dados)):
                if dados[i][1] == matr:
                    achouIndex = i

            if achouIndex != -1: # achou aeronave com mesmo ID de ocorrencia e mesma matricula. Alterar?
                yn = QtWidgets.QMessageBox.question(self, 'Atualizar Dados?',
                                                    "Já existe registro para a ocorrência e aeronave com o código e matrícula especificados.\n"
                                                    "Deseja sobrescrevê-lo com os novos dados informados?\n"
                                                    "(NOTA: Esta ação é irreversível! Os dados correntes serão permanentemente descartados)",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if yn == QtWidgets.QMessageBox.No:
                    pass
                else:
                    self.dadosAeroLista, self.dadosAeroStringFinal = self.novaStringAeronave()
                    ret = mainFunctions.updateAnvWithDataString(id, matr, 'Trie.bin', self.dadosAeroLista)
                    if ret == -1:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)

                        msg.setWindowTitle("Erro de atualização")
                        msg.setText("Não foi possível atualizar os dados da aeronave especificada no banco de dados.\n")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                        msg.exec()
                        return
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)

                        msg.setWindowTitle("Atualização bem sucedida")
                        msg.setText("Registro de aeronave atualizado com sucesso.\n")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                        msg.exec()
                        return


            else: #nao achou esta aeronave registrada para este ID. Inserir sem perguntas
                self.dadosAeroLista, self.dadosAeroStringFinal = self.novaStringAeronave()
                ret = mainFunctions.addAeroData([self.dadosAeroLista], 'Trie.bin')

                if ret == -1:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)

                    msg.setWindowTitle("Erro de inserção")
                    msg.setText("Não foi possível inserir o novo registro de aeronave no banco de dados.\n")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    msg.exec()
                    return
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)

                    msg.setWindowTitle("Inserção bem sucedida")
                    msg.setText("Novo registro de aeronave inserido com sucesso.\n")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                    msg.exec()
                    return

        else:  # nao existe essa ID; não pode registrar aeronave ainda
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)

            msg.setWindowTitle("404 - ID Not Found")
            msg.setText("ID não encontrado.\n\nÉ necessário registrar a ocorrência antes de acrescentar dados de aeronaves envolvidas ao banco de dados.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            msg.exec()


    def novaStringOcorrencia(self):

        #self.textRegOco = [self.toc0CodOco, self.toc2TipoOco, self.toc3LatitudeOco, self.toc4LongitudeOco,
        #                   self.toc5CidadeOco, self.toc8AerodromeOco, self.toc13NumRelatOco, self.toc16Recomend]

        sep = '"~"'
        empty = '***'
        stringElements = []

        stringElements.append(self.toc0CodOco.displayText())   #0

        stringElements.append(self.doc1Classif.currentText().upper())

        for i in range(1,5): #2,3,4,5
            input = self.textRegOco[i].displayText()
            if input == "":
                stringElements.append(empty)
            else:
                stringElements.append(self.textRegOco[i].displayText().upper())

        stringElements.append(self.doc6EstadoOco.currentText()) #6
        stringElements.append('BRASIL') #7

        if self.toc8AerodromeOco.displayText() == "":  #8
            stringElements.append(empty)
        else:
            stringElements.append(self.toc8AerodromeOco.displayText().upper())

        dia = self.dtoc910DataHoraOco.date().toPyDate()
        hora = self.dtoc910DataHoraOco.time().toPyTime()
        stringElements.append(str(dia)) # 9
        stringElements.append(str(hora)) #10
        stringElements.append('NULL') #11

        if self.coc12StatusInvestOco.isChecked(): #12
            stringElements.append('ATIVA')
        else:
            stringElements.append('FINALIZADA')

        if self.coc14RelatPublOco.isChecked():
            #SIM para relatorio. Checa se tem codigo de relatorio:
            if self.toc13NumRelatOco == "":
                stringElements.append('A DEFINIR') #13
            else:
                stringElements.append(self.toc13NumRelatOco.displayText().upper()) #13

            stringElements.append('SIM') #14

        else:
            stringElements.append(empty)#13
            stringElements.append('NÃO')#14

        if self.coc15TemDataRelat.isChecked():
            stringElements.append(str(self.dtoc15DataPublicRelat.date().toPyDate())) #15
        else:
            stringElements.append('NULL') #15

        stringElements.append(self.toc16Recomend.displayText())
        stringElements.append(str(self.soc17NumAeronavesEnv.value()))

        if self.coc18SaidaPistaOco.isChecked():
            stringElements.append('SIM')
        else:
            stringElements.append('NÃO')

        stringElements.append(str(QtCore.QDate.currentDate().toPyDate()))
        stringFinal = sep.join(stringElements)

        return( stringElements, stringFinal)

        # codigo_ocorrencia"~"ocorrencia_classificacao"~"ocorrencia_tipo"~"ocorrencia_latitude"~"ocorrencia_longitude"~
        # "ocorrencia_cidade"~"ocorrencia_uf"~"ocorrencia_pais"~"ocorrencia_aerodromo"~"ocorrencia_dia"~"ocorrencia_horario"~
        # "investigacao_aeronave_liberada"~"investigacao_status"~"divulgacao_relatorio_numero"~"divulgacao_relatorio_publicado"~
        # "divulgacao_dia_publicacao"~"total_recomendacoes"~"total_aeronaves_envolvidas"~"ocorrencia_saida_pista"~
        # "ocorrencia_dia_extracao

    def novaStringAeronave(self):

        # self.textRegAero = [self.tae0CodOco, self.tae1Matricula, self.tae2CategOperador,
        #                    self.tae3TipoAero, self.tae4Fabricante, self.tae5Modelo, self.tae6TipoICAO,
        #                    self.tae7TipoMotor, self.tae8QtdMotores, self.tae9PesoMax, self.tae11NumAssentos,
        #                    self.tae13PaisFabric, self.tae14PaisRegistro, self.tae15RegCategoria, self.tae16RegSegmento,
        #                    self.tae17VooOrigem, self.tae18VooDestino, self.tae19FaseOperacao, self.tae20TipoOperacao,
        #                    self.tae22Fatalidades]

        sep = '"~"'
        empty = '***'
        stringElements = []

        for i in range(10):
            textinput = self.textRegAero[i].displayText().upper()
            if textinput == "":
                stringElements.append(empty)
            else:
                stringElements.append(textinput)

        #10, 11, 12
        stringElements.append(self.dae10CategPesoMax.currentText().upper())
        stringElements.append(self.tae11NumAssentos.displayText())
        stringElements.append(str(self.dt12AnoFabric.date().year()))

        for i in range(11,19):
            textinput = self.textRegAero[i].displayText().upper()
            if textinput == "":
                stringElements.append(empty)
            else:
                stringElements.append(textinput)

        stringElements.append(self.dae21DanoAeronave.currentText().upper())
        stringElements.append(self.tae22Fatalidades.displayText())
        stringElements.append(str(QtCore.QDate.currentDate().toPyDate()))

        stringFinal = sep.join(stringElements)
        return (stringElements, stringFinal)

        #codigo_ocorrencia"~"aeronave_matricula"~"aeronave_operador_categoria"~"aeronave_tipo_veiculo"~
        # "aeronave_fabricante"~"aeronave_modelo"~"aeronave_tipo_icao"~"aeronave_motor_tipo"~
        # "aeronave_motor_quantidade"~"aeronave_pmd"~"aeronave_pmd_categoria"~"aeronave_assentos"~
        # "aeronave_ano_fabricacao"~"aeronave_pais_fabricante"~"aeronave_pais_registro"~"aeronave_registro_categoria"~
        # "aeronave_registro_segmento"~"aeronave_voo_origem"~"aeronave_voo_destino"~
        # "aeronave_fase_operacao"~"aeronave_tipo_operacao"~"aeronave_nivel_dano"~
        # "total_fatalidades"~"aeronave_dia_extracao

    def onLimparRegOcoClicked(self):

        for v in self.textRegOco:
            v.setText("")

        self.doc6EstadoOco.setCurrentIndex(0)
        self.soc17NumAeronavesEnv.setValue(1)

        self.coc12StatusInvestOco.setChecked(False)
        self.coc14RelatPublOco.setChecked(False)
        self.coc15TemDataRelat.setChecked(False)
        self.coc18SaidaPistaOco.setChecked(False)

        self.doc1Classif.setCurrentIndex(0)

        self.dtoc15DataPublicRelat.setDateTime(self.dtoc15DataPublicRelat.dateTime().currentDateTime())
        self.dtoc910DataHoraOco.setDateTime(self.dtoc910DataHoraOco.dateTime().currentDateTime())


    def onLimparRegAeroClicked(self):
        for v in self.textRegAero:
            v.setText("")

        self.dt12AnoFabric.setDate(QtCore.QDate(2000,1,1))
        self.dae10CategPesoMax.setCurrentIndex(0)
        self.dae21DanoAeronave.setCurrentIndex(0)



    def shutDown(self):

        yn = QtWidgets.QMessageBox.question(self, 'Sair',
        "Deseja mesmo sair do airsort?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if yn == QtWidgets.QMessageBox.Yes:
            print("Shutting down :<")
            sys.exit()
        else:
            pass

    def aboutWindow(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setWindowTitle("Sobre airsort")
        msg.setText("airsort, Inc. 2017-2018\nInstituto de Informatica, UFRGS\n")
        msg.setInformativeText("Arthur Balbao\nGiovane Fonseca\nGiovanna Miotto")

        #msg.setDetailedText("Arthur Balbao\nGiovane Fonseca\nGiovanna Miotto")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # msg.buttonClicked.connect(msgbtn)

        msg.exec()




def main():
    app = QtWidgets.QApplication(sys.argv)  # nova app

    # traducao de standard messages para a lingua local
    translator = QtCore.QTranslator(app)
    localeQT = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load('qtbase_%s' % localeQT, path)
    app.installTranslator(translator)

    # dark~~~ stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


    form = MainWIndow()

    #override the overrides ^^
    view = QtWidgets.QListView()  # create a ListView
    view.setFixedWidth(450)  # set the ListView with fixed Width
    #form.dropTipoOcorrencia.setView(view)  # provide the list view to Combobox object
    form.dropFabricante.setView(view)
    #form.dropTipoOcorrencia.setFixedHeight(24)
    #form.dropTipoOcorrencia.setFixedWidth(271)
    form.doc1Classif.setFixedHeight(24)
    form.doc1Classif.setFixedWidth(133)
    form.dae21DanoAeronave.setFixedHeight(24)
    form.dae21DanoAeronave.setFixedWidth(113)
    form.dae10CategPesoMax.setFixedHeight(24)
    form.dae10CategPesoMax.setFixedWidth(113)
    form.dropCidade.setFixedHeight(24)
    form.dropCidade.setFixedWidth(211)


    form.show() # mostra a janelera
    sys.exit(app.exec_())  # executa o app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()
