import numpy as np

# Material: Alumínio 6061-T6

pi = np.pi

a = 1                                           # Comprimento 'a'
b = 1                                           # Comprimento 'b'
t = 5/1000
p0 = 10**4

# t = float(input('Espessura da placa [mm]:'))*10**(-3)                                  # Espessura da placa
# p0 = float(input('Carga p0[N]:'))                                          # Carga p0 que distribuímos pela placa
# a = float(input('Comprimento "a" [m]:'))                                           # Comprimento 'a'
# b = float(input('Comprimento "b" [m]:'))                                          # Comprimento 'b'

z = t/2                                         # Centro da espessura
E = 68.9*10**9                                  # Módulo de elasticidade do Alumínio 6061-T6
poi = 0.33                                      # Coeficiente de poisson

D = E*t**3/(12*(1-poi**2))                      # Fator 'D' é calculado

#Iniciando variáveis gerais
s = 0                       # 's' é parte do cálculo da deflexão
err_rel = 2                 # Erro relativo
C = 20                      # Alterar C para aumentar/diminuir n. de iterações máximo
lim = 2*(2+C)               # Limite superior de 'n' e 'm' -
k=0                         # Contagem inicia em 0

#Iniciando variáveis para a Deflexão
w_max = 0                   # Inicia a variável de deflexão
cache_wmax = 1              # Cachê
er = 6.0                    # Erro relativo em razão 100/100
ss = 0                                                                          # Similar a 'sx', 'sy'
cache_wp = 10                                                                   # Cache

# Iniciando variáveis para os Momentos

sx = 0; sy = 0; sxy_pos =0; sxy_neg =0
cache_Mxmax = 10; cache_Mymax = 10; cache_Mxymax = 10
errx = 100; erry = 100; errxy = 100

# Iniciando variáveis 9.1
N = -20*(10**5)
Xd = a/2
Yd = b/2
sD = 0
WMAXD = 0
cache_wmaxD = 0

# Número de casas decimais para aproximações
n_dec = 5

# Limite mínimo de erro
lim_er = 5           # 5% de erro

# Malha
n_pontos = 150
x = np.linspace(0,a,n_pontos)
y = np.linspace(0,b,n_pontos)
X, Y = np.meshgrid(x,y)

n_pontosh = 300
xh = np.linspace(0,a,n_pontosh)
yh = np.linspace(0,b,n_pontosh)
Xh, Yh = np.meshgrid(xh,yh)
