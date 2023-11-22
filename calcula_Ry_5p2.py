import numpy as np
import constantes
from calcula_rigidez_flexao import calcula_rigidez_flexao

def calcula_Ry_5p2(x,y):
    p0 = constantes.po
    a = constantes.lado_a
    b = constantes.lado_b
    E = constantes.E_aco
    t = constantes.t
    v = constantes.poisson
    
    D = calcula_rigidez_flexao()
    
    return ((-p0)/((np.pi*b)*(((1/a**2)+(1/b**2))**2))) * ((1/b**2 + (2-v)/b**2)) * np.sin(np.pi*y/a)

