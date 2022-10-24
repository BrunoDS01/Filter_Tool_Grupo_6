from src.ui.mainwindow import Ui_MainWindow
from src.Filters2 import FilterClass
import scipy.signal as ss
import matplotlib.pyplot as plt
import numpy as np


tipo = "BS"
f0 = 16e3
dP = 10e3
dA = 600
Fp = [11e3, 21e3]
Fa = [15.7e3, 16.3e3]
Ap = 6
Aa = 55
f = FilterClass()
tF = f.getBSTransferFunctionBW(f0, dP, dA, Ap, Aa, "cheby2", 0)


if tipo == "LP":
    w = np.logspace(np.log10(Fp *2*np.pi / 10), np.log10(Fa *2*np.pi* 10), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fp/2, Fp, Fp, Fp/2], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fa, Fa*10, Fa*10, Fa], [-Aa, -Aa, -Aa -10, -Aa -10], '0.9', lw=0)

elif tipo == "HP":
    w = np.logspace(np.log10(Fa * 2 * np.pi / 10), np.log10(Fp * 2 * np.pi * 10), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fp, Fp*10, Fp*10, Fp], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fa/10, Fa, Fa, Fa/10], [-Aa, -Aa, -Aa*2, -Aa*2], '0.9', lw=0)

elif tipo == "BP":
    w = np.logspace(np.log10(Fa[0] * 2 * np.pi / 10), np.log10(Fa[1] * 2 * np.pi*2), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fp[0], Fp[1], Fp[1], Fp[0]], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fa[0]/10, Fa[0], Fa[0], Fa[0]/10], [-Aa, -Aa, -Aa*2, -Aa*2], '0.9', lw=0)
    plt.fill([Fa[1], Fa[1]*2, Fa[1]*2, Fa[1]], [-Aa, -Aa, -Aa * 2, -Aa * 2], '0.9', lw=0)

elif tipo == "BS":
    w = np.logspace(np.log10(Fa[0] * 2 * np.pi / 10), np.log10(Fa[1] * 2 * np.pi * 10), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fa[0], Fa[1], Fa[1], Fa[0]], [-Aa, -Aa, -Aa-10, -Aa-10], '0.9', lw=0)
    plt.fill([Fp[0]/10, Fp[0], Fp[0], Fp[0]/10], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fp[1], Fp[1]*10, Fp[1]*10, Fp[1]], [0, 0, -Ap, -Ap], '0.9', lw=0)

tipo = "BS"  # ....fp-...........f0.............fp+.......
f0 = 16e3
dP = 10e3
dA = 600
Fp = [11e3, 21e3]
Fa = [15.7e3, 16.3e3]
Ap = 6
Aa = 50
f = FilterClass()
tF = f.getBSTransferFunctionBW(f0, dP, dA, Ap, Aa, "cheby2", 0)

w = np.logspace(np.log10(Fa[0] * 2 * np.pi / 10), np.log10(Fa[1] * 2 * np.pi * 10), 1000)
w, m, p = ss.bode(tF, w, n=1000)
plt.semilogx(w / (2 * np.pi), m)

plt.fill([Fa[0], Fa[1], Fa[1], Fa[0]], [-Aa, -Aa, -Aa-10, -Aa-10], '0.9', lw=0)
plt.fill([Fp[0]/10, Fp[0], Fp[0], Fp[0]/10], [0, 0, -Ap, -Ap], '0.9', lw=0)
plt.fill([Fp[1], Fp[1]*10, Fp[1]*10, Fp[1]], [0, 0, -Ap, -Ap], '0.9', lw=0)

plt.show()

N = f.n +1
tF = f.changeFilterOrder(N)

if tipo == "LP":
    w = np.logspace(np.log10(Fp * 2 * np.pi / 10), np.log10(Fa * 2 * np.pi * 10), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fp / 10, Fp, Fp, Fp / 10], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fa, Fa * 10, Fa * 10, Fa], [-Aa, -Aa, -Aa - 10, -Aa - 10], '0.9', lw=0)

elif tipo == "HP":
    w = np.logspace(np.log10(Fa * 2 * np.pi / 10), np.log10(Fp * 2 * np.pi * 10), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fp, Fp * 10, Fp * 10, Fp], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fa / 10, Fa, Fa, Fa / 10], [-Aa, -Aa, -Aa * 2, -Aa * 2], '0.9', lw=0)

elif tipo == "BP":
    w = np.logspace(np.log10(Fa[0] * 2 * np.pi / 10), np.log10(Fa[1] * 2 * np.pi * 2), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fp[0], Fp[1], Fp[1], Fp[0]], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fa[0] / 10, Fa[0], Fa[0], Fa[0] / 10], [-Aa, -Aa, -Aa * 2, -Aa * 2], '0.9', lw=0)
    plt.fill([Fa[1], Fa[1] * 2, Fa[1] * 2, Fa[1]], [-Aa, -Aa, -Aa * 2, -Aa * 2], '0.9', lw=0)

elif tipo == "BS":
    w = np.logspace(np.log10(Fa[0] * 2 * np.pi / 10), np.log10(Fa[1] * 2 * np.pi * 10), 1000)
    w, m, p = ss.bode(tF, w, n=1000)
    plt.semilogx(w / (2 * np.pi), m)

    plt.fill([Fa[0], Fa[1], Fa[1], Fa[0]], [-Aa, -Aa, -Aa - 10, -Aa - 10], '0.9', lw=0)
    plt.fill([Fp[0] / 10, Fp[0], Fp[0], Fp[0] / 10], [0, 0, -Ap, -Ap], '0.9', lw=0)
    plt.fill([Fp[1], Fp[1] * 10, Fp[1] * 10, Fp[1]], [0, 0, -Ap, -Ap], '0.9', lw=0)

plt.show()