import numpy as np
import constantes
def calcula_Rx_5p2(x,y):
    a = constantes.lado_a
    b = constantes.lado_b
    p0 = constantes.po
    poisson = constantes.poisson
    
    return ((-p0)/((np.pi*a)*((1/a**2)+(1/b**2))**2)) * ((1/a**2 + (2-poisson)/b**2)) * np.sin(np.pi*y/b)