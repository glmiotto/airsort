# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'airUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1254, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.toolBox_6 = QtWidgets.QToolBox(self.tab1)
        self.toolBox_6.setGeometry(QtCore.QRect(10, 20, 1091, 361))
        self.toolBox_6.setObjectName("toolBox_6")
        self.toolBox_6Page1 = QtWidgets.QWidget()
        self.toolBox_6Page1.setObjectName("toolBox_6Page1")
        self.groupBox_7 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_7.setGeometry(QtCore.QRect(720, -10, 211, 131))
        self.groupBox_7.setMaximumSize(QtCore.QSize(212, 131))
        self.groupBox_7.setAutoFillBackground(False)
        self.groupBox_7.setStyleSheet("")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_11.setObjectName("radioButton_11")
        self.fatalButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.fatalButtonGroup.setObjectName("fatalButtonGroup")
        self.fatalButtonGroup.addButton(self.radioButton_11)
        self.gridLayout_15.addWidget(self.radioButton_11, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_15.addWidget(self.label_6, 0, 0, 1, 1)
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setObjectName("radioButton_12")
        self.fatalButtonGroup.addButton(self.radioButton_12)
        self.gridLayout_15.addWidget(self.radioButton_12, 1, 0, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_13.setObjectName("radioButton_13")
        self.fatalButtonGroup.addButton(self.radioButton_13)
        self.gridLayout_15.addWidget(self.radioButton_13, 3, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_10.setGeometry(QtCore.QRect(490, -10, 211, 131))
        self.groupBox_10.setMaximumSize(QtCore.QSize(212, 131))
        self.groupBox_10.setAutoFillBackground(False)
        self.groupBox_10.setStyleSheet("")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setCheckable(False)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton_5.setObjectName("radioButton_5")
        self.statusButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.statusButtonGroup.setObjectName("statusButtonGroup")
        self.statusButtonGroup.addButton(self.radioButton_5)
        self.gridLayout_18.addWidget(self.radioButton_5, 2, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton_7.setObjectName("radioButton_7")
        self.statusButtonGroup.addButton(self.radioButton_7)
        self.gridLayout_18.addWidget(self.radioButton_7, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_10)
        self.label_9.setObjectName("label_9")
        self.gridLayout_18.addWidget(self.label_9, 0, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.statusButtonGroup.addButton(self.radioButton_6)
        self.gridLayout_18.addWidget(self.radioButton_6, 1, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_11.setGeometry(QtCore.QRect(23, -10, 212, 131))
        self.groupBox_11.setMaximumSize(QtCore.QSize(212, 131))
        self.groupBox_11.setAutoFillBackground(False)
        self.groupBox_11.setStyleSheet("")
        self.groupBox_11.setTitle("")
        self.groupBox_11.setFlat(False)
        self.groupBox_11.setCheckable(False)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_11)
        self.radioButton_4.setObjectName("radioButton_4")
        self.classifButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.classifButtonGroup.setObjectName("classifButtonGroup")
        self.classifButtonGroup.addButton(self.radioButton_4)
        self.gridLayout_19.addWidget(self.radioButton_4, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_11)
        self.label_10.setObjectName("label_10")
        self.gridLayout_19.addWidget(self.label_10, 0, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_11)
        self.radioButton_3.setObjectName("radioButton_3")
        self.classifButtonGroup.addButton(self.radioButton_3)
        self.gridLayout_19.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_11)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.classifButtonGroup.addButton(self.radioButton_2)
        self.gridLayout_19.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_8.setGeometry(QtCore.QRect(23, 110, 121, 91))
        self.groupBox_8.setMaximumSize(QtCore.QSize(212, 91))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_7 = QtWidgets.QLabel(self.groupBox_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_16.addWidget(self.label_7, 0, 0, 1, 1)
        self.dropEstado = QtWidgets.QComboBox(self.groupBox_8)
        self.dropEstado.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropEstado.setObjectName("dropEstado")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.dropEstado.addItem("")
        self.gridLayout_16.addWidget(self.dropEstado, 1, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_9.setGeometry(QtCore.QRect(370, 110, 211, 91))
        self.groupBox_9.setMaximumSize(QtCore.QSize(211, 91))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_8 = QtWidgets.QLabel(self.groupBox_9)
        self.label_8.setObjectName("label_8")
        self.gridLayout_17.addWidget(self.label_8, 0, 0, 1, 1)
        self.dropTurno = QtWidgets.QComboBox(self.groupBox_9)
        self.dropTurno.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropTurno.setObjectName("dropTurno")
        self.dropTurno.addItem("")
        self.gridLayout_17.addWidget(self.dropTurno, 1, 0, 1, 1)
        self.groupBox_17 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_17.setGeometry(QtCore.QRect(590, 110, 300, 91))
        self.groupBox_17.setTitle("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.label_16 = QtWidgets.QLabel(self.groupBox_17)
        self.label_16.setObjectName("label_16")
        self.gridLayout_25.addWidget(self.label_16, 0, 0, 1, 1)
        self.dropTipoOco = QtWidgets.QComboBox(self.groupBox_17)
        self.dropTipoOco.setMinimumSize(QtCore.QSize(0, 0))
        self.dropTipoOco.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropTipoOco.setFrame(True)
        self.dropTipoOco.setObjectName("dropTipoOco")
        self.dropTipoOco.addItem("")
        self.gridLayout_25.addWidget(self.dropTipoOco, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_5.setGeometry(QtCore.QRect(300, 190, 395, 91))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.dateTimeFrom = QtWidgets.QDateTimeEdit(self.groupBox_5)
        self.dateTimeFrom.setGeometry(QtCore.QRect(10, 50, 171, 25))
        self.dateTimeFrom.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeFrom.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeFrom.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateTimeFrom.setCalendarPopup(True)
        self.dateTimeFrom.setObjectName("dateTimeFrom")
        self.dateTimeTo = QtWidgets.QDateTimeEdit(self.groupBox_5)
        self.dateTimeTo.setGeometry(QtCore.QRect(200, 50, 171, 25))
        self.dateTimeTo.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(23, 54, 59)))
        self.dateTimeTo.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeTo.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateTimeTo.setCalendarPopup(True)
        self.dateTimeTo.setObjectName("dateTimeTo")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 173, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_12 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_12.setGeometry(QtCore.QRect(23, 190, 270, 91))
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_11 = QtWidgets.QLabel(self.groupBox_12)
        self.label_11.setObjectName("label_11")
        self.gridLayout_20.addWidget(self.label_11, 0, 0, 1, 1)
        self.textCodigo = QtWidgets.QLineEdit(self.groupBox_12)
        self.textCodigo.setInputMask("")
        self.textCodigo.setText("")
        self.textCodigo.setObjectName("textCodigo")
        self.gridLayout_20.addWidget(self.textCodigo, 1, 0, 1, 1)
        self.groupBox_18 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_18.setGeometry(QtCore.QRect(150, 110, 212, 91))
        self.groupBox_18.setMaximumSize(QtCore.QSize(212, 91))
        self.groupBox_18.setTitle("")
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.label_17 = QtWidgets.QLabel(self.groupBox_18)
        self.label_17.setObjectName("label_17")
        self.gridLayout_26.addWidget(self.label_17, 0, 0, 1, 1)
        self.dropCidade = QtWidgets.QComboBox(self.groupBox_18)
        self.dropCidade.setEnabled(False)
        self.dropCidade.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropCidade.setObjectName("dropCidade")
        self.dropCidade.addItem("")
        self.gridLayout_26.addWidget(self.dropCidade, 1, 0, 1, 1)
        self.groupBox_19 = QtWidgets.QGroupBox(self.toolBox_6Page1)
        self.groupBox_19.setGeometry(QtCore.QRect(250, 10, 212, 91))
        self.groupBox_19.setMaximumSize(QtCore.QSize(212, 91))
        self.groupBox_19.setTitle("")
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label_19 = QtWidgets.QLabel(self.groupBox_19)
        self.label_19.setObjectName("label_19")
        self.gridLayout_28.addWidget(self.label_19, 0, 0, 1, 1)
        self.dropAerodromo = QtWidgets.QComboBox(self.groupBox_19)
        self.dropAerodromo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropAerodromo.setObjectName("dropAerodromo")
        self.dropAerodromo.addItem("")
        self.gridLayout_28.addWidget(self.dropAerodromo, 1, 0, 1, 1)
        self.toolBox_6.addItem(self.toolBox_6Page1, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.groupBox_13 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 0, 212, 91))
        self.groupBox_13.setTitle("")
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.dropFabricante = QtWidgets.QComboBox(self.groupBox_13)
        self.dropFabricante.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropFabricante.setObjectName("dropFabricante")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.dropFabricante.addItem("")
        self.gridLayout_21.addWidget(self.dropFabricante, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_13)
        self.label_12.setObjectName("label_12")
        self.gridLayout_21.addWidget(self.label_12, 0, 0, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_14.setGeometry(QtCore.QRect(230, 0, 211, 91))
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_13 = QtWidgets.QLabel(self.groupBox_14)
        self.label_13.setObjectName("label_13")
        self.gridLayout_22.addWidget(self.label_13, 0, 0, 1, 1)
        self.dropCategoriaPeso = QtWidgets.QComboBox(self.groupBox_14)
        self.dropCategoriaPeso.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropCategoriaPeso.setObjectName("dropCategoriaPeso")
        self.dropCategoriaPeso.addItem("")
        self.gridLayout_22.addWidget(self.dropCategoriaPeso, 1, 0, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_15.setGeometry(QtCore.QRect(450, 0, 211, 91))
        self.groupBox_15.setTitle("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_14 = QtWidgets.QLabel(self.groupBox_15)
        self.label_14.setObjectName("label_14")
        self.gridLayout_23.addWidget(self.label_14, 0, 0, 1, 1)
        self.dropQtdMotores = QtWidgets.QComboBox(self.groupBox_15)
        self.dropQtdMotores.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropQtdMotores.setObjectName("dropQtdMotores")
        self.dropQtdMotores.addItem("")
        self.gridLayout_23.addWidget(self.dropQtdMotores, 1, 0, 1, 1)
        self.groupBox_16 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 100, 212, 91))
        self.groupBox_16.setTitle("")
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.dropTipoAeronave = QtWidgets.QComboBox(self.groupBox_16)
        self.dropTipoAeronave.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.dropTipoAeronave.setObjectName("dropTipoAeronave")
        self.dropTipoAeronave.addItem("")
        self.gridLayout_24.addWidget(self.dropTipoAeronave, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_16)
        self.label_15.setObjectName("label_15")
        self.gridLayout_24.addWidget(self.label_15, 0, 0, 1, 1)
        self.toolBox_6.addItem(self.page_5, "")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab1)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 460, 1171, 298))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.tableResultadosOco = QtWidgets.QTableWidget(self.tab_10)
        self.tableResultadosOco.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableResultadosOco.setAlternatingRowColors(True)
        self.tableResultadosOco.setObjectName("tableResultadosOco")
        self.tableResultadosOco.setColumnCount(10)
        self.tableResultadosOco.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(112, 112, 112))
        self.tableResultadosOco.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosOco.setHorizontalHeaderItem(9, item)
        self.tableResultadosOco.verticalHeader().setVisible(False)
        self.gridLayout_13.addWidget(self.tableResultadosOco, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableResultadosAero = QtWidgets.QTableWidget(self.tab)
        self.tableResultadosAero.setGeometry(QtCore.QRect(11, 11, 1145, 243))
        self.tableResultadosAero.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableResultadosAero.setAlternatingRowColors(True)
        self.tableResultadosAero.setObjectName("tableResultadosAero")
        self.tableResultadosAero.setColumnCount(8)
        self.tableResultadosAero.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(112, 112, 112))
        self.tableResultadosAero.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosAero.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosAero.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosAero.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosAero.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosAero.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosAero.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadosAero.setHorizontalHeaderItem(7, item)
        self.tableResultadosAero.verticalHeader().setVisible(False)
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_9)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 14, 1141, 241))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.buscarButton = QtWidgets.QPushButton(self.tab1)
        self.buscarButton.setGeometry(QtCore.QRect(930, 390, 121, 41))
        self.buscarButton.setObjectName("buscarButton")
        self.limparButton = QtWidgets.QPushButton(self.tab1)
        self.limparButton.setGeometry(QtCore.QRect(790, 390, 121, 41))
        self.limparButton.setStyleSheet("selection-background-color: rgb(170, 0, 0);")
        self.limparButton.setObjectName("limparButton")
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 25))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.menuMenu.addAction(self.actionSalvar)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSair)
        self.menuSobre.addAction(self.actionSobre)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #MainWindow.setTabOrder(self.treeWidget, MainWindow.horizontalSlider)
        #MainWindow.setTabOrder(MainWindow.horizontalSlider, MainWindow.textEdit)
        #MainWindow.setTabOrder(MainWindow.textEdit, MainWindow.verticalSlider)
        #MainWindow.setTabOrder(MainWindow.verticalSlider, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_11.setText(_translate("MainWindow", "Fatal"))
        self.label_6.setText(_translate("MainWindow", "Fatalidade"))
        self.radioButton_12.setText(_translate("MainWindow", "Qualquer"))
        self.radioButton_13.setText(_translate("MainWindow", "Não Fatal"))
        self.radioButton_5.setText(_translate("MainWindow", "Em Andamento"))
        self.radioButton_7.setText(_translate("MainWindow", "Finalizado"))
        self.label_9.setText(_translate("MainWindow", "Status Investigativo"))
        self.radioButton_6.setText(_translate("MainWindow", "Qualquer"))
        self.radioButton_4.setText(_translate("MainWindow", "Incidente"))
        self.label_10.setText(_translate("MainWindow", "Classificação"))
        self.radioButton_3.setText(_translate("MainWindow", "Acidente"))
        self.radioButton_2.setText(_translate("MainWindow", "Qualquer"))
        self.label_7.setText(_translate("MainWindow", "Estado/UF"))
        self.dropEstado.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.dropEstado.setItemText(1, _translate("MainWindow", "Acre (AC)"))
        self.dropEstado.setItemText(2, _translate("MainWindow", "Alagoas (AL)"))
        self.dropEstado.setItemText(3, _translate("MainWindow", "Amapá (AP)"))
        self.dropEstado.setItemText(4, _translate("MainWindow", "Amazonas (AM)"))
        self.dropEstado.setItemText(5, _translate("MainWindow", "Bahia (BA)"))
        self.dropEstado.setItemText(6, _translate("MainWindow", "Ceará (CE)"))
        self.dropEstado.setItemText(7, _translate("MainWindow", "Distrito Federal (DF)"))
        self.dropEstado.setItemText(8, _translate("MainWindow", "Espírito Santo (Amém)"))
        self.dropEstado.setItemText(9, _translate("MainWindow", "Goiás (GO)"))
        self.dropEstado.setItemText(10, _translate("MainWindow", "Maranhão (MA)"))
        self.dropEstado.setItemText(11, _translate("MainWindow", "Mato Grosso (MT)"))
        self.dropEstado.setItemText(12, _translate("MainWindow", "Mato Grosso do Sul (MS)"))
        self.dropEstado.setItemText(13, _translate("MainWindow", "Minas Gerais (MG)"))
        self.dropEstado.setItemText(14, _translate("MainWindow", "Pará (PA)"))
        self.dropEstado.setItemText(15, _translate("MainWindow", "Paraíba (PB)"))
        self.dropEstado.setItemText(16, _translate("MainWindow", "Paraná (PR)"))
        self.dropEstado.setItemText(17, _translate("MainWindow", "Pernambuco (PE)"))
        self.dropEstado.setItemText(18, _translate("MainWindow", "Piauí (PI)"))
        self.dropEstado.setItemText(19, _translate("MainWindow", "Rio de Janeiro (RJ)"))
        self.dropEstado.setItemText(20, _translate("MainWindow", "Rio Grande do Norte (RN)"))
        self.dropEstado.setItemText(21, _translate("MainWindow", "Rio Grande do Sul (RS)"))
        self.dropEstado.setItemText(22, _translate("MainWindow", "Rondônia (RO)"))
        self.dropEstado.setItemText(23, _translate("MainWindow", "Roraima (RR)"))
        self.dropEstado.setItemText(24, _translate("MainWindow", "Santa Catarina (SC)"))
        self.dropEstado.setItemText(25, _translate("MainWindow", "São Paulo (SP)"))
        self.dropEstado.setItemText(26, _translate("MainWindow", "Sergipe (SE)"))
        self.dropEstado.setItemText(27, _translate("MainWindow", "Tocantins (TO)"))
        self.label_8.setText(_translate("MainWindow", "Turno do Dia"))
        self.dropTurno.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.label_16.setText(_translate("MainWindow", "Tipo"))
        self.dropTipoOco.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.label_4.setText(_translate("MainWindow", "Período de Tempo"))
        self.label_11.setText(_translate("MainWindow", "Código Identificador (Completo ou Parcial)"))
        self.textCodigo.setPlaceholderText(_translate("MainWindow", " ID (numérico)"))
        self.label_17.setText(_translate("MainWindow", "Cidade"))
        self.dropCidade.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.label_19.setText(_translate("MainWindow", "Aeródromo"))
        self.dropAerodromo.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.toolBox_6Page1), _translate("MainWindow", "Ocorrências"))
        self.dropFabricante.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.dropFabricante.setItemText(1, _translate("MainWindow", "Acre (AC)"))
        self.dropFabricante.setItemText(2, _translate("MainWindow", "Alagoas (AL)"))
        self.dropFabricante.setItemText(3, _translate("MainWindow", "Amapá (AP)"))
        self.dropFabricante.setItemText(4, _translate("MainWindow", "Amazonas (AM)"))
        self.dropFabricante.setItemText(5, _translate("MainWindow", "Bahia (BA)"))
        self.dropFabricante.setItemText(6, _translate("MainWindow", "Ceará (CE)"))
        self.dropFabricante.setItemText(7, _translate("MainWindow", "Distrito Federal (DF)"))
        self.dropFabricante.setItemText(8, _translate("MainWindow", "Espírito Santo (Amém)"))
        self.dropFabricante.setItemText(9, _translate("MainWindow", "Goiás (GO)"))
        self.dropFabricante.setItemText(10, _translate("MainWindow", "Maranhão (MA)"))
        self.dropFabricante.setItemText(11, _translate("MainWindow", "Mato Grosso (MT)"))
        self.dropFabricante.setItemText(12, _translate("MainWindow", "Mato Grosso do Sul (MS)"))
        self.dropFabricante.setItemText(13, _translate("MainWindow", "Minas Gerais (MG)"))
        self.dropFabricante.setItemText(14, _translate("MainWindow", "Pará (PA)"))
        self.dropFabricante.setItemText(15, _translate("MainWindow", "Paraíba (PB)"))
        self.dropFabricante.setItemText(16, _translate("MainWindow", "Paraná (PR)"))
        self.dropFabricante.setItemText(17, _translate("MainWindow", "Pernambuco (PE)"))
        self.dropFabricante.setItemText(18, _translate("MainWindow", "Piauí (PI)"))
        self.dropFabricante.setItemText(19, _translate("MainWindow", "Rio de Janeiro (RJ)"))
        self.dropFabricante.setItemText(20, _translate("MainWindow", "Rio Grande do Norte (RN)"))
        self.dropFabricante.setItemText(21, _translate("MainWindow", "Rio Grande do Sul (RS)"))
        self.dropFabricante.setItemText(22, _translate("MainWindow", "Rondônia (RO)"))
        self.dropFabricante.setItemText(23, _translate("MainWindow", "Roraima (RR)"))
        self.dropFabricante.setItemText(24, _translate("MainWindow", "Santa Catarina (SC)"))
        self.dropFabricante.setItemText(25, _translate("MainWindow", "São Paulo (SP)"))
        self.dropFabricante.setItemText(26, _translate("MainWindow", "Sergipe (SE)"))
        self.dropFabricante.setItemText(27, _translate("MainWindow", "Tocantins (TO)"))
        self.label_12.setText(_translate("MainWindow", "Fabricante"))
        self.label_13.setText(_translate("MainWindow", "Categoria de Peso"))
        self.dropCategoriaPeso.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.label_14.setText(_translate("MainWindow", "Quantidade de Motores"))
        self.dropQtdMotores.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.dropTipoAeronave.setItemText(0, _translate("MainWindow", "Qualquer"))
        self.label_15.setText(_translate("MainWindow", "Tipo"))
        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.page_5), _translate("MainWindow", "Aeronaves Envolvidas"))
        self.tableResultadosOco.setSortingEnabled(True)
        item = self.tableResultadosOco.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableResultadosOco.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Classificação"))
        item = self.tableResultadosOco.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo de Ocorrência"))
        item = self.tableResultadosOco.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cidade"))
        item = self.tableResultadosOco.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "UF"))
        item = self.tableResultadosOco.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Aeródromo"))
        item = self.tableResultadosOco.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dia e Hora"))
        item = self.tableResultadosOco.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Turno do Dia"))
        item = self.tableResultadosOco.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Investigação"))
        item = self.tableResultadosOco.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "# Aeronaves"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MainWindow", "Resultados Ocorrências"))
        self.tableResultadosAero.setSortingEnabled(True)
        item = self.tableResultadosAero.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableResultadosAero.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo de Aeronave"))
        item = self.tableResultadosAero.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fabricante"))
        item = self.tableResultadosAero.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Modelo"))
        item = self.tableResultadosAero.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "# Motores"))
        item = self.tableResultadosAero.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Classe"))
        item = self.tableResultadosAero.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dano"))
        item = self.tableResultadosAero.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fatalidades"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("MainWindow", "Resultados Aeronaves"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Ranking"))
        self.buscarButton.setText(_translate("MainWindow", "Buscar"))
        self.limparButton.setText(_translate("MainWindow", "Limpar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Busca"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "covfefe"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "cov"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "fefe"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuMenu.setTitle(_translate("MainWindow", "&Menu"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))
        self.actionSalvar.setText(_translate("MainWindow", "&Salvar Resultados"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSair.setToolTip(_translate("MainWindow", "Fechar o airsort"))
        self.actionSair.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre airsort"))

