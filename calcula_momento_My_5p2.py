import numpy as np
import constantes

a = constantes.lado_a
b = constantes.lado_b
p0 = constantes.po
v = constantes.poisson

def calcula_momento_My_5p2(x, y):
    poisson = (1 / a ** 2) + (1 / b ** 2)
    return (p0 / ((np.pi ** 2) * poisson ** 2)) * ((poisson / a ** 2) + (1 / b ** 2)) * np.sin((np.pi * x) / a) * np.sin((np.pi * y) / b)
