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

        lll = ['classification.bin', 'type.bin', 'city.bin', 'UF.bin', 'aerodrome.bin', 'dayShift.bin', 'invStatus.bin',
         'veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin',
         'fatalities.bin']

        self.menuVariablesOco = [self.dropEstado, self.dropCidade, self.dropAerodromo, self.dropTurno, self.dropTipoOco]
        self.menuVariablesOcoBin = ['UF.bin', 'city.bin', 'aerodrome.bin', 'dayShift.bin', 'type.bin']
        self.menuVariablesOcoDictBin = ['dicUF.bin', 'dicCity.bin', 'dicAerodrome.bin', 'dicDayShift.bin', 'dicType.bin']

        self.menuVariablesAero = [self.dropTipoAeronave, self.dropFabricante, self.dropQtdMotores, self.dropCategoriaPeso]
        self.menuVariablesAeroBin = ['veicType.bin', 'manufacturer.bin', 'model.bin', 'qtyEngine.bin', 'class.bin', 'harm.bin','fatalities.bin']
        self.menuVariablesAeroDictBin = ['dicVeicType.bin', 'dicManufacturer.bin', 'dicModel.bin', 'dicQtyEngine.bin','dicClass.bin', 'dicHarm.bin', 'dicFatalities.bin']

        listaTipoOco = supportFile.returnSorted('dicType.bin')
        self.dropTipoOco.addItems(listaTipoOco)

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

        listaAerodromo = supportFile.returnSorted('dicAerodrome.bin')
        self.dropAerodromo.addItems(listaAerodromo)

        listaQtdMotores = supportFile.returnSorted('dicQtyEngine.bin')
        motors = ["***", "SEM TRAÇÃO", "MONOMOTOR", "BIMOTOR", "TRIMOTOR", "QUADRIMOTOR"]  # garante a ordem intuitiva
        listaQtdMotores = sorted(listaQtdMotores, key=lambda x: motors.index(x))
        self.dropQtdMotores.addItems(listaQtdMotores)

        listaUF = supportFile.returnSorted('dicUF.bin')
        self.dropEstado.clear()
        self.dropEstado.addItem('Qualquer')
        self.dropEstado.addItems(listaUF)

        # FAZER UMA FUNC QUE MANIPULA OCO.BIN DIRETAMENTE DEPOIS PQ NÉ
        self.dictCitiesByUF = {}
        for uf in listaUF:
            if uf != "***":
                ufids = supportFile.getIDs('dicUF.bin', 'UF.bin', uf)

                #print("Numero de ids", len(ufids))
                for id in ufids:
                    data = mainFunctions.getInfoID(id, 'Trie.bin')
                    if (uf not in self.dictCitiesByUF) or (data[0][5] not in self.dictCitiesByUF[uf]):
                            self.dictCitiesByUF.setdefault(uf, []).append(data[0][5])
                self.dictCitiesByUF[uf].sort(key=locale.strxfrm) # sort baseado na lingua local (because acentos)


        # se trocar estado, troca a selecao de cidades
        self.dropEstado.currentIndexChanged['QString'].connect(self.onUFSelected)


        # usa regex para validar entradas ao linebox de codigo ID
        # para até 35 digitos numericos (embora tenham 15 - pois podem ser inseridas novas IDs mais longas mais tarde)
        self.regex = QtCore.QRegExp("[0-9]\\d{0,34}")
        self.onlyDigits = QtGui.QRegExpValidator(self.regex)
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



    def onUFSelected(self):

        uf = self.dropEstado.currentText() # Novo dado escolhido em Estado
        if (uf != "***") and (uf != "Qualquer"): # Se for UF válido
            self.dropCidade.clear()
            self.dropCidade.addItem('Qualquer')
            self.dropCidade.addItems(self.dictCitiesByUF[uf])
            self.dropCidade.setEnabled(True) # Pode selecionar
        else: # Se for Qualquer ou ***, presume-se cidade Qualquer
            self.dropCidade.clear()
            self.dropCidade.addItem('Qualquer')
            self.dropCidade.setEnabled(False) # Não pode selecionar, só Qualquer

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

        dt = self.dateTimeTo.date()
        dt = dt.toPyDate()
        print(dt)
        tt = self.dateTimeTo.time()
        tt = tt.toPyTime()
        print(tt)

        df = self.dateTimeFrom.date()
        df = df.toPyDate()
        print(df)
        tf = self.dateTimeFrom.time()
        tf = tf.toPyTime()
        print(tf)

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



    def shutDown(self):

        yn = QtWidgets.QMessageBox.question(self, 'Sair',
        "Deseja sair do airsort?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
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

    #override the override ^^
    view = QtWidgets.QListView()  # create a ListView
    view.setFixedWidth(450)  # set the ListView with fixed Width
    form.dropTipoOco.setView(view)  # provide the list view to Combobox object

    form.show() # mostra a janelera
    sys.exit(app.exec_())  # executa o app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()
