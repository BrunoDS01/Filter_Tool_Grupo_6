from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot()
        self.fig.set_tight_layout(True)
        super().__init__(self.fig)
        self.navToolBar = NavigationToolbar(self, parent=parent)

    def clear(self):
        self.axes.clear()

class BodePlot(MplCanvas):
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)

    def addCurveMag(self, w, mag, label):
        self.axes.semilogx(w, mag, label = label)

    def addCurveMagAten(self, w, mag, label):
        self.axes.semilogx(w, -mag, label=label)

    def addCurveFase(self, w, fase, label):
        self.axes.semilogx(w, fase, label = label)

    def addCurveFaseAten(self, w, fase, label):
        self.axes.semilogx(w, fase, label=label)

    def addLPPlantilla(self, Fp, Fa, Ap, Aa):
        self.axes.fill([Fp / 10, Fp, Fp, Fp / 10], [-Ap, -Ap, -Ap*2, -Ap*2], '0.9', lw=0)
        self.axes.fill([Fa, Fa*10, Fa*10, Fa], [0, 0, -Aa, -Aa], '0.9', lw=0)

    def addHPPlantilla(self, Fp, Fa, Ap, Aa):
        self.axes.fill([Fa / 10, Fa, Fa, Fa / 10], [0, 0, -Aa, -Aa], '0.9', lw=0)
        self.axes.fill([Fp, Fp * 10, Fp * 10, Fp], [-Ap, -Ap, -Ap*2, -Ap*2], '0.9', lw=0)

    def addBSPlantilla(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.axes.fill([Fpx / 10, Fpx, Fpx, Fpx / 10], [-Ap, -Ap, -Ap*2, -Ap*2], '0.9', lw=0)
        self.axes.fill([Fax, Fay, Fay, Fax], [0, 0, -Aa, -Aa], '0.9', lw=0)
        self.axes.fill([Fpy, Fpy * 10, Fpy * 10, Fpy], [-Ap, -Ap, -Ap*2, -Ap*2], '0.9', lw=0)

    def addBPPlantilla(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.axes.fill([Fax / 10, Fax, Fax, Fax / 10], [0, 0, -Aa, -Aa], '0.9', lw=0)
        self.axes.fill([Fpx, Fpy, Fpy, Fpx], [-Ap, -Ap, -Ap*2, -Ap*2], '0.9', lw=0)
        self.axes.fill([Fay, Fay * 10, Fay * 10, Fay], [0, 0, -Aa, -Aa], '0.9', lw=0)

    def addLPPlantillaAten(self, Fp, Fa, Ap, Aa):
        self.addLPPlantilla(Fp, Fa, -Ap, -Aa)

    def addHPPlantillaAten(self, Fp, Fa, Ap, Aa):
        self.addHPPlantilla(Fp, Fa, -Ap, -Aa)

    def addBPPlantillaAten(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.addBPPlantilla(Fpx, Fpy, Fax, Fay, -Ap, -Aa)

    def addBSPlantillaAten(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.addBSPlantilla(Fpx, Fpy, Fax, Fay, -Ap, -Aa)

    def plotMag(self):
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('|H| [dB]')
        self.axes.set_xscale('log')

        self.axes.legend(loc=0)

        self.fig.canvas.draw()

    def plotFase(self):
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Fase (°)')
        self.axes.set_xscale('log')

        self.axes.legend(loc=0)

        self.fig.canvas.draw()

class PolosCerosPlot(MplCanvas):
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)

    def addCurvePolosCeros(self, poles, zeros, label):
        if len(poles) != 0:
            self.axes.scatter(np.real(poles), np.imag(poles), marker='x', label='Polos ' + label)

        if len(zeros) != 0:
            self.axes.scatter(np.real(zeros), np.imag(zeros), marker='o', label='Ceros ' + label)


    def plotPolosCeros(self):
        self.axes.axis('equal')
        self.axes.ticklabel_format(axis='both', style='sci')
        self.axes.grid(visible=True)
        self.axes.axhline(0, color='black', linewidth=1)
        self.axes.axvline(0, color='black', linewidth=1)  # marcamos los ejes

        self.axes.set_ylabel('jω')
        self.axes.set_xlabel('σ')

        self.axes.legend(loc=0)

        self.fig.canvas.draw()

