import numpy as np
import constantes

def calcula_mxy_5p2(x,y):
    p0 = constantes.po
    poisson = constantes.poisson
    a = constantes.lado_a
    b = constantes.lado_b
    
    return ((p0 * (1 - poisson)) / ((np.pi**2) * (((1 / a**2) + (1 / b**2))**2) * a * b)) * np.cos((np.pi * x) / a) * np.cos((np.pi * y) / b)

    