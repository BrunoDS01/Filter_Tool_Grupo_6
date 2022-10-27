from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import Rectangle
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
        self.axes.add_patch(Rectangle((Fp, -Ap), - (Fp - Fp / 5), -(Ap * 2 - Ap), color='blue'))
        self.axes.add_patch(Rectangle((Fa, -Aa), (Fa), (0 + Aa), color='blue'))

    def addHPPlantilla(self, Fp, Fa, Ap, Aa):
        self.axes.add_patch(Rectangle((Fp, -Ap), (Fp), -(Ap * 2 - Ap), color='blue'))
        self.axes.add_patch(Rectangle((Fa, -Aa), -(Fa - Fa/5), (0 + Aa), color='blue'))

    def addBSPlantilla(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.axes.add_patch(Rectangle((Fpx, -Ap), - (Fpx - Fpx / 5), -(Ap * 2 - Ap), color='blue'))
        self.axes.add_patch(Rectangle((Fax, -Aa), (Fay-Fax), (0 + Aa), color='blue'))
        self.axes.add_patch(Rectangle((Fpy, -Ap), (Fpy), -(Ap * 2 - Ap), color='blue'))

    def addBPPlantilla(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.axes.add_patch(Rectangle((Fax, -Aa), -(Fax - Fax/5), (0 + Aa), color='blue'))
        self.axes.add_patch(Rectangle((Fpx, -Ap), (Fpy -Fpx), -(Ap * 2 - Ap), color='blue'))
        self.axes.add_patch(Rectangle((Fay, -Aa), (Fay), (0 + Aa), color='blue'))


    def addLPPlantillaAten(self, Fp, Fa, Ap, Aa):
        self.addLPPlantilla(Fp, Fa, -Ap, -Aa)

    def addHPPlantillaAten(self, Fp, Fa, Ap, Aa):
        self.addHPPlantilla(Fp, Fa, -Ap, -Aa)

    def addBPPlantillaAten(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.addBPPlantilla(Fpx, Fpy, Fax, Fay, -Ap, -Aa)

    def addBSPlantillaAten(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.addBSPlantilla(Fpx, Fpy, Fax, Fay, -Ap, -Aa)

    def addNormalizedMagCurve(self, w, mag, label):
        self.axes.plot(w, mag, label=label)

    def plotMag(self):
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('|H| [dB]')
        self.axes.set_xscale('log')

        self.axes.legend(loc=0)
        self.axes.grid(visible = True, which = 'both', axis = 'both')

        self.fig.canvas.draw()

    def plotFase(self):
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Fase (°)')
        self.axes.set_xscale('log')
        self.axes.grid(visible=True, which='both', axis='both')

        self.axes.legend(loc=0)

        self.fig.canvas.draw()

    def plotNormalizedMag(self):
        self.axes.set_xlabel('Frecuencia [rad/s]')
        self.axes.set_ylabel('Ganancia [veces]')
        self.axes.set_xscale('linear')

        self.axes.legend(loc=0)
        self.axes.grid(visible=True, which='both', axis='both')

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

class TemporalPlot(MplCanvas):
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)

    def addTemporalPlot(self, t, y, label):
        self.axes.plot(t, y, label = label)

    def plotTemporalPlot(self):
        self.axes.set_xlabel('Tiempo [s]')
        self.axes.set_ylabel('Tensión [V]')
        self.axes.set_xscale('linear')

        self.axes.legend(loc=0)
        self.axes.grid(visible=True, which='both', axis='both')

        self.fig.canvas.draw()

class GroupDelayPlot(MplCanvas):
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)

    def addGroupDelayPlot(self, f, gd, label):
        self.axes.plot(f, gd, label = label)

    def plotTGroupDelay(self):
        self.axes.set_xlabel('Frecuencia [Hz]')
        self.axes.set_ylabel('Group Delay [s]')
        self.axes.set_xscale('log')

        self.axes.legend(loc=0)
        self.axes.grid(visible=True, which='both', axis='both')

        self.fig.canvas.draw()

