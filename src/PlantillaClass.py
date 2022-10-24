import numpy as np

class PlantillaClass:
    def __init__(self):
        self.nombre = None
        self.tipoPlantilla = None
        self.ap = None
        self.aa = None
        self.fp = None
        self.fa = None
        self.fo = None
        self.fpx = None
        self.fpy = None
        self.fax = None
        self.fay = None
        self.dfp = None
        self.dfa = None

    def crearPasaBajos(self, Fp, Fa, Ap, Aa):
        self.tipoPlantilla = "LP"
        self.fp = Fp
        self.fa = Fa
        self.ap = Ap
        self.aa = Aa

    def crearNombre(self, nombre):
        self.nombre = nombre

    def crearPasaAltos(self, Fp, Fa, Ap, Aa):
        self.tipoPlantilla = "HP"
        self.fp = Fp
        self.fa = Fa
        self.ap = Ap
        self.aa = Aa

    def crearPasaBandaFreq(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.tipoPlantilla = "BPF"
        self.fpx = Fpx
        self.fpy = Fpy
        self.fax = Fax
        self.fay = Fay
        self.ap = Ap
        self.aa = Aa

    def crearPasaBandaBW(self, Fo, dFp, dFa, Ap, Aa):
        self.tipoPlantilla = "BPBW"
        self.fo = Fo
        self.dfp = dFp
        self.dfa = dFa
        self.ap = Ap
        self.aa = Aa

        Fay = dFa / 2 + np.sqrt((dFa ** 2 + 4 * Fo ** 2)) / 2  # Hallo el valor de la frecuencia de atenuación más alta
        Fax = Fay - dFa

        Fpy = dFp / 2 + np.sqrt((dFp ** 2 + 4 * Fo ** 2)) / 2  # Hallo el valor de la frecuencia de atenuación más alta
        Fpx = Fpy - dFp

        self.fax = Fax
        self.fay = Fay
        self.fpx = Fpx
        self.fpy = Fpy

    def crearRechazaBandaFreq(self, Fpx, Fpy, Fax, Fay, Ap, Aa):
        self.tipoPlantilla = "BSF"
        self.fpx = Fpx
        self.fpy = Fpy
        self.fax = Fax
        self.fay = Fay
        self.ap = Ap
        self.aa = Aa

    def crearRechazaBandaBW(self, Fo, dFp, dFa, Ap, Aa):
        self.tipoPlantilla = "BSBW"

        Fay = dFa / 2 + np.sqrt((dFa ** 2 + 4 * Fo ** 2)) / 2  # Hallo el valor de la frecuencia de atenuación más alta
        Fax = Fay - dFa

        Fpy = dFp / 2 + np.sqrt((dFp ** 2 + 4 * Fo ** 2)) / 2  # Hallo el valor de la frecuencia de atenuación más alta
        Fpx = Fpy - dFp

        self.fo = Fo
        self.dfp = dFp
        self.dfa = dFa
        self.ap = Ap
        self.aa = Aa

        self.fax = Fax
        self.fay = Fay
        self.fpx = Fpx
        self.fpy = Fpy