import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

#Importa modulos

from calcula_deflexao_maxima import calcula_deflexao_maxima
from determina_w import determina_w
from calcula_derivadas import calcula_derivadas
from converter_expressoes import converte_expressoes
from calcula_deflexao_5p2 import calcula_deflexao_5p2
from calcula_momento_My_5p2 import calcula_momento_My_5p2
from calcula_momento_Mx_5p2 import calcula_momento_Mx_5p2
from calcula_mxy_5p2 import calcula_mxy_5p2
from calcula_qx_5p2 import calcula_qx_5p2
from calcula_qy_5p2 import calcula_qy_5p2
from calcula_Rx_5p2 import calcula_Rx_5p2
from calcula_Ry_5p2 import calcula_Ry_5p2
from calcula_Rc_5p2 import calcula_Rc_5p2
from calcula_pmn_5p9 import calcula_pmn_5p9
from determina_coeficiente_amn import determina_coeficiente_amn
from w_max_5p3 import w_max_5p3
from avalia_w_5p9 import avalia_w_5p9
from calcula_w_central import calcula_w_central
from determina_w_9p1 import determina_w_9p1
import constantes
from Const import *             # 'Const.py' já foi importado por todos os outros arquivos
from Deflexao   import *
from Momentos   import *
from Apoio      import *
from Reacoes    import *
from Deflexao2  import *

Deflexao    = 0;Momentos    = 0;Apoio       = 0;Reac        = 0;Soma        = 0;Deflexao2   = 0

Deflexao    = 1
Momentos    = 1
Apoio       = 1
Reac        = 1
Soma        = 1
Deflexao2   = 1

###Variaveis importantes para plotagem de grafico (5p2)
a = constantes.lado_a
b = constantes.lado_b



########## Exercicio 5.1 ##############
# Deflexão w(x,y)

if Deflexao == 1:
    figW = plt.figure()
    axw = figW.add_subplot(111, projection='3d')
    # axw.set_aspect('equal')

    axw.plot_surface(X, Y, Wplot, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    axw.set_title(f'W(x,y)');axw.set_xlabel('Largura X [m]');axw.set_ylabel('Altura Y [m]');axw.set_zlabel('W(x,y) [m]')
    # plt.show()

# Momentos Mx, My, Mxy

if Momentos ==1:
    figM = plt.figure()

    ax1 = figM.add_subplot(131, projection='3d')
    ax2 = figM.add_subplot(132, projection='3d')
    ax3 = figM.add_subplot(133, projection='3d')

    ax1.plot_surface(X, Y, Mxp, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    ax1.set_title(f'Mx');ax1.set_xlabel('Largura X [m]');ax1.set_ylabel('Altura Y [m]');ax1.set_zlabel('Mx(x,y) [Nm]')

    ax2.plot_surface(X, Y, Myp, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    ax2.set_title(f'My');ax2.set_xlabel('Largura X [m]');ax2.set_ylabel('Altura Y [m]');ax2.set_zlabel('My(x,y) [Nm]')

    ax3.plot_surface(X, Y, Mxyp, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    ax3.set_title(f'Mxy');ax3.set_xlabel('Largura X [m]');ax3.set_ylabel('Altura Y [m]');ax3.set_zlabel('Mxy(x,y) [Nm]')

    # plt.show()

# Apoios(x,y)

if Apoio == 1:
    figA = plt.figure()

    axa = figA.add_subplot(131, projection='3d')
    axb = figA.add_subplot(132, projection='3d')
    axc = figA.add_subplot(133, projection='3d')

    axa.plot_surface(X, Y, P, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    axa.set_title(f'P(x,y)');axa.set_xlabel('Largura X [m]');axa.set_ylabel('Altura Y [m]');axa.set_zlabel('P(x,y) [N]')

    axb.plot_surface(X, Y, qtx, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    axb.set_title(f'Qx(x,y)');axb.set_xlabel('Largura X [m]');axb.set_ylabel('Altura Y [m]');axb.set_zlabel('Qx(x,y) [N]')

    axc.plot_surface(X, Y, qty, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    axc.set_title(f'Qy(x,y)');axc.set_xlabel('Largura X [m]');axc.set_ylabel('Altura Y [m]');axc.set_zlabel('Qy(x,y) [N]')
    # plt.show()



# Reações Rx, Ry

if Reac ==1:
    figR = plt.figure()

    rb = figR.add_subplot(121, projection='3d')
    rc = figR.add_subplot(122, projection='3d')

    rb.plot_surface(X, Y, Rxx, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    rb.set_title(f'Rx(x,y)');rb.set_xlabel('Largura X [m]');rb.set_ylabel('Altura Y [m]');rb.set_zlabel('Rx(x,y) [N]')

    rc.plot_surface(X, Y, Ryy, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    rc.set_title(f'Ry(x,y)');rc.set_xlabel('Largura X [m]');rc.set_ylabel('Altura Y [m]');rc.set_zlabel('Ry(x,y) [N]')
    # plt.show()

# Somatório de forças
if Soma==1:
    # print(f'Rc = {RCC}\nMxy={Mxy_pos}\nMxy/Rc={Mxy_pos/RCC}')
    print(f'\nRc = {RCC} N\nMxy = {Mxy_pos} Nm')

    # SomatorioZ = +4*RCC+ 2*(2*Mxy_pos + 2*Mxy_neg)
    SomatorioZ = -4*RCC+ 4*(Mxy_pos)

    print(f'\nO somatório de forças em Z (Rc + 2*(Mxy(1,1)+Mxy(1,0)+Mxy(0,1)+Mxy(0,0)))resulta em: {SomatorioZ} [N].')
    print(f'O que confirma que surgem, de fato, reações pontuais R = 2*Mxy nos 4 cantos da placa.')
    print(f'O somatório de forças aproxima-se de 0 conforme maiores os valores de "m" e "n".')

if Deflexao2 == 1:
    figWD = plt.figure()
    axwD = figWD.add_subplot(111, projection='3d');
    # axwD.set_aspect('equal')

    axwD.plot_surface(Xh, Yh, WplotD, cmap='plasma', rstride=1, cstride=1, linewidth=0)
    axwD.set_title(f'W 9.1(x,y)');
    axwD.set_xlabel('Largura X [m]');
    axwD.set_ylabel('Altura Y [m]');
    axwD.set_zlabel('W 9.1(x,y) [m]')
    # plt.show()
plt.show()


######### Exercicio 5.2 ####################
#Queremos reações no suporte de uma placa retangular apoiada.
x = np.linspace(0, a, 100)
y = np.linspace(0, b, 100)
x, y = np.meshgrid(x, y)
z = calcula_deflexao_5p2(x, y)

# Plotagem do gráfico 3D com wireframe e título diferente
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Modificando o estilo para wireframe com colormap 'plasma'
surf = ax.plot_wireframe(x, y, z, cmap='plasma')

# Novo título para o gráfico
ax.set_title('Deflexão do Modelo')

# Configurações adicionais
ax.set_xlabel('Comprimento (x)')
ax.set_ylabel('Largura (y)')
ax.set_zlabel('Deflexão (w)')
fig.colorbar(surf, shrink=0.5, aspect=5)

# Exibição do gráfico
plt.show()

#####Plota momento My:
z2 = calcula_momento_My_5p2(x, y)
M_x_5p2 = calcula_momento_Mx_5p2(x, y)
M_xy = calcula_mxy_5p2(x, y)

fig = plt.figure(figsize=(18, 6))

# Plotagem do gráfico para M_y
ax1 = fig.add_subplot(131, projection='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('M_y')
ax1.set_title('Gráfico de M_y')
ax1.plot_surface(x, y, z2, cmap='viridis')

# Plotagem do gráfico para M_x
ax2 = fig.add_subplot(132, projection='3d')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('M_x')
ax2.set_title('Gráfico de M_x')
ax2.plot_surface(x, y, M_x_5p2, cmap='viridis')

# Plotagem do gráfico para M_xy
ax3 = fig.add_subplot(133, projection='3d')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('M_xy')
ax3.set_title('Gráfico da função M_xy')
ax3.plot_surface(x, y, M_xy, cmap='viridis')

plt.tight_layout()
plt.show()
#
Qx_5p2 = calcula_qx_5p2(x, y)
Qy_5p2 = calcula_qy_5p2(x, y)

fig = plt.figure(figsize=(12, 6))

# Gráfico para Qx
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Função Q_x')
surf1 = ax1.plot_surface(x, y, Qx_5p2, cmap='viridis')

# Gráfico para Qy
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Função Q_y')
surf2 = ax2.plot_surface(x, y, Qy_5p2, cmap='viridis')

# Mostrar o gráfico
plt.tight_layout()
plt.show()

# ##########Plotar RX
Rx_5p2 = calcula_Rx_5p2(x, y)
Ry_5p2 = calcula_Ry_5p2(x, y)

fig = plt.figure(figsize=(10, 5))

# Plotagem da função Rx
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Função R_x')
surf1 = ax1.plot_surface(x, y, Rx_5p2, cmap='viridis')

# Plotagem da função Ry
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Função R_y')
surf2 = ax2.plot_surface(x, y, Ry_5p2, cmap='viridis')

# Mostrar o gráfico combinado
plt.tight_layout()
plt.show()


#####Calcula Rc
Rc_5p2 = calcula_Rc_5p2()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(a, b, Rc_5p2, cmap='viridis')

# Configurações do gráfico
ax.set_xlabel('Comprimento (a)')
ax.set_ylabel('Largura (b)')
ax.set_title('R_c')

# Mostrar o gráfico
plt.show()

######### EXERCICIO 5.3 ############
Pmn,M,N = calcula_pmn_5p9()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(M, N, Pmn, cmap='viridis')

# Configurando os rótulos dos eixos
ax.set_xlabel('m')
ax.set_ylabel('n')

# gráfico
plt.show()

w,a,b = avalia_w_5p9()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar o gráfico 3D
ax.plot_surface(a, b, w, cmap='viridis')

# Configurar os rótulos dos eixos
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w')
plt.show()

#W central
w_central,a,b = calcula_w_central()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar o gráfico 3D
ax.plot_surface(a, b, w_central, cmap='viridis')

# Configurar os rótulos dos eixos
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w')

# Exibir o gráfico 3D
plt.show()

p = 5e2  # Carga 
D = 200e9 
# Intervalo de valores para a e b
a_values = np.linspace(0, 5, 100)
b_values = np.linspace(0, 10, 100)

# Criação da malha de valores
A, B = np.meshgrid(a_values, b_values)

# Cálculo de w_max para cada combinação de a e b
W_max = w_max_5p3(p, A, B, 1, 1, D)  # Aqui, assumimos m = n = 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, B, W_max, cmap='viridis')
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w_max')

# Exibição do gráfico
plt.show()


############ Exercicio 9.1 #################
amn,m,n = determina_coeficiente_amn()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(m, n, amn)
ax.set_xlabel('m')
ax.set_ylabel('n')
ax.set_zlabel('amn')
plt.show()

# determina_w_9p1()

