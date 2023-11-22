import numpy as np
import constantes

def calcula_Rc_5p2():
    p0 = constantes.po
    poisson = constantes.poisson
    a = np.linspace(1, 5, 100)
    b = np.linspace(1, 10, 100)
    
    a, b = np.meshgrid(a, b)
    return (2 * p0 * (1 - poisson)) / (np.pi ** 2 * a * b * ((1 / a ** 2) + (1 / b ** 2)) ** 2)

    