import constantes
from sympy import symbols, sin, pi, integrate, N, diff
from calcula_rigidez_flexao import calcula_rigidez_flexao
from sympy.utilities.lambdify import lambdify
import numpy as np

def determina_w():
    m_max = constantes.m_max
    n_max = constantes.n_max
    m = constantes.m
    n = constantes.n
    q = constantes.q
    t = constantes.t
    E=constantes.E_aco
    b = constantes.b
    a = constantes.a
    poisson = constantes.poisson
    soma = 0
    wmax_antigo = 0
    
    D = calcula_rigidez_flexao()
    
    x, y = symbols('x y', real=True)

    #  w(x, y)
    for m in range(1, m_max + 1):
        for n in range(1, n_max + 1):
            if m % 2 != 0 and n % 2 != 0:
                Fint = q * sin(m * pi * x / a) * sin(n * pi * y / b)
                Fint2 = integrate(Fint, (x, 0, a))
                Q = (4 / (a * b)) * integrate(Fint2, (y, 0, b))
                Fint3 = Q / ((m**2 / a**2 + n**2 / b**2)**2) * sin(m * pi * x / a) * sin(n * pi * y / b)
                soma = soma + Fint3
                w = (1 / (pi**4 * D)) * soma
                wmaxx = w.subs(x, a / 2)
                wmax = N(wmaxx.subs(y, b / 2))
                print("---------------------------------------------------------------------------------------------------")
                print(f'Campo de deflexão para o par m = {m}, n = {n}: w(x,y) = {w}')
                print(f'Deformação máxima para o par m = {m}, n = {n}: wmax = {wmax:.8f}')
                err = (wmax - wmax_antigo) / wmax
                print(f'Erro para o o par m = {m}, n = {n}: e = {err * 100:.4f} %')
                wmax_antigo = wmax
    
    return w, x, y, D, poisson