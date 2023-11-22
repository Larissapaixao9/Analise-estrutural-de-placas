import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import constantes

def calcula_pmn_5p9():
    m = np.linspace(1, 200, 100)
    n = np.linspace(1, 200, 100)
    M, N = np.meshgrid(m, n)
    a = constantes.lado_a
    b = constantes.lado_b
    c = constantes.c
    d = constantes.c
    p = constantes.po
    x1 = a / 2
    y1 = b / 2
    return ((4 * p) / (np.pi ** 2 * M * N * c * d)) * np.sin((M * np.pi * x1) / a) * np.sin((M * np.pi * y1) / b) * np.sin((M * np.pi * c) / a) * np.sin((N * np.pi * d) / b),M,N
