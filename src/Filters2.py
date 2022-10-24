import numpy as np
import scipy.signal as ss
import sympy as sp
from sympy.abc import s,w
from sympy.functions.special import polynomials as poly

Epsilon = 1e-5

class FilterClass:
    def __init__(self):

        self.nombre = None

        self.transferFunction = ss.TransferFunction(1,1)    #transferencia final orden minimo
        self.tfLP = ss.TransferFunction(1,1)               #transferencia del pasabajos orden minimo

        self.currentTransferFunction = ss.TransferFunction(1,1)  # transferencia final
        self.currentTFLP = ss.TransferFunction(1,1)             #transferencia pasa bajos
        self.currentLPRango = ss.TransferFunction(1,1)          #transferencia pasa bajos con rango

        self.filterType = None          #Tipo de filtro
        self.filterName = None
        self.n = 1
        self.Wp = 1                  #Frecuencias del pasa bajos normalizado
        self.Wa = 2
        self.Ap = 3
        self.Aa = 10
        self.rango = 0

        self.Fp = None
        self.Fo = None
        self.dFp = None

        self.currentN = 1            #nuevo N
        self.Wan = 2              # nuevo Wan

    def crearNombre(self, nombre):
        self.nombre = nombre

    '''
        Low Pass
    '''
    def getLPTransferFunction(self, Fp, Fa, Ap, Aa, btype, rango):

        self.filterType = "LP"
        self.filterName = btype
        self.rango = rango

        Wp = 1
        Wa = Fa / Fp

        self.Wp = Wp
        self.Wa = Wa
        self.Ap = Ap
        self.Aa = Aa
        self.Fp = Fp

        b1, a1, N = self.findLowPassNormalizedFilter(Wp, Wa, Ap, Aa, btype)
        self.tfLP = ss.TransferFunction(b1,a1)
        self.currentTFLP = ss.TransferFunction(b1, a1)
        self.n = N

        b, a = ss.lp2lp(b1, a1, Fp * 2 * np.pi)
        self.transferFunction = ss.TransferFunction(b,a)

        self.currentTransferFunction = self.aplicarRangoDesnormalización(rango)

        return self.currentTransferFunction

    '''
        High Pass
    '''
    def getHPTransferFunction(self, Fp, Fa, Ap, Aa, btype, rango):
        self.filterType = "HP"
        self.filterName = btype
        self.rango = rango

        Wp = 1
        Wa = 2 * np.pi * Fp / (Fa * 2 * np.pi)

        self.Wp = Wp
        self.Wa = Wa
        self.Ap = Ap
        self.Aa = Aa
        self.Fp = Fp

        b1, a1, N = self.findLowPassNormalizedFilter(Wp, Wa, Ap, Aa, btype)
        self.tfLP = ss.TransferFunction(b1, a1)
        self.currentTFLP = ss.TransferFunction(b1, a1)
        self.n = N

        b, a = ss.lp2hp(b1,a1, Fp * 2 * np.pi)

        self.transferFunction = ss.TransferFunction(b, a)
        self.currentTransferFunction = self.aplicarRangoDesnormalización(rango)

        return self.currentTransferFunction

    '''
        Band Pass con ANCHOS DE BANDA
    '''
    def getBPTransferFunctionBW(self, Fo, dFp, dFa, Ap, Aa, btype, rango):
        self.filterType = "BP"
        self.filterName = btype
        self.rango = rango

        #Fa = dFa / 2 + np.sqrt((dFa**2 + 4 * Fo**2)) / 2        # Hallo el valor de la frecuencia de atenuación más alta

        Wp = 1
        Wa = dFa / dFp

        self.Wp = Wp
        self.Wa = Wa
        self.Ap = Ap
        self.Aa = Aa

        self.Fo = Fo
        self.dFp = dFp

        b1, a1, N = self.findLowPassNormalizedFilter(Wp, Wa, Ap, Aa, btype)
        self.tfLP = ss.TransferFunction(b1, a1)
        self.currentTFLP = ss.TransferFunction(b1, a1)
        self.n = N

        b, a = ss.lp2bp(b1, a1, Fo * 2 * np.pi, dFp * 2 *np.pi)

        self.transferFunction = ss.TransferFunction(b, a)
        self.currentTransferFunction = self.aplicarRangoDesnormalización(rango)

        return self.currentTransferFunction

    '''
        Band Pass con FRECUENCIAS CRÍTICAS
    '''
    def getBPTransferFunctionFreq(self, Fps, Fas, Ap, Aa, btype, rango):
        self.filterType = "BP"
        self.filterName = btype
        self.rango = rango

        Fo = np.sqrt(Fps[0]*Fps[1])
        Fp = Fps[1]

        dFp = Fps[1] - Fps[0]
        self.dFp = dFp

        Fa = 1

        if (Fas[1] / Fo < Fo / Fas[0]):
            Fa = Fas[1]
            dFa = Fa - Fo ** 2 / Fa

        else:
            Fa = Fas[0]
            dFa = Fo ** 2 / Fa - Fa

        Wp = 1
        Wa = dFa / dFp

        self.Wp = Wp
        self.Wa = Wa
        self.Ap = Ap
        self.Aa = Aa

        self.Fo = Fo
        self.dFp = dFp

        b1, a1, N = self.findLowPassNormalizedFilter(Wp, Wa, Ap, Aa, btype)
        self.tfLP = ss.TransferFunction(b1, a1)
        self.currentTFLP = ss.TransferFunction(b1, a1)
        self.n = N


        b, a = ss.lp2bp(b1, a1, Fo * 2 * np.pi, dFp * 2 * np.pi)

        self.transferFunction = ss.TransferFunction(b, a)
        self.currentTransferFunction = self.aplicarRangoDesnormalización(rango)

        return self.currentTransferFunction

    '''
        Band Stop con ANCHOS DE BANDA
    '''
    def getBSTransferFunctionBW(self, Fo, dFp, dFa, Ap, Aa, btype, rango):
        self.filterType = "BS"
        self.filterName = btype
        self.rango = rango


        Wp = 1
        Wa = dFp / dFa

        self.Wp = Wp
        self.Wa = Wa
        self.Ap = Ap
        self.Aa = Aa

        self.Fo = Fo
        self.dFp = dFp

        b1, a1, N = self.findLowPassNormalizedFilter(Wp, Wa, Ap, Aa, btype)
        self.tfLP = ss.TransferFunction(b1, a1)
        self.currentTFLP = ss.TransferFunction(b1, a1)
        self.n = N

        b, a = ss.lp2bs(b1, a1, Fo * 2 * np.pi, dFp * 2 * np.pi)

        self.transferFunction = ss.TransferFunction(b, a)
        self.currentTransferFunction = self.aplicarRangoDesnormalización(rango)

        return self.currentTransferFunction

    '''
        Band Stop con FRECUENCIAS CRÍTICAS
    '''
    def getBSTransferFunctionFreq(self, Fps, Fas, Ap, Aa, btype, rango):
        self.filterType = "BS"
        self.filterName = btype
        self.rango = rango

        Fo = np.sqrt(Fps[0] * Fps[1])
        Fp = Fps[1]

        dFp = Fps[1] - Fps[0]

        if (Fas[1] / Fo > Fo / Fas[0]):
            Fa = Fas[1]
            dFa = Fa - Fo ** 2 / Fa

        else:
            Fa = Fas[0]
            dFa = Fo ** 2 / Fa - Fa

        Wp = 1
        Wa = dFp / dFa

        self.Wp = Wp
        self.Wa = Wa
        self.Ap = Ap
        self.Aa = Aa

        self.Fo = Fo
        self.dFp = dFp

        b1, a1, N = self.findLowPassNormalizedFilter(Wp, Wa, Ap, Aa, btype)
        self.tfLP = ss.TransferFunction(b1, a1)
        self.currentTFLP = ss.TransferFunction(b1, a1)
        self.n = N

        b, a = ss.lp2bs(b1, a1, Fo * 2 * np.pi, dFp * 2 * np.pi)

        self.transferFunction = ss.TransferFunction(b, a)
        self.currentTransferFunction = self.aplicarRangoDesnormalización(rango)

        return self.currentTransferFunction

    '''
        Cambiar el orden del filtro
    '''
    def changeFilterOrder(self, N):

        b1 = [1]
        a1 = [1]

        if self.filterName == "butter":
            Wan1 = 10 ** (np.log10((10 ** (self.Aa / 10) - 1) / (10 ** (self.Ap / 10) - 1)) / (2 * N))
            Wan2 = 10 ** (np.log10((10 ** (self.Aa / 10) - 1) / (10 ** (self.Ap / 10) - 1)) / (2 * (N-1)))

            Wan = (Wan1 + Wan2) / 2

            self.Wan = Wan

            N1, Wn = ss.buttord(self.Wp, Wan, self.Ap, self.Aa, True)
            self.currentN = N1                                      #N1 debería ser igual a N
            b1, a1 = ss.butter(N1, Wn, 'lowpass', analog=True)
            self.currentTFLP = ss.TransferFunction(b1, a1)

        elif self.filterName == "cheby1":
            Wan1 = np.cosh(np.arccosh(np.sqrt((10 ** (self.Aa / 10) - 1) / (10 ** (self.Ap / 10) - 1))) / (N))
            Wan2 = np.cosh(np.arccosh(np.sqrt((10 ** (self.Aa / 10) - 1) / (10 ** (self.Ap / 10) - 1))) / (N-1))

            Wan = (Wan1 + Wan2) / 2

            self.Wan = Wan

            N1, Wn = ss.cheb1ord(self.Wp, Wan, self.Ap, self.Aa, True)
            self.currentN = N1  # N1 debería ser igual a N
            b1, a1 = ss.cheby1(N1, self.Ap, Wn, 'lowpass', analog=True)
            self.currentTFLP = ss.TransferFunction(b1, a1)


        elif self.filterName == "cheby2":
            Wan1 = np.cosh(np.arccosh(np.sqrt((10 ** (self.Aa / 10) - 1) / (10 ** (self.Ap / 10) - 1))) / (N))
            Wan2 = np.cosh(np.arccosh(np.sqrt((10 ** (self.Aa / 10) - 1) / (10 ** (self.Ap / 10) - 1))) / (N - 1))

            Wan = (Wan1 + Wan2) / 2

            self.Wan = Wan

            N1, Wn = ss.cheb2ord(self.Wp, Wan, self.Ap, self.Aa, True)
            self.currentN = N1  # N1 debería ser igual a N
            b1, a1 = ss.cheby2(N1, self.Aa, Wn, 'lowpass', analog=True)
            self.currentTFLP = ss.TransferFunction(b1, a1)

        elif self.filterName == "ellip":

            self.currentN = N  # N1 debería ser igual a N
            b1, a1 = ss.ellip(N, self.Ap, self.Aa, self.Wp, 'lowpass', analog=True) #debería funcionar
            self.currentTFLP = ss.TransferFunction(b1, a1)

        self.currentTransferFunction = self.aplicarRangoDesnormalización(self.rango)

        return self.currentTransferFunction

    def findLowPassNormalizedFilter(self, Wp, Wa, Ap, Aa, btype):
        b1 = [1]
        a1 = [1]

        if (btype == "butter"):
            N, Wn = ss.buttord(Wp, Wa, Ap, Aa, True)
            b1, a1 = ss.butter(N, Wn, 'lowpass', analog = True)

        elif (btype == "cheby1"):
            N, Wn = ss.cheb1ord(Wp, Wa, Ap, Aa, True)
            b1, a1 = ss.cheby1(N, Ap, Wn, 'lowpass', analog = True)

        elif (btype == "cheby2"):
            N, Wn = ss.cheb2ord(Wp, Wa, Ap, Aa, True)
            b1, a1 = ss.cheby2(N, Aa, Wn, 'lowpass', analog = True)

        elif (btype == "ellip"):
            N, Wn = ss.ellipord(Wp, Wa, Ap, Aa, True)
            b1, a1 = ss.ellip(N, Ap, Aa, Wn, 'lowpass', analog=True)

        return b1, a1, N


    '''
        Aplicar el rango de desnormalización. (rango entre 0 y 1)
    '''
    def aplicarRangoDesnormalización(self, rango):

        Wx = self.findWx()
        escale = (self.Wa / Wx)**(rango)

        a1 = self.currentTFLP.den
        b1 = self.currentTFLP.num

        b2, a2 = ss.lp2lp(b1, a1, escale)

        self.currentLPRango = ss.TransferFunction(b2, a2)

        self.currentTransferFunction = self.findFilterFromLP(b2,a2)

        return self.currentTransferFunction

    '''
        Halla en qué frecuencia (Wx) atenúa exactamente Wa 
    '''
    def findWx(self):
        Wx = np.sqrt(self.Wa - self.Wp)
        min = self.Wp
        max = self.Wa
        w, mag, phase = ss.bode(self.currentTFLP, Wx)

        while (abs(-self.Aa - mag) > Epsilon):

            if mag > -self.Aa:
                min = Wx
                Wx = np.sqrt(Wx * max)

            else:
                max = Wx
                Wx = np.sqrt(Wx * min)

            w, mag, phase = ss.bode(self.currentTFLP, Wx)

        return Wx

    def findFilterFromLP(self, b1, a1):
        if self.filterType == "LP":
            b, a = ss.lp2lp(b1, a1, self.Fp * 2 * np.pi)

        elif self.filterType == "HP":
            b, a = ss.lp2hp(b1, a1, self.Fp * 2 * np.pi)

        elif self.filterType == "BP":
            b, a = ss.lp2bp(b1, a1, self.Fo * 2 * np.pi, self.dFp * 2 * np.pi)

        elif self.filterType == "BS":
            b, a = ss.lp2bs(b1, a1, self.Fo * 2 * np.pi, self.dFp * 2 * np.pi)

        return ss.TransferFunction(b, a)

    def getBode(self, w, WDado):
        if WDado == None:
            return ss.bode(self.currentTransferFunction, n = 1000)
        else:
            return ss.bode(self.currentTransferFunction, w, n=1000)

    def getBodeNormalized(self, w, WDado):
        if WDado == None:
            return ss.bode(self.currentTFLP, n=1000)
        else:
            return ss.bode(self.currentTFLP, w, n=1000)

    def getName(self):
        return self.nombre

    def getPolesZeros(self):
        return self.currentTransferFunction.poles, self.currentTransferFunction.zeros
















