# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(600, 0))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.atenMagPlotBox = QtWidgets.QGroupBox(self.tab)
        self.atenMagPlotBox.setMinimumSize(QtCore.QSize(300, 300))
        self.atenMagPlotBox.setTitle("")
        self.atenMagPlotBox.setObjectName("atenMagPlotBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.atenMagPlotBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_4.addWidget(self.atenMagPlotBox, 0, 0, 1, 1)
        self.atenFasePlotBox = QtWidgets.QGroupBox(self.tab)
        self.atenFasePlotBox.setMinimumSize(QtCore.QSize(300, 300))
        self.atenFasePlotBox.setTitle("")
        self.atenFasePlotBox.setObjectName("atenFasePlotBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.atenFasePlotBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_4.addWidget(self.atenFasePlotBox, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ganMagPlotBox = QtWidgets.QGroupBox(self.tab_2)
        self.ganMagPlotBox.setTitle("")
        self.ganMagPlotBox.setObjectName("ganMagPlotBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.ganMagPlotBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_6.addWidget(self.ganMagPlotBox, 0, 0, 1, 1)
        self.ganFasePlotBox = QtWidgets.QGroupBox(self.tab_2)
        self.ganFasePlotBox.setTitle("")
        self.ganFasePlotBox.setObjectName("ganFasePlotBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.ganFasePlotBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_6.addWidget(self.ganFasePlotBox, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.curvaNormalizadaPlotBox = QtWidgets.QGroupBox(self.tab_7)
        self.curvaNormalizadaPlotBox.setTitle("")
        self.curvaNormalizadaPlotBox.setObjectName("curvaNormalizadaPlotBox")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.curvaNormalizadaPlotBox)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.gridLayout_33.addWidget(self.curvaNormalizadaPlotBox, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.polosCerosPlotBox = QtWidgets.QGroupBox(self.tab_3)
        self.polosCerosPlotBox.setTitle("")
        self.polosCerosPlotBox.setObjectName("polosCerosPlotBox")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.polosCerosPlotBox)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_7.addWidget(self.polosCerosPlotBox, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupDelayPlotBox = QtWidgets.QGroupBox(self.tab_10)
        self.groupDelayPlotBox.setTitle("")
        self.groupDelayPlotBox.setObjectName("groupDelayPlotBox")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.groupDelayPlotBox)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.gridLayout_15.addWidget(self.groupDelayPlotBox, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.ordenQComboBox = QtWidgets.QComboBox(self.tab_4)
        self.ordenQComboBox.setObjectName("ordenQComboBox")
        self.gridLayout_29.addWidget(self.ordenQComboBox, 0, 0, 1, 1)
        self.ordenQLatexBox = QtWidgets.QGroupBox(self.tab_4)
        self.ordenQLatexBox.setTitle("")
        self.ordenQLatexBox.setObjectName("ordenQLatexBox")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.ordenQLatexBox)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.gridLayout_29.addWidget(self.ordenQLatexBox, 2, 0, 1, 1)
        self.ordenQButton = QtWidgets.QPushButton(self.tab_4)
        self.ordenQButton.setObjectName("ordenQButton")
        self.gridLayout_29.addWidget(self.ordenQButton, 1, 0, 1, 1)
        self.gridLayout_32.addLayout(self.gridLayout_29, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.respuestaEscalonPlotBox = QtWidgets.QGroupBox(self.tab_8)
        self.respuestaEscalonPlotBox.setTitle("")
        self.respuestaEscalonPlotBox.setObjectName("respuestaEscalonPlotBox")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.respuestaEscalonPlotBox)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.gridLayout_35.addWidget(self.respuestaEscalonPlotBox, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 3, 10, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.borrarTodasPlantillasButton = QtWidgets.QPushButton(self.groupBox_2)
        self.borrarTodasPlantillasButton.setObjectName("borrarTodasPlantillasButton")
        self.gridLayout_2.addWidget(self.borrarTodasPlantillasButton, 12, 1, 2, 1)
        self.tipoFiltroComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.tipoFiltroComboBox.setObjectName("tipoFiltroComboBox")
        self.tipoFiltroComboBox.addItem("")
        self.tipoFiltroComboBox.addItem("")
        self.tipoFiltroComboBox.addItem("")
        self.tipoFiltroComboBox.addItem("")
        self.gridLayout_2.addWidget(self.tipoFiltroComboBox, 0, 1, 1, 1)
        self.borrarPlantillasButton = QtWidgets.QPushButton(self.groupBox_2)
        self.borrarPlantillasButton.setObjectName("borrarPlantillasButton")
        self.gridLayout_2.addWidget(self.borrarPlantillasButton, 12, 0, 2, 1)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.groupBox_2)
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_53 = QtWidgets.QLabel(self.page_3)
        self.label_53.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_53.setObjectName("label_53")
        self.gridLayout_16.addWidget(self.label_53, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.page_3)
        self.label_27.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_27.setObjectName("label_27")
        self.gridLayout_16.addWidget(self.label_27, 2, 0, 1, 1)
        self.fpLP = QtWidgets.QLineEdit(self.page_3)
        self.fpLP.setObjectName("fpLP")
        self.gridLayout_16.addWidget(self.fpLP, 0, 1, 1, 1)
        self.faLP = QtWidgets.QLineEdit(self.page_3)
        self.faLP.setObjectName("faLP")
        self.gridLayout_16.addWidget(self.faLP, 2, 1, 1, 1)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_55 = QtWidgets.QLabel(self.page_4)
        self.label_55.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_55.setObjectName("label_55")
        self.gridLayout_17.addWidget(self.label_55, 0, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.page_4)
        self.label_54.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_54.setObjectName("label_54")
        self.gridLayout_17.addWidget(self.label_54, 1, 0, 1, 1)
        self.fpHP = QtWidgets.QLineEdit(self.page_4)
        self.fpHP.setObjectName("fpHP")
        self.gridLayout_17.addWidget(self.fpHP, 0, 1, 1, 1)
        self.faHP = QtWidgets.QLineEdit(self.page_4)
        self.faHP.setObjectName("faHP")
        self.gridLayout_17.addWidget(self.faHP, 1, 1, 1, 1)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.BPTypeComboBox = QtWidgets.QComboBox(self.page_7)
        self.BPTypeComboBox.setObjectName("BPTypeComboBox")
        self.BPTypeComboBox.addItem("")
        self.BPTypeComboBox.addItem("")
        self.gridLayout_18.addWidget(self.BPTypeComboBox, 0, 0, 1, 2)
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.page_7)
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_63 = QtWidgets.QLabel(self.page_8)
        self.label_63.setObjectName("label_63")
        self.gridLayout_19.addWidget(self.label_63, 0, 0, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.page_8)
        self.label_62.setObjectName("label_62")
        self.gridLayout_19.addWidget(self.label_62, 1, 0, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.page_8)
        self.label_61.setObjectName("label_61")
        self.gridLayout_19.addWidget(self.label_61, 2, 0, 1, 1)
        self.f0BP = QtWidgets.QLineEdit(self.page_8)
        self.f0BP.setObjectName("f0BP")
        self.gridLayout_19.addWidget(self.f0BP, 0, 1, 1, 1)
        self.dFpBP = QtWidgets.QLineEdit(self.page_8)
        self.dFpBP.setObjectName("dFpBP")
        self.gridLayout_19.addWidget(self.dFpBP, 1, 1, 1, 1)
        self.dFaBP = QtWidgets.QLineEdit(self.page_8)
        self.dFaBP.setObjectName("dFaBP")
        self.gridLayout_19.addWidget(self.dFaBP, 2, 1, 1, 1)
        self.stackedWidget_4.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_58 = QtWidgets.QLabel(self.page_9)
        self.label_58.setObjectName("label_58")
        self.gridLayout_20.addWidget(self.label_58, 0, 0, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.page_9)
        self.label_60.setObjectName("label_60")
        self.gridLayout_20.addWidget(self.label_60, 1, 0, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.page_9)
        self.label_64.setObjectName("label_64")
        self.gridLayout_20.addWidget(self.label_64, 2, 0, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.page_9)
        self.label_59.setObjectName("label_59")
        self.gridLayout_20.addWidget(self.label_59, 3, 0, 1, 1)
        self.fpXBP = QtWidgets.QLineEdit(self.page_9)
        self.fpXBP.setObjectName("fpXBP")
        self.gridLayout_20.addWidget(self.fpXBP, 0, 1, 1, 1)
        self.fpYBP = QtWidgets.QLineEdit(self.page_9)
        self.fpYBP.setObjectName("fpYBP")
        self.gridLayout_20.addWidget(self.fpYBP, 1, 1, 1, 1)
        self.faXBP = QtWidgets.QLineEdit(self.page_9)
        self.faXBP.setObjectName("faXBP")
        self.gridLayout_20.addWidget(self.faXBP, 2, 1, 1, 1)
        self.faYBP = QtWidgets.QLineEdit(self.page_9)
        self.faYBP.setObjectName("faYBP")
        self.gridLayout_20.addWidget(self.faYBP, 3, 1, 1, 1)
        self.stackedWidget_4.addWidget(self.page_9)
        self.gridLayout_18.addWidget(self.stackedWidget_4, 1, 0, 1, 2)
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.formLayout = QtWidgets.QFormLayout(self.page_10)
        self.formLayout.setObjectName("formLayout")
        self.BSTypeComboBox = QtWidgets.QComboBox(self.page_10)
        self.BSTypeComboBox.setObjectName("BSTypeComboBox")
        self.BSTypeComboBox.addItem("")
        self.BSTypeComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.BSTypeComboBox)
        self.stackedWidget_5 = QtWidgets.QStackedWidget(self.page_10)
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.page_11)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_67 = QtWidgets.QLabel(self.page_11)
        self.label_67.setObjectName("label_67")
        self.gridLayout_21.addWidget(self.label_67, 0, 0, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.page_11)
        self.label_66.setObjectName("label_66")
        self.gridLayout_21.addWidget(self.label_66, 1, 0, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.page_11)
        self.label_65.setObjectName("label_65")
        self.gridLayout_21.addWidget(self.label_65, 2, 0, 1, 1)
        self.f0BS = QtWidgets.QLineEdit(self.page_11)
        self.f0BS.setObjectName("f0BS")
        self.gridLayout_21.addWidget(self.f0BS, 0, 1, 1, 1)
        self.dFpBS = QtWidgets.QLineEdit(self.page_11)
        self.dFpBS.setObjectName("dFpBS")
        self.gridLayout_21.addWidget(self.dFpBS, 1, 1, 1, 1)
        self.dFaBS = QtWidgets.QLineEdit(self.page_11)
        self.dFaBS.setObjectName("dFaBS")
        self.gridLayout_21.addWidget(self.dFaBS, 2, 1, 1, 1)
        self.stackedWidget_5.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.page_12)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_69 = QtWidgets.QLabel(self.page_12)
        self.label_69.setObjectName("label_69")
        self.gridLayout_22.addWidget(self.label_69, 0, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.page_12)
        self.label_71.setObjectName("label_71")
        self.gridLayout_22.addWidget(self.label_71, 1, 0, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.page_12)
        self.label_70.setObjectName("label_70")
        self.gridLayout_22.addWidget(self.label_70, 2, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.page_12)
        self.label_68.setObjectName("label_68")
        self.gridLayout_22.addWidget(self.label_68, 3, 0, 1, 1)
        self.fpXBS = QtWidgets.QLineEdit(self.page_12)
        self.fpXBS.setObjectName("fpXBS")
        self.gridLayout_22.addWidget(self.fpXBS, 0, 1, 1, 1)
        self.fpYBS = QtWidgets.QLineEdit(self.page_12)
        self.fpYBS.setObjectName("fpYBS")
        self.gridLayout_22.addWidget(self.fpYBS, 1, 1, 1, 1)
        self.faXBS = QtWidgets.QLineEdit(self.page_12)
        self.faXBS.setObjectName("faXBS")
        self.gridLayout_22.addWidget(self.faXBS, 2, 1, 1, 1)
        self.faYBS = QtWidgets.QLineEdit(self.page_12)
        self.faYBS.setObjectName("faYBS")
        self.gridLayout_22.addWidget(self.faYBS, 3, 1, 1, 1)
        self.stackedWidget_5.addWidget(self.page_12)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.stackedWidget_5)
        self.stackedWidget_2.addWidget(self.page_10)
        self.gridLayout_2.addWidget(self.stackedWidget_2, 1, 0, 1, 2)
        self.label_73 = QtWidgets.QLabel(self.groupBox_2)
        self.label_73.setMaximumSize(QtCore.QSize(100, 50))
        self.label_73.setObjectName("label_73")
        self.gridLayout_2.addWidget(self.label_73, 2, 0, 2, 1)
        self.crearPlantillaButton = QtWidgets.QPushButton(self.groupBox_2)
        self.crearPlantillaButton.setObjectName("crearPlantillaButton")
        self.gridLayout_2.addWidget(self.crearPlantillaButton, 7, 0, 3, 2)
        self.label_72 = QtWidgets.QLabel(self.groupBox_2)
        self.label_72.setMaximumSize(QtCore.QSize(100, 50))
        self.label_72.setObjectName("label_72")
        self.gridLayout_2.addWidget(self.label_72, 4, 0, 2, 1)
        self.listPlantillasWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listPlantillasWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listPlantillasWidget.setObjectName("listPlantillasWidget")
        self.gridLayout_2.addWidget(self.listPlantillasWidget, 10, 0, 1, 2)
        self.graficarPlantillasButton = QtWidgets.QPushButton(self.groupBox_2)
        self.graficarPlantillasButton.setObjectName("graficarPlantillasButton")
        self.gridLayout_2.addWidget(self.graficarPlantillasButton, 14, 0, 1, 2)
        self.apVal = QtWidgets.QLineEdit(self.groupBox_2)
        self.apVal.setObjectName("apVal")
        self.gridLayout_2.addWidget(self.apVal, 2, 1, 2, 1)
        self.aaVal = QtWidgets.QLineEdit(self.groupBox_2)
        self.aaVal.setObjectName("aaVal")
        self.gridLayout_2.addWidget(self.aaVal, 4, 1, 2, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 10, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.borrarFiltrosButton = QtWidgets.QPushButton(self.groupBox)
        self.borrarFiltrosButton.setObjectName("borrarFiltrosButton")
        self.gridLayout_24.addWidget(self.borrarFiltrosButton, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_24.addWidget(self.label_3, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_24.addWidget(self.label_2, 9, 0, 1, 1)
        self.listFiltrosWidget = QtWidgets.QListWidget(self.groupBox)
        self.listFiltrosWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listFiltrosWidget.setObjectName("listFiltrosWidget")
        self.gridLayout_24.addWidget(self.listFiltrosWidget, 4, 0, 1, 2)
        self.crearFiltroButton = QtWidgets.QPushButton(self.groupBox)
        self.crearFiltroButton.setObjectName("crearFiltroButton")
        self.gridLayout_24.addWidget(self.crearFiltroButton, 2, 0, 2, 2)
        self.tipoAproxComboBox = QtWidgets.QComboBox(self.groupBox)
        self.tipoAproxComboBox.setObjectName("tipoAproxComboBox")
        self.tipoAproxComboBox.addItem("")
        self.tipoAproxComboBox.addItem("")
        self.tipoAproxComboBox.addItem("")
        self.tipoAproxComboBox.addItem("")
        self.gridLayout_24.addWidget(self.tipoAproxComboBox, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_24.addWidget(self.label_6, 0, 0, 1, 1)
        self.borrarTodosFiltrosButton = QtWidgets.QPushButton(self.groupBox)
        self.borrarTodosFiltrosButton.setObjectName("borrarTodosFiltrosButton")
        self.gridLayout_24.addWidget(self.borrarTodosFiltrosButton, 5, 1, 1, 1)
        self.cambiarOrdenFiltroButton = QtWidgets.QPushButton(self.groupBox)
        self.cambiarOrdenFiltroButton.setObjectName("cambiarOrdenFiltroButton")
        self.gridLayout_24.addWidget(self.cambiarOrdenFiltroButton, 6, 0, 1, 2)
        self.cambiarRangoFiltroButton = QtWidgets.QPushButton(self.groupBox)
        self.cambiarRangoFiltroButton.setObjectName("cambiarRangoFiltroButton")
        self.gridLayout_24.addWidget(self.cambiarRangoFiltroButton, 7, 0, 2, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_24.addWidget(self.label_5, 1, 0, 1, 1)
        self.rangoPorcentaje = QtWidgets.QLineEdit(self.groupBox)
        self.rangoPorcentaje.setObjectName("rangoPorcentaje")
        self.gridLayout_24.addWidget(self.rangoPorcentaje, 1, 1, 1, 1)
        self.graficarFiltrosButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.graficarFiltrosButton.setFont(font)
        self.graficarFiltrosButton.setObjectName("graficarFiltrosButton")
        self.gridLayout_24.addWidget(self.graficarFiltrosButton, 11, 0, 3, 2)
        self.minFreq = QtWidgets.QLineEdit(self.groupBox)
        self.minFreq.setObjectName("minFreq")
        self.gridLayout_24.addWidget(self.minFreq, 10, 0, 1, 1)
        self.maxFreq = QtWidgets.QLineEdit(self.groupBox)
        self.maxFreq.setObjectName("maxFreq")
        self.gridLayout_24.addWidget(self.maxFreq, 10, 1, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_24, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.listaEtapasWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.listaEtapasWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listaEtapasWidget.setObjectName("listaEtapasWidget")
        self.gridLayout_27.addWidget(self.listaEtapasWidget, 2, 0, 1, 2)
        self.filtroComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.filtroComboBox.setObjectName("filtroComboBox")
        self.gridLayout_27.addWidget(self.filtroComboBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_27.addWidget(self.label_4, 0, 0, 1, 1)
        self.borrarEtapasButton = QtWidgets.QPushButton(self.groupBox_4)
        self.borrarEtapasButton.setObjectName("borrarEtapasButton")
        self.gridLayout_27.addWidget(self.borrarEtapasButton, 3, 0, 1, 1)
        self.cambiarGananciaEtapasButton = QtWidgets.QPushButton(self.groupBox_4)
        self.cambiarGananciaEtapasButton.setObjectName("cambiarGananciaEtapasButton")
        self.gridLayout_27.addWidget(self.cambiarGananciaEtapasButton, 3, 1, 1, 1)
        self.obtenerEtapasButton = QtWidgets.QPushButton(self.groupBox_4)
        self.obtenerEtapasButton.setObjectName("obtenerEtapasButton")
        self.gridLayout_27.addWidget(self.obtenerEtapasButton, 1, 0, 1, 2)
        self.gridLayout_28.addLayout(self.gridLayout_27, 0, 0, 1, 1)
        self.graficarRespEtapaButton = QtWidgets.QPushButton(self.groupBox_4)
        self.graficarRespEtapaButton.setObjectName("graficarRespEtapaButton")
        self.gridLayout_28.addWidget(self.graficarRespEtapaButton, 1, 0, 1, 1)
        self.gridLayout_26.addWidget(self.groupBox_4, 0, 0, 2, 1)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_6)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.etapaGanMagPlotBox = QtWidgets.QGroupBox(self.tab_11)
        self.etapaGanMagPlotBox.setMinimumSize(QtCore.QSize(300, 300))
        self.etapaGanMagPlotBox.setTitle("")
        self.etapaGanMagPlotBox.setObjectName("etapaGanMagPlotBox")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.etapaGanMagPlotBox)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayout_37.addWidget(self.etapaGanMagPlotBox, 0, 0, 1, 1)
        self.etapaGanFasePlotBox = QtWidgets.QGroupBox(self.tab_11)
        self.etapaGanFasePlotBox.setMinimumSize(QtCore.QSize(300, 300))
        self.etapaGanFasePlotBox.setTitle("")
        self.etapaGanFasePlotBox.setObjectName("etapaGanFasePlotBox")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.etapaGanFasePlotBox)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.gridLayout_37.addWidget(self.etapaGanFasePlotBox, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.polosCerosEtapasPlotBox = QtWidgets.QGroupBox(self.tab_12)
        self.polosCerosEtapasPlotBox.setTitle("")
        self.polosCerosEtapasPlotBox.setObjectName("polosCerosEtapasPlotBox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.polosCerosEtapasPlotBox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_9.addWidget(self.polosCerosEtapasPlotBox, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.infoEtapaComboBox = QtWidgets.QComboBox(self.tab_9)
        self.infoEtapaComboBox.setObjectName("infoEtapaComboBox")
        self.gridLayout_13.addWidget(self.infoEtapaComboBox, 0, 0, 1, 1)
        self.mostrarInfoButton = QtWidgets.QPushButton(self.tab_9)
        self.mostrarInfoButton.setObjectName("mostrarInfoButton")
        self.gridLayout_13.addWidget(self.mostrarInfoButton, 1, 0, 1, 1)
        self.infoLatexBox = QtWidgets.QGroupBox(self.tab_9)
        self.infoLatexBox.setMinimumSize(QtCore.QSize(0, 200))
        self.infoLatexBox.setTitle("")
        self.infoLatexBox.setObjectName("infoLatexBox")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.infoLatexBox)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_13.addWidget(self.infoLatexBox, 2, 0, 1, 1)
        self.infoPoloCeroPlotBox = QtWidgets.QGroupBox(self.tab_9)
        self.infoPoloCeroPlotBox.setTitle("")
        self.infoPoloCeroPlotBox.setObjectName("infoPoloCeroPlotBox")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.infoPoloCeroPlotBox)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.gridLayout_13.addWidget(self.infoPoloCeroPlotBox, 3, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_9, "")
        self.gridLayout_26.addWidget(self.tabWidget_3, 0, 1, 2, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tipoFiltroComboBox.currentIndexChanged['int'].connect(self.stackedWidget_2.setCurrentIndex) # type: ignore
        self.BPTypeComboBox.currentIndexChanged['int'].connect(self.stackedWidget_4.setCurrentIndex) # type: ignore
        self.BSTypeComboBox.currentIndexChanged['int'].connect(self.stackedWidget_5.setCurrentIndex) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Curvas de atenuación"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Curvas de ganancia"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Curva normalizada"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Polos y ceros"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Group Delay"))
        self.ordenQButton.setText(_translate("MainWindow", "Ver orden mínimo, actual y máximo Q"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Orden y máximo Q"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Respuesta al escalón"))
        self.label.setText(_translate("MainWindow", "Tipo de Filtro"))
        self.borrarTodasPlantillasButton.setText(_translate("MainWindow", "Borrar todas"))
        self.tipoFiltroComboBox.setItemText(0, _translate("MainWindow", "Pasa Bajos"))
        self.tipoFiltroComboBox.setItemText(1, _translate("MainWindow", "Pasa Altos"))
        self.tipoFiltroComboBox.setItemText(2, _translate("MainWindow", "Pasa Banda"))
        self.tipoFiltroComboBox.setItemText(3, _translate("MainWindow", "Rechaza Banda"))
        self.borrarPlantillasButton.setText(_translate("MainWindow", "Borrar selec."))
        self.label_53.setText(_translate("MainWindow", "Fp"))
        self.label_27.setText(_translate("MainWindow", "Fa"))
        self.fpLP.setText(_translate("MainWindow", "1e3"))
        self.faLP.setText(_translate("MainWindow", "10e3"))
        self.label_55.setText(_translate("MainWindow", "Fp"))
        self.label_54.setText(_translate("MainWindow", "Fa"))
        self.fpHP.setText(_translate("MainWindow", "1e3"))
        self.faHP.setText(_translate("MainWindow", "10e3"))
        self.BPTypeComboBox.setItemText(0, _translate("MainWindow", "Anchos de Banda"))
        self.BPTypeComboBox.setItemText(1, _translate("MainWindow", "Frecuencias"))
        self.label_63.setText(_translate("MainWindow", "Fo"))
        self.label_62.setText(_translate("MainWindow", "ΔFp"))
        self.label_61.setText(_translate("MainWindow", "ΔFa"))
        self.f0BP.setText(_translate("MainWindow", "10e3"))
        self.dFpBP.setText(_translate("MainWindow", "100"))
        self.dFaBP.setText(_translate("MainWindow", "500"))
        self.label_58.setText(_translate("MainWindow", "Fp-"))
        self.label_60.setText(_translate("MainWindow", "Fp+"))
        self.label_64.setText(_translate("MainWindow", "Fa-"))
        self.label_59.setText(_translate("MainWindow", "Fa+"))
        self.fpXBP.setText(_translate("MainWindow", "1000"))
        self.fpYBP.setText(_translate("MainWindow", "10e3"))
        self.faXBP.setText(_translate("MainWindow", "500"))
        self.faYBP.setText(_translate("MainWindow", "5000"))
        self.BSTypeComboBox.setItemText(0, _translate("MainWindow", "Anchos de Banda"))
        self.BSTypeComboBox.setItemText(1, _translate("MainWindow", "Frecuencias"))
        self.label_67.setText(_translate("MainWindow", "Fo"))
        self.label_66.setText(_translate("MainWindow", "ΔFp"))
        self.label_65.setText(_translate("MainWindow", "ΔFa"))
        self.f0BS.setText(_translate("MainWindow", "10e3"))
        self.dFpBS.setText(_translate("MainWindow", "500"))
        self.dFaBS.setText(_translate("MainWindow", "100"))
        self.label_69.setText(_translate("MainWindow", "Fp-"))
        self.label_71.setText(_translate("MainWindow", "Fp+"))
        self.label_70.setText(_translate("MainWindow", "Fa-"))
        self.label_68.setText(_translate("MainWindow", "Fa+"))
        self.fpXBS.setText(_translate("MainWindow", "500"))
        self.fpYBS.setText(_translate("MainWindow", "5000"))
        self.faXBS.setText(_translate("MainWindow", "1000"))
        self.faYBS.setText(_translate("MainWindow", "10000"))
        self.label_73.setText(_translate("MainWindow", "Ap"))
        self.crearPlantillaButton.setText(_translate("MainWindow", "Crear Plantilla"))
        self.label_72.setText(_translate("MainWindow", "Aa"))
        self.graficarPlantillasButton.setText(_translate("MainWindow", "Graficar plantillas selec."))
        self.apVal.setText(_translate("MainWindow", "3"))
        self.aaVal.setText(_translate("MainWindow", "100"))
        self.borrarFiltrosButton.setText(_translate("MainWindow", "Borrar selec."))
        self.label_3.setText(_translate("MainWindow", "Max freq"))
        self.label_2.setText(_translate("MainWindow", "Min freq"))
        self.crearFiltroButton.setText(_translate("MainWindow", "Crear Filtro"))
        self.tipoAproxComboBox.setItemText(0, _translate("MainWindow", "Butterworth"))
        self.tipoAproxComboBox.setItemText(1, _translate("MainWindow", "Chebyshev I"))
        self.tipoAproxComboBox.setItemText(2, _translate("MainWindow", "Chebyshev II (inverso)"))
        self.tipoAproxComboBox.setItemText(3, _translate("MainWindow", "Cauer (elíptico)"))
        self.label_6.setText(_translate("MainWindow", "Tipo de filtro"))
        self.borrarTodosFiltrosButton.setText(_translate("MainWindow", "Borrar todos"))
        self.cambiarOrdenFiltroButton.setText(_translate("MainWindow", "Cambiar Orden"))
        self.cambiarRangoFiltroButton.setText(_translate("MainWindow", "Cambiar Rango"))
        self.label_5.setText(_translate("MainWindow", "Rango (%)"))
        self.rangoPorcentaje.setText(_translate("MainWindow", "0"))
        self.graficarFiltrosButton.setText(_translate("MainWindow", "Graficar filtros"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Aproximaciones"))
        self.label_4.setText(_translate("MainWindow", "Seleccionar filtro"))
        self.borrarEtapasButton.setText(_translate("MainWindow", "Borrar etapas"))
        self.cambiarGananciaEtapasButton.setText(_translate("MainWindow", "Cambiar Ganancia"))
        self.obtenerEtapasButton.setText(_translate("MainWindow", "Obtener etapas"))
        self.graficarRespEtapaButton.setText(_translate("MainWindow", "Calcular respuesta en frecuencia"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "Respuesta en frecuencia"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Polos y ceros"))
        self.mostrarInfoButton.setText(_translate("MainWindow", "Mostrar información"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Información de las etapas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "División de etapas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
