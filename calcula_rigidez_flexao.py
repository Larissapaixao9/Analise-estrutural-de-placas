import numpy as np
import constantes

def calcula_rigidez_flexao():
    E_aco = constantes.E_aco
    poisson = constantes.poisson
    t = constantes.t
    D = (E_aco*t**3)/(12*(1-poisson**2))
    
    return D



