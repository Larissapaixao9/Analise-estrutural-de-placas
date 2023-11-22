import numpy as np
import constantes
from calcula_rigidez_flexao import calcula_rigidez_flexao

def calcula_deflexao_maxima():
    p0 = constantes.po
    a =  constantes.a
    b =  constantes.b
    valores_m = []
    valores_n = []
    valores_wmax = []
    
    #Obtem valor de rigidez a flexao
    D = calcula_rigidez_flexao()
    
    for m in range(1, 6):
        for n in range(1, 6):
            wmax = ((16*p0)/(((np.pi)**6)*D)) * ((-1)**(((m+n)/2)-1))/((m*n*((m/a)**2 + (n/b)**2))**2)
            # Verificar se wmax é real e não complexo
            if np.isreal(wmax):
                valores_m.append(m)
                valores_n.append(n)
                valores_wmax.append(wmax)
                
    
    return valores_wmax,valores_n,valores_m