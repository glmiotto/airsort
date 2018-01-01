import sys
from PyQt5 import QtGui, QtCore, QtWidgets

import airsortUI as design
import qdarkstyle

import supportFile
import mainFunctions

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

        lista1 = supportFile.getIDs('dicModelsByManufacturer.bin', 'modelsByManufacturer.bin', "EMBRAER")
        print("EMBRAER", lista1)
        lista2 = supportFile.getIDs('dicModelsByManufacturer.bin', 'modelsByManufacturer.bin', "CESSNA")
        print("CESSNA", lista2)

        lista1s = sorted(lista1, key=locale.strxfrm)
        print("EMBRAER sorted", lista1s)
        lista2s = sorted(lista2, key=locale.strxfrm)
        print("CESSNA sorted", lista2s)

        print("Consertar: pegando modelos de outras marcas why")

        lll = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin',
         'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin',
         'fatalities.bin']

        self.menuVariablesOco = [self.dropEstado, self.dropCidade, self.dropAerodromo, self.dropTurno, self.dropTipoOcorrencia]
        self.menuVariablesOcoBin = ['UF.bin', 'city.bin', 'aerodrome.bin', 'dayShift.bin', 'type.bin']
        self.menuVariablesOcoDictBin = ['dicUF.bin', 'dicCity.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicType.bin']

        self.menuVariablesAero = [self.dropTipoAeronave, self.dropFabricante, self.dropQtdMotores, self.dropCategoriaPeso]
        self.menuVariablesAeroBin = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin','fatalities.bin']
        self.menuVariablesAeroDictBin = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin','dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']


        listaTipoOco = supportFile.returnSorted('dicType.bin')
        self.dropTipoOcorrencia.addItems(listaTipoOco)

        self.dropClassificacao.addItems(supportFile.returnSorted('dicClassification.bin'))

        listaTurnoDia = supportFile.returnSorted('dicDayShift.bin')
        turnos = ["MADRUGADA", "MANHÃ", "TARDE", "NOITE"] #garante a ordem intuitiva dos turnos (caso nao tenha todos)
        listaTurnoDia = sorted(listaTurnoDia, key=lambda x: turnos.index(x))
        self.dropTurno.addItems(listaTurnoDia)

        listaCatPesos = supportFile.returnSorted('dicClass.bin')
        pesos = ["***", "LEVE", "MÉDIA", "MÉDIO", "PESADA", "PESADO"]  # garante a ordem intuitiva
        listaCatPesos = sorted(listaCatPesos, key=lambda x: pesos.index(x))
        self.dropCategoriaPeso.addItems(listaCatPesos)

        listaTipoAero = supportFile.returnSorted('dicVeicType.bin')
        self.dropTipoAeronave.addItems(listaTipoAero)

        listaDano = supportFile.returnSorted('dicHarm.bin')
        damages = ["***", "NENHUM", "LEVE", "SUBSTANCIAL", "DESTRUÍDA", "DESTRUÍDO"]
        listaDano = sorted(listaDano, key=lambda x: damages.index(x))
        self.dropDano.addItems(listaDano)



        #listaAerodromo = supportFile.returnSorted('dicAerodrome.bin')
        #self.dropAerodromo.addItems(listaAerodromo)

        listaQtdMotores = supportFile.returnSorted('dicQtyEngine.bin')
        motors = ["***", "SEM TRAÇÃO", "MONOMOTOR", "BIMOTOR", "TRIMOTOR", "QUADRIMOTOR"]  # garante a ordem intuitiva
        listaQtdMotores = sorted(listaQtdMotores, key=lambda x: motors.index(x))
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

        # Reseta calendário FROM para seu mínimo e o TO para a data atual no sistema do usuário
        self.dateTimeFrom.setDateTime(self.dateTimeFrom.minimumDateTime())
        self.dateTimeTo.setDateTime(self.dateTimeTo.dateTime().currentDateTime())



    def onBuscarButtonClicked(self):

        l = ['Classificação:', 'Tipo:', 'Cidade:', 'Estado:', 'Aeródromo:', 'Turno do Dia:', 'Status Investigativo:',
             'Tipo de Veículo:', 'Fabricante:', 'Modelo:', 'Quantidade de Motores:', 'Classe:', 'Dano:',
             'Presença de Fatalidades:']
        l1 = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin',
              'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin',
              'fatalities.bin']
        l2 = ['dicClassification.bin', 'dicType.bin', 'dicCity.bin', 'dicUF.bin', 'dicAerodrome.bin', 'dicDayShift.bin',
              'dicInvStatus.bin', 'dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin',
              'dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']


        IDs = set()

        strIDParcial = self.textCodigo.displayText()
        #if strIDParcial != "":  #tem ID numerico

        IDs = IDs.union(mainFunctions.filterIDTrie(strIDParcial, 'Trie.bin'))

        for i,v in enumerate(self.menuVariablesOco):
            if v.currentText() != "Qualquer":
                IDs = IDs.intersection(supportFile.getIDs(self.menuVariablesOcoDictBin[i], self.menuVariablesOcoBin[i], v.currentText()))


        startdate = datetime.datetime.combine(self.dateTimeFrom.date().toPyDate(), self.dateTimeFrom.time().toPyTime())
        enddate = datetime.datetime.combine(self.dateTimeTo.date().toPyDate(), self.dateTimeTo.time().toPyTime())

        # ID, Classificacao, TipoOco, Cidade, UF, Aerodromo, Dia e Hora, Turno do Dia, Invest Status, # Aeronaves
        listaIndicesOco = [0, 1, 2, 5, 6, 8, "dh", "turno", 12, 17]


        #da um clear na table anterior
        self.tableResultadosOco.setSortingEnabled(False)  # evita bug esquisito que mantem row vazias se estiver sorted
        for x in reversed(range(self.tableResultadosOco.rowCount())):
            self.tableResultadosOco.removeRow(x)
        #self.tableResultadosOco.setRowCount(0)

        IDkeepers = []
        for id in IDs:

            dados = mainFunctions.getInfoID(id, 'Trie.bin')
            #if id == "201604251335501":
            #    print(dados)

            date = dados[0][9]
            time = dados[0][10]
            #print(date)
            #print(time)

            datatempo = datetime.datetime.combine(datetime.date(int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2]) ),
                                                  datetime.time(int(time.split(":")[0]), int(time.split(":")[1]), int(time.split(":")[2]) ))
            #print("combinou")
            if startdate <= datatempo <= enddate:
                #print("comparou")
                IDkeepers.append(id)
                rowPosition = self.tableResultadosOco.rowCount()
                self.tableResultadosOco.insertRow(rowPosition)
                for i, j in enumerate(listaIndicesOco):
                    if j != "dh" and j != "turno":
                        self.tableResultadosOco.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dados[0][j]))
                    elif j == "dh":
                        dia = dados[0][9]
                        hora = dados[0][10]
                        dh = dia + " " + hora
                        horahora = int(hora.split(":")[0])
                        if horahora >= 18:
                            turno = "NOITE"
                        elif horahora >= 12:
                            turno = "TARDE"
                        elif horahora >= 6:
                            turno = "MANHÃ"
                        else:
                            turno = "MADRUGADA"
                        self.tableResultadosOco.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dh))
                        i += 1
                        self.tableResultadosOco.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(turno))


        self.tableResultadosOco.setSortingEnabled(True)
        self.tableResultadosOco.sortItems(0, QtCore.Qt.AscendingOrder)

        IDs = IDkeepers

        ## TABLE AERONAVES
        # ID, TipoAero, Fabricante, Modelo, Qtd Motores, Classe, Dano, Fatalidades
        listaIndicesAero = [0, 3,4,5,8, 10, 21,22]

        # clearzera
        self.tableResultadosAero.setSortingEnabled(False)  # evita bug esquisito que mantem row vazias se estiver sorted
        for x in reversed(range(self.tableResultadosAero.rowCount())):
            self.tableResultadosAero.removeRow(x)

        for id in IDs:
            dados = mainFunctions.getInfoID(id, 'Trie.bin')
            if len(dados) == 2:
                rowPosition = self.tableResultadosAero.rowCount()
                self.tableResultadosAero.insertRow(rowPosition)
                for i, j in enumerate(listaIndicesAero):
                    self.tableResultadosAero.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dados[1][j]))
            elif len(dados) > 2:
                for k in range(1,len(dados)):
                    rowPosition = self.tableResultadosAero.rowCount()
                    self.tableResultadosAero.insertRow(rowPosition)
                    for i, j in enumerate(listaIndicesAero):
                        self.tableResultadosAero.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(dados[k][j]))
            # ignora se nao tem aeronave inscrita

        self.tableResultadosAero.setSortingEnabled(True)
        self.tableResultadosAero.sortItems(0, QtCore.Qt.AscendingOrder)



        print(self.classifButtonGroup.checkedButton().text())


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

        self.toc13NumRelatOco.setText("")
        self.toc13NumRelatOco.setEnabled(False)
        self.dtoc15DataPublicRelat.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dtoc15DataPublicRelat.setEnabled(False)
        self.coc15TemDataRelat.setChecked(False)
        self.groupBoxPublicacao.setEnabled(False)

        self.coc15TemDataRelat.setChecked(False)
        self.coc14RelatPublOco.setChecked(False)


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
                registro = self.novaStringOcorrencia()

        else: # nao existe essa ID; fazer uma nova sem perguntas
            registro = self.novaStringOcorrencia()



    def onRegistrarRegAeroClicked(self):

        # Mandou registrar os dados em Aeronave
        # Checar se ID e Matricula de Aeronave ja existem nos registros
        id = self.tae0CodOco.displayText()
        matr = self.tae1Matricula.displayText()
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
                    registro = self.novaStringAeronave()

            else: #nao achou esta aeronave registrada para este ID. Inserir sem perguntas
                registro = self.novaStringAeronave()



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

        print(stringFinal)

        return(stringFinal)

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
        print(stringFinal)
        return (stringFinal)

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
