import numpy as np
import constantes

def w_max_5p3(p, a, b, m, n, D):
    numerator = (4 * p * a**2) / (np.pi**4 * D)
    denominator = ((m**2 + n**2)**2)
    return numerator / denominator