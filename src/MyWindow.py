# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Filters2 import FilterClass
import scipy.signal as ss
import sympy as sp
from sympy.abc import s
import numpy as np
from src.plottingClasses import BodePlot, PolosCerosPlot, TemporalPlot, GroupDelayPlot
from src.PlantillaClass import PlantillaClass
from src.MPLLaTexClass import MPLTexText

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.listaFiltros: list[PlantillaClass]
        self.listaPlantillas: list[FilterClass]

        self.listaFiltros = []
        self.listaPlantillas = []
        self.listaSOS = []
        self.listaEtapas = []
        self.listaGananciaEtapas = []
        self.listaGananciaNominalEtapas = []

        self.filtroParaEtapas = None
        self.currentEtapasTF = None
        self.currentEtapasNum = sp.poly(1, s)
        self.currentEtapasDen = sp.poly(1, s)

        # Configuración gráfica

        # Gráficos de atenuación
        self.atenMagPlot = BodePlot(parent = self.atenMagPlotBox)
        self.atenMagPlotBox.layout().addWidget(self.atenMagPlot.navToolBar)
        self.atenMagPlotBox.layout().addWidget(self.atenMagPlot) #importante setear tamaños mínimos desde QTDesigner, sino no anda

        self.atenFasePlot = BodePlot(parent=self.atenFasePlotBox)
        self.atenFasePlotBox.layout().addWidget(self.atenFasePlot.navToolBar)
        self.atenFasePlotBox.layout().addWidget(self.atenFasePlot)

        # Gráficos de ganancia
        self.ganMagPlot = BodePlot(parent = self.ganMagPlotBox)
        self.ganMagPlotBox.layout().addWidget(self.ganMagPlot.navToolBar)
        self.ganMagPlotBox.layout().addWidget(self.ganMagPlot)

        self.ganFasePlot = BodePlot(parent=self.ganFasePlotBox)
        self.ganFasePlotBox.layout().addWidget(self.ganFasePlot.navToolBar)
        self.ganFasePlotBox.layout().addWidget(self.ganFasePlot)

        # Gráfico curva normalizada
        self.curvaNormalizadaPlot= BodePlot(parent=self.curvaNormalizadaPlotBox)
        self.curvaNormalizadaPlotBox.layout().addWidget(self.curvaNormalizadaPlot.navToolBar)
        self.curvaNormalizadaPlotBox.layout().addWidget(self.curvaNormalizadaPlot)

        # Gráficos de ganancia Etapas
        self.etapaGanMagPlot = BodePlot(parent=self.etapaGanMagPlotBox)
        self.etapaGanMagPlotBox.layout().addWidget(self.etapaGanMagPlot.navToolBar)
        self.etapaGanMagPlotBox.layout().addWidget(self.etapaGanMagPlot)

        self.etapaGanFasePlot = BodePlot(parent=self.etapaGanFasePlotBox)
        self.etapaGanFasePlotBox.layout().addWidget(self.etapaGanFasePlot.navToolBar)
        self.etapaGanFasePlotBox.layout().addWidget(self.etapaGanFasePlot)

        # Gráficos de polos y ceros
        self.polosCerosPlot = PolosCerosPlot(parent=self.polosCerosPlotBox)
        self.polosCerosPlotBox.layout().addWidget(self.polosCerosPlot.navToolBar)
        self.polosCerosPlotBox.layout().addWidget(self.polosCerosPlot)

        self.polosCerosEtapasPlot = PolosCerosPlot(parent=self.polosCerosEtapasPlotBox)
        self.polosCerosEtapasPlotBox.layout().addWidget(self.polosCerosEtapasPlot.navToolBar)
        self.polosCerosEtapasPlotBox.layout().addWidget(self.polosCerosEtapasPlot)

        self.infoPoloCeroPlot = PolosCerosPlot(parent=self.infoPoloCeroPlotBox)
        self.infoPoloCeroPlotBox.layout().addWidget(self.infoPoloCeroPlot.navToolBar)
        self.infoPoloCeroPlotBox.layout().addWidget(self.infoPoloCeroPlot)

        #Gráfico respuesta al escalón
        self.respuestaEscalonPlot = TemporalPlot(parent=self.respuestaEscalonPlotBox)
        self.respuestaEscalonPlotBox.layout().addWidget(self.respuestaEscalonPlot.navToolBar)
        self.respuestaEscalonPlotBox.layout().addWidget(self.respuestaEscalonPlot)

        #Gráfico Group Delay
        self.groupDelayPlot = GroupDelayPlot(parent=self.groupDelayPlotBox)
        self.groupDelayPlotBox.layout().addWidget(self.groupDelayPlot.navToolBar)
        self.groupDelayPlotBox.layout().addWidget(self.groupDelayPlot)

        # Textos Latex
        self.ordenQLatex = MPLTexText(self.ordenQLatexBox)
        self.infoLatex = MPLTexText(self.infoLatexBox)


        # Configuración de las pestañas y clicks
        self.crearPlantillaButton.clicked.connect(self.crearPlantilla)
        self.crearFiltroButton.clicked.connect(self.crearFiltro)
        self.graficarPlantillasButton.clicked.connect(self.graficarPlantillasFiltros)
        self.graficarFiltrosButton.clicked.connect(self.graficarPlantillasFiltros)
        self.obtenerEtapasButton.clicked.connect(self.obtenerEtapas)
        self.graficarRespEtapaButton.clicked.connect(self.graficarRespEtapa)
        self.cambiarOrdenFiltroButton.clicked.connect(self.cambiarOrdenFiltro)
        self.ordenQButton.clicked.connect(self.verOrdenQ)
        self.cambiarRangoFiltroButton.clicked.connect(self.cambiarRangoFiltro)
        self.mostrarInfoButton.clicked.connect(self.mostrarInfoEtapas)
        self.cambiarGananciaEtapasButton.clicked.connect(self.cambiarGananciaEtapas)


        self.borrarFiltrosButton.clicked.connect(self.deleteFiltros)
        self.borrarTodosFiltrosButton.clicked.connect(self.deleteAllFiltros)
        self.borrarPlantillasButton.clicked.connect(self.deletePlantillas)
        self.borrarTodasPlantillasButton.clicked.connect(self.deleteAllPlantillas)
        self.borrarEtapasButton.clicked.connect(self.deleteEtapas)


    def crearPlantilla(self):
        newPlantilla = PlantillaClass()

        text = self.tipoFiltroComboBox.currentText()

        if text == "Pasa Bajos":
            try:
                fp = float(self.fpLP.text())
                fa = float(self.faLP.text())
                ap= float(self.apVal.text())
                aa = float(self.aaVal.text())
            except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Ingresar un número valido")
                msgBox.setWindowTitle("Advertencia")
                msgBox.exec()
                return

            if fp >= fa:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Ingresar frecuencias válidas")
                msgBox.setWindowTitle("Advertencia")
                msgBox.exec()
                return

            newPlantilla.crearPasaBajos(fp, fa, ap, aa)

        elif text == "Pasa Altos":
            try:
                fp = float(self.fpHP.text())
                fa = float(self.faHP.text())
                ap = float(self.apVal.text())
                aa = float(self.aaVal.text())

            except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Ingresar un número valido")
                msgBox.setWindowTitle("Advertencia")
                msgBox.exec()
                return
            if fa >= fp:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Ingresar frecuencias válidas")
                msgBox.setWindowTitle("Advertencia")
                msgBox.exec()
                return

            newPlantilla.crearPasaAltos(fp, fa, ap, aa)

        elif text == "Pasa Banda":
            tipo = self.BPTypeComboBox.currentText()
            if tipo == "Anchos de Banda":
                try:
                    fo = float(self.f0BP.text())
                    dfp = float(self.dFpBP.text())
                    dfa = float(self.dFaBP.text())
                    ap = float(self.apVal.text())
                    aa = float(self.aaVal.text())

                except:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Ingresar un número valido")
                    msgBox.setWindowTitle("Advertencia")
                    msgBox.exec()
                    return

                if dfp >= dfa:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Ingresar frecuencias válidas")
                    msgBox.setWindowTitle("Advertencia")
                    msgBox.exec()
                    return

                newPlantilla.crearPasaBandaBW(fo, dfp, dfa, ap, aa)

            elif tipo == "Frecuencias":
                try:
                    fpx = float(self.fpXBP.text())
                    fpy = float(self.fpYBP.text())
                    fax = float(self.faXBP.text())
                    fay = float(self.faYBP.text())
                    ap = float(self.apVal.text())
                    aa = float(self.aaVal.text())
                except:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Ingresar un número valido")
                    msgBox.setWindowTitle("Advertencia")
                    msgBox.exec()
                    return

                if fax >= fpx or fay <= fpy:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Warning)
                        msgBox.setText("Ingresar frecuencias válidas")
                        msgBox.setWindowTitle("Advertencia")
                        msgBox.exec()
                        return

                newPlantilla.crearPasaBandaFreq(fpx, fpy, fax, fay, ap, aa)

        elif text == "Rechaza Banda":
            tipo = self.BSTypeComboBox.currentText()
            if tipo == "Anchos de Banda":
                try:
                    fo = float(self.f0BS.text())
                    dfp = float(self.dFpBS.text())
                    dfa = float(self.dFaBS.text())
                    ap = float(self.apVal.text())
                    aa = float(self.aaVal.text())

                except:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Ingresar un número valido")
                    msgBox.setWindowTitle("Advertencia")
                    msgBox.exec()
                    return

                if dfa >= dfp:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Ingresar frecuencias válidas")
                    msgBox.setWindowTitle("Advertencia")
                    msgBox.exec()
                    return

                newPlantilla.crearRechazaBandaBW(fo,dfp, dfa, ap, aa)

            elif tipo == "Frecuencias":
                try:
                    fpx = float(self.fpXBS.text())
                    fpy = float(self.fpYBS.text())
                    fax = float(self.faXBS.text())
                    fay = float(self.faYBS.text())
                    ap = float(self.apVal.text())
                    aa = float(self.aaVal.text())
                except:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Ingresar un número valido")
                    msgBox.setWindowTitle("Advertencia")
                    msgBox.exec()
                    return

                if fax <= fpx or fay>= fpy:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Warning)
                        msgBox.setText("Ingresar frecuencias válidas")
                        msgBox.setWindowTitle("Advertencia")
                        msgBox.exec()
                        return

                newPlantilla.crearRechazaBandaFreq(fpx, fpy, fax, fay, ap, aa)


        plantillaName, ok = QInputDialog.getText(self, "Agregar Plantilla", 'Nombre la plantilla: ')
        if not ok:
            return
        if len(plantillaName) < 1:
            plantillaName = "Plantilla " + str(len(self.listaPlantillas))

        newPlantilla.crearNombre(plantillaName)

        self.listaPlantillas.append(newPlantilla)

        item = QListWidgetItem(plantillaName)
        item.setCheckState(Qt.Checked)

        self.listPlantillasWidget.addItem(item)

    def crearFiltro(self):
        text = self.tipoAproxComboBox.currentText()
        rango = float(self.rangoPorcentaje.text()) / 100

        if text == "Butterworth":
            text = "butter"
        elif text == "Chebyshev I":
            text = "cheby1"
        elif text == "Chebyshev II (inverso)":
            text = "cheby2"
        elif text == "Cauer (elíptico)":
            text = "ellip"

        for i in range(len(self.listaPlantillas)):
            if self.listPlantillasWidget.item(i).checkState() == 2:
                filtroActual = FilterClass()
                p = self.listaPlantillas[i]

                if p.tipoPlantilla == "LP":
                    filtroActual.getLPTransferFunction(p.fp, p.fa, p.ap, p.aa, text, rango)

                elif p.tipoPlantilla == "HP":
                    filtroActual.getHPTransferFunction(p.fp, p.fa, p.ap, p.aa, text, rango)

                elif p.tipoPlantilla == "BPF":
                    filtroActual.getBPTransferFunctionFreq([p.fpx,p.fpy], [p.fax, p.fay], p.ap, p.aa, text, rango)

                elif p.tipoPlantilla == "BPBW":
                    filtroActual.getBPTransferFunctionBW(p.fo, p.dfp, p.dfa, p.ap, p.aa, text, rango)

                elif p.tipoPlantilla == "BSF":
                    filtroActual.getBSTransferFunctionFreq([p.fpx, p.fpy], [p.fax, p.fay], p.ap, p.aa, text, rango)

                elif p.tipoPlantilla == "BSBW":
                    filtroActual.getBSTransferFunctionBW(p.fo, p.dfp, p.dfa, p.ap, p.aa, text, rango)



                filtroName, ok = QInputDialog.getText(self, "Agregar Filtro", 'Nombre del filtro: ')
                if not ok:
                    return
                if len(filtroName) < 1:
                    filtroName = "Filtro " + str(len(self.listaFiltros))

                filtroActual.crearNombre(filtroName)

                self.listaFiltros.append(filtroActual)

                item = QListWidgetItem(filtroName)
                item.setCheckState(Qt.Checked)

                self.listFiltrosWidget.addItem(item)

                self.filtroComboBox.addItem(filtroName)

        self.filtroComboBox.clear()
        for i in range(len(self.listaFiltros)):
            self.filtroComboBox.addItem(self.listaFiltros[i].nombre)

        self.ordenQComboBox.clear()
        for i in range(len(self.listaFiltros)):
            self.ordenQComboBox.addItem(self.listaFiltros[i].nombre)


    '''
        Grafica las plantillas seleccionadas
    '''
    def graficarPlantillas(self):
        for i in range(len(self.listaPlantillas)):
            if self.listPlantillasWidget.item(i).checkState() == 2:
                tipo = self.listaPlantillas[i].tipoPlantilla
                if tipo == 'LP':
                    Fp = self.listaPlantillas[i].fp
                    Fa = self.listaPlantillas[i].fa
                    Ap = self.listaPlantillas[i].ap
                    Aa = self.listaPlantillas[i].aa
                    self.ganMagPlot.addLPPlantilla(Fp, Fa, Ap, Aa)
                    self.atenMagPlot.addLPPlantillaAten(Fp, Fa, Ap, Aa)

                elif tipo == 'HP':
                    Fp = self.listaPlantillas[i].fp
                    Fa = self.listaPlantillas[i].fa
                    Ap = self.listaPlantillas[i].ap
                    Aa = self.listaPlantillas[i].aa
                    self.ganMagPlot.addHPPlantilla(Fp, Fa, Ap, Aa)
                    self.atenMagPlot.addHPPlantillaAten(Fp, Fa, Ap, Aa)

                elif tipo == 'BPF' or tipo == 'BPBW':
                    Fpx = self.listaPlantillas[i].fpx
                    Fpy = self.listaPlantillas[i].fpy
                    Fax = self.listaPlantillas[i].fax
                    Fay = self.listaPlantillas[i].fay
                    Ap = self.listaPlantillas[i].ap
                    Aa = self.listaPlantillas[i].aa
                    self.ganMagPlot.addBPPlantilla(Fpx, Fpy, Fax, Fay, Ap, Aa)
                    self.atenMagPlot.addBPPlantillaAten(Fpx, Fpy, Fax, Fay, Ap, Aa)

                elif tipo == 'BSF' or tipo == 'BSBW':
                    Fpx = self.listaPlantillas[i].fpx
                    Fpy = self.listaPlantillas[i].fpy
                    Fax = self.listaPlantillas[i].fax
                    Fay = self.listaPlantillas[i].fay
                    Ap = self.listaPlantillas[i].ap
                    Aa = self.listaPlantillas[i].aa
                    self.ganMagPlot.addBSPlantilla(Fpx, Fpy, Fax, Fay, Ap, Aa)
                    self.atenMagPlot.addBSPlantillaAten(Fpx, Fpy, Fax, Fay, Ap, Aa)


    def graficarFiltros(self):
        for i in range(len(self.listaFiltros)):
            if self.listFiltrosWidget.item(i).checkState() == 2:
                try:
                    minFreq = float(self.minFreq.text())
                    maxFreq = float(self.maxFreq.text())
                    w1 = np.logspace(np.log10(minFreq * 2 * np.pi), np.log10(maxFreq * 2 * np.pi), 1000)
                    x = True
                except:
                    w1 = None
                    x = False
                w, m, p = self.listaFiltros[i].getBode(w1, x)
                label = self.listaFiltros[i].getName()
                self.ganMagPlot.addCurveMag(w/(2*np.pi),m, label)
                self.atenMagPlot.addCurveMagAten(w/(2*np.pi),m, label)
                self.ganFasePlot.addCurveFase(w/(2*np.pi), p, label)
                self.atenFasePlot.addCurveFaseAten(w/(2*np.pi),p, label)

                # grafico la plantilla normalizada
                w2, m2, p2 = self.listaFiltros[i].getBodeNormalized(None, False)
                self.curvaNormalizadaPlot.addNormalizedMagCurve(w2, 10**(m2/20), label)

                #grafico el group delay
                delay = -np.diff(np.unwrap(p * np.pi / 180)) / np.diff(w)
                freq = w/(2*np.pi)
                freqDelay = freq[1:]
                self.groupDelayPlot.addGroupDelayPlot(freqDelay, delay, label)


    def graficarPolosZeros(self):
        for i in range(len(self.listaFiltros)):
            if self.listFiltrosWidget.item(i).checkState() == 2:
                polos, ceros = self.listaFiltros[i].getPolesZeros()
                label = self.listaFiltros[i].getName()
                self.polosCerosPlot.addCurvePolosCeros(polos, ceros, label)

    def graficarRespuestaEscalon(self):
        for i in range(len(self.listaFiltros)):
            if self.listFiltrosWidget.item(i).checkState() == 2:
                t, y = ss.step(self.listaFiltros[i].currentTransferFunction, N = 1000)
                label = self.listaFiltros[i].getName()
                self.respuestaEscalonPlot.addTemporalPlot(t,y,label)


    def graficarPlantillasFiltros(self):
        self.ganMagPlot.clear()
        self.ganFasePlot.clear()
        self.atenMagPlot.clear()
        self.atenFasePlot.clear()
        self.curvaNormalizadaPlot.clear()
        self.polosCerosPlot.clear()
        self.respuestaEscalonPlot.clear()
        self.groupDelayPlot.clear()

        self.graficarPlantillas()
        self.graficarFiltros()
        self.graficarPolosZeros()
        self.graficarRespuestaEscalon()


        self.ganMagPlot.plotMag()
        self.ganFasePlot.plotFase()
        self.atenMagPlot.plotMag()
        self.atenFasePlot.plotFase()
        self.curvaNormalizadaPlot.plotNormalizedMag()
        self.polosCerosPlot.plotPolosCeros()
        self.respuestaEscalonPlot.plotTemporalPlot()
        self.groupDelayPlot.plotTGroupDelay()

    '''
        Cambiar orden del filtro
    '''
    def cambiarOrdenFiltro(self):
        for i in range(len(self.listaFiltros)):
            if self.listFiltrosWidget.item(i).checkState() == 2:
                ordenActual = self.listaFiltros[i].currentN
                minimoOrden = self.listaFiltros[i].n
                ordenNuevo, ok = QInputDialog.getText(self, "Cambiar orden del filtro", 'Orden actual: '+ str(ordenActual)+', Orden mínimo: '+ str(minimoOrden))
                if not ok:
                    return
                if len(ordenNuevo) < 1:
                    ordenNuevo = ordenActual

                ordenNuevo = int(ordenNuevo)
                if ordenNuevo < minimoOrden:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("El nuevo orden no puede ser menor al orden mínimo!")
                    msgBox.setWindowTitle("Advertencia")
                    msgBox.exec()
                    return

                self.listaFiltros[i].changeFilterOrder(ordenNuevo)

    '''
        Cambiar rango de desnormalización
    '''
    def cambiarRangoFiltro(self):
        for i in range(len(self.listaFiltros)):
            if self.listFiltrosWidget.item(i).checkState() == 2:
                rangoActual = self.listaFiltros[i].rango
                rangoNuevo, ok = QInputDialog.getText(self, "Cambiar rango de desnormalización", 'Rango actual: '+ str(rangoActual * 100))
                if not ok:
                    return
                if len(rangoNuevo) < 1:
                    rangoNuevo = rangoActual

                rangoNuevo = float(rangoNuevo)/100

                self.listaFiltros[i].aplicarRangoDesnormalizacion(rangoNuevo)

    '''
        Muestra orden mínimo, actual y Q
    '''
    def verOrdenQ(self):
        index = self.ordenQComboBox.currentIndex()
        filtroActual = self.listaFiltros[index]

        Nmin = filtroActual.n
        Nactual = filtroActual.currentN

        poles = filtroActual.currentTransferFunction.poles
        maxQ = 0

        for i in range(len(poles)):
            q = np.abs(np.abs(poles[i]) / (2*np.real(poles[i])))
            if q > maxQ:
                maxQ = q

        stri = "Orden mínimo: "+ "$" + str(Nmin) +"$\n"
        stri += "Orden actual: " + "$" + str(Nactual) +"$\n"
        stri += "Máximo Q: " + "$" + str(maxQ) +"$\n"

        self.ordenQLatex.updateTex(stri)

    '''
        Obtiene las etapas del filtro seleccionado
    '''
    def obtenerEtapas(self):
        numberOfFunctions = len(self.listaEtapas)
        for i in range(numberOfFunctions):
            self.listaEtapasWidget.takeItem(numberOfFunctions - 1 - i)

        self.listaEtapas.clear()
        self.listaGananciaEtapas.clear()
        self.listaGananciaNominalEtapas.clear()

        index = self.filtroComboBox.currentIndex()
        filtroActual = self.listaFiltros[index]

        self.filtroParaEtapas = filtroActual
        self.listaSOS = filtroActual.getSOS()

        totalTF = self.filtroParaEtapas.currentTransferFunction

        poles = totalTF.poles
        zeros = totalTF.zeros
        gain = totalTF.gain

        gananciaNormalizadaTotal = gain

        factorIndividual = gananciaNormalizadaTotal ** (1 / len(self.listaSOS))  # ganancia normalizada por etapa (misma)

        self.infoEtapaComboBox.clear()

        kTotal = 1

        for i in range(len(self.listaSOS)):
            numer = [self.listaSOS[i][0], self.listaSOS[i][1], self.listaSOS[i][2]]
            denom = [self.listaSOS[i][3], self.listaSOS[i][4], self.listaSOS[i][5]]

            tf = ss.TransferFunction(numer, denom)

            tf = tf.to_zpk()

            z = tf.zeros
            p = tf.poles
            k = 1

            auxtf = ss.ZerosPolesGain(z,p,k).to_tf()

            num = auxtf.num
            den = auxtf.den

            if len(den) == 2:
                if len(num) == 0:
                    k = den[1]
                elif num[1] == 0:
                    k = 1
                else:
                    k = den[1] / num[1]

            elif len(den) == 3:
                if len(num) == 1:
                    k = den[2]
                elif len(num) == 2:
                    if num[1] == 0:
                        k = den[1]
                    else:
                        k = den[2] / num[1]
                elif len(num) == 3:
                    if num[2] == 0:
                        k = 1
                    else:
                        k = den[2] / num[2]

            newTF = ss.ZerosPolesGain(z, p, k)

            self.listaGananciaNominalEtapas.append(k)
            self.listaEtapas.append(newTF)

            kTotal *= k #actualizo la ganancia total

        factoNormalizacion = (gain / kTotal) ** (1/len( self.listaEtapas))

        for i in range(len(self.listaEtapas)):

            z = self.listaEtapas[i].zeros
            p = self.listaEtapas[i].poles
            k = self.listaEtapas[i].gain

            newTF = ss.ZerosPolesGain(z,p,factoNormalizacion*k)

            self.listaGananciaEtapas.append(factoNormalizacion)

            self.listaEtapas[i] = newTF

            item = QListWidgetItem("Etapa " + str(i))
            item.setCheckState(Qt.Checked)

            self.listaEtapasWidget.addItem(item)

            self.infoEtapaComboBox.addItem("Etapa " + str(i))

        self.polosCerosEtapasPlot.clear()
        self.polosCerosEtapasPlot.addCurvePolosCeros(poles, zeros, label = filtroActual.nombre)
        self.polosCerosEtapasPlot.plotPolosCeros()

    def cambiarGananciaEtapas(self):
        for i in range(len(self.listaSOS)):
            if self.listaEtapasWidget.item(i).checkState() == 2:
                gan = 20*np.log10(self.listaGananciaEtapas[i])
                ganancia, ok = QInputDialog.getText(self, "Cambiar ganancia", 'Ganancia actual: ' + str(gan) + 'dB ' + '\nNueva ganancia: ')
                if not ok:
                    return

                if len(ganancia) < 1:
                    nuevaGan = gan
                else:
                    nuevaGan = 10**(float(ganancia)/20)

                z = self.listaEtapas[i].zeros
                p = self.listaEtapas[i].poles
                k = self.listaGananciaNominalEtapas[i]

                newTF = ss.ZerosPolesGain(z, p, nuevaGan * k)

                self.listaGananciaEtapas[i] = nuevaGan

                self.listaEtapas[i] = newTF

    '''
        Graficar respuesta en frecuencia etapas
    '''
    def graficarRespEtapa(self):
        etapasPolos = []
        etapasZeros = []
        gananciaAcum = 1

        for i in range(len(self.listaSOS)):
            if self.listaEtapasWidget.item(i).checkState() == 2:
                z = self.listaEtapas[i].zeros
                p = self.listaEtapas[i].poles
                k = self.listaEtapas[i].gain

                for pole in p:
                    etapasPolos.append(pole)
                for zero in z:
                    etapasZeros.append(zero)

                gananciaAcum *= k

        self.currentEtapasTF = ss.ZerosPolesGain(etapasZeros, etapasPolos, gananciaAcum)

        self.etapaGanMagPlot.clear()
        self.etapaGanFasePlot.clear()

        w, m, p = ss.bode(self.currentEtapasTF, n = 1000)
        label = 'Etapas'
        self.etapaGanMagPlot.addCurveMag(w / (2 * np.pi), m, label)
        self.etapaGanFasePlot.addCurveFase(w / (2 * np.pi), p, label)

        self.etapaGanMagPlot.plotMag()
        self.etapaGanFasePlot.plotFase()

    def mostrarInfoEtapas(self):
        index = self.infoEtapaComboBox.currentIndex()
        label = self.infoEtapaComboBox.currentText()
        tf2 = self.listaEtapas[index]

        frase = ''

        poles = tf2.poles
        zeros = tf2.zeros

        tf = tf2.to_tf()

        num = tf.num
        den = tf.den

        tfLatex = self.tf2Tex(num, den)

        frase += tfLatex + '\n'

        #Numerador
        if len(zeros) == 1:
            frase += "Num: $n = 1; f0 = " + self.formatedNum(zeros[0]/(2*np.pi)) + 'Hz$\n'
        elif len(zeros) == 2:
            if np.imag(zeros[0]) == 0:
                frase += "Num: $n = 1; f0 = " + self.formatedNum(zeros[0]/(2*np.pi)) + 'Hz; '
                frase += "n = 1; f0 = " + self.formatedNum(zeros[1] / (2 * np.pi)) + 'Hz$\n'
            else:
                frase += "Num: $n = 2; f0 = " + self.formatedNum(np.abs(zeros[0]) / (2 * np.pi)) + 'Hz; '
                frase += "Q = " + self.formatedNum(np.abs(np.abs(zeros[0]) / (2*np.real(zeros[0])))) + '$\n'

        # Denominador
        if len(poles) == 1:
            frase += "Den: $n = 1; f0 = " + self.formatedNum(poles[0] / (2 * np.pi)) + 'Hz$\n'
        elif len(poles) == 2:
            if np.imag(poles[0]) == 0:
                frase += "Den: $n = 1; f0 = " + self.formatedNum(poles[0] / (2 * np.pi)) + 'Hz; '
                frase += "n = 1, f0 = " + self.formatedNum(poles[1] / (2 * np.pi)) + 'Hz$\n'
            else:
                frase += "Den: $n = 2; f0 = " + self.formatedNum(np.abs(poles[0]) / (2 * np.pi)) + 'Hz; '
                frase += "Q = " + self.formatedNum(np.abs(np.abs(poles[0]) / (2 * np.real(poles[0])))) + '$\n'

        self.infoLatex.updateTex(frase)

        self.infoPoloCeroPlot.clear()

        self.infoPoloCeroPlot.addCurvePolosCeros(poles, zeros, label = label)

        self.infoPoloCeroPlot.plotPolosCeros()


    '''
        Funciones que eliminan cosas
    '''
    def deletePlantillas(self):
        numberOfFunctions = len(self.listaPlantillas)
        for i in range(numberOfFunctions):
            if self.listPlantillasWidget.item(numberOfFunctions-1-i).checkState() == 2:
                self.listPlantillasWidget.takeItem(numberOfFunctions-1-i)
                self.listaPlantillas.pop(numberOfFunctions-1-i)

    def deleteAllPlantillas(self):
        numberOfFunctions = len(self.listaPlantillas)
        for i in range(numberOfFunctions):
            self.listPlantillasWidget.takeItem(numberOfFunctions - 1 - i)
            self.listaPlantillas.pop(numberOfFunctions - 1 - i)

    def deleteFiltros(self):
        numberOfFunctions = len(self.listaFiltros)
        for i in range(numberOfFunctions):
            if self.listFiltrosWidget.item(numberOfFunctions-1-i).checkState() == 2:
                self.listFiltrosWidget.takeItem(numberOfFunctions-1-i)
                self.listaFiltros.pop(numberOfFunctions-1-i)

        self.filtroComboBox.clear()
        for i in range(len(self.listaFiltros)):
            self.filtroComboBox.addItem(self.listaFiltros[i].nombre)

        self.ordenQComboBox.clear()
        for i in range(len(self.listaFiltros)):
            self.ordenQComboBox.addItem(self.listaFiltros[i].nombre)

    def deleteAllFiltros(self):
        numberOfFunctions = len(self.listaFiltros)
        for i in range(numberOfFunctions):
            self.listFiltrosWidget.takeItem(numberOfFunctions - 1 - i)
            self.listaFiltros.pop(numberOfFunctions - 1 - i)

        self.filtroComboBox.clear()
        for i in range(len(self.listaFiltros)):
            self.filtroComboBox.addItem(self.listaFiltros[i].nombre)

        self.ordenQComboBox.clear()
        for i in range(len(self.listaFiltros)):
            self.ordenQComboBox.addItem(self.listaFiltros[i].nombre)


    def deleteEtapas(self):
        numberOfFunctions = len(self.listaSOS)
        for i in range(numberOfFunctions):
            self.listaEtapasWidget.takeItem(numberOfFunctions - 1 - i)
            self.listaEtapas.pop(numberOfFunctions - 1 - i)

        self.infoEtapaComboBox.clear()

    def formatedNum(self, num) -> str:
        return "{0:.2f}".format(num)

    def tf2Tex(self,num, den) -> str:
        return "$H(s) = \\frac{" + self.arrToPol(num) + "}{" + self.arrToPol(den) + "}$ "

    def arrToPol(self,arr=[], var='s'):

        pol = ''
        for i in range(len(arr)):
            q = len(arr) - i - 1
            if arr[i] != 0:
                if pol and arr[i] > 0:
                    pol += ' + '

                if abs(arr[i]) != 1 or q < 1:
                    base, exp = self.toBaseExp(arr[i])
                    if (exp < -1 or exp > 3):
                        pol += str(base) + '\\times10^{' + str(exp) + '}\ '
                    else:
                        pol += "{:.2f}".format(arr[i]) + '\ '
                elif arr[i] == -1:
                    pol += '-'

                if q > 1:
                    pol += var + '^{' + str(q) + '}'
                elif q == 1:
                    pol += var

        return pol if pol else '0'

    def toBaseExp(self,num):
        str = "{:.2e}".format(num)
        return (float(str[:4]), int(str[-3:]))










