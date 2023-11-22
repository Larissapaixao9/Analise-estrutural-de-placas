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

###Variaveis importantes para plotagem de grafico (5p2)
a = constantes.lado_a
b = constantes.lado_b



########## Exercicio 5.1 ##############
valores_wmax, valores_n, valores_m = calcula_deflexao_maxima()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar o gráfico 3D com cor azul ('Blues') e estilo de superfície 'coolwarm'
ax.plot_trisurf(valores_m, valores_n, valores_wmax, cmap='PuBu', linewidth=0, antialiased=True)

# Definir rótulos dos eixos
ax.set_xlabel('m')
ax.set_ylabel('n')
ax.set_zlabel('wmax')

# Título e legenda personalizados
plt.title('Variação da deflexão máxima (wmax) com m e n')
mappable = ax.collections[0]
cbar = plt.colorbar(mappable)
cbar.set_label('wmax', rotation=270)

# Exibir o gráfico
plt.show()

w, x, y, D, poisson = determina_w()

mx, my, mxy, qx, qy = calcula_derivadas(w, x, y, D, poisson)

Mx, My,Mxy,Qx,Qy,W,X,Y = converte_expressoes(mx, my, mxy,qx,qy,w,x,y)

dados = [Mx, My, Mxy, Qx, Qy, W]

# Títulos, mapas de cores e estilos diferentes
titulos = ['Mx', 'My', 'Mxy', 'Qx', 'Qy', 'Deflecção (w)']
mapas_cores = [cm.viridis, cm.coolwarm, cm.spring, cm.summer, cm.autumn, cm.winter]
estilos = ['surface', 'wireframe', 'surface', 'wireframe', 'surface', 'wireframe']

# Plot de cada superfície em uma figura separada
for i in range(6):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    if estilos[i] == 'surface':
        surf = ax.plot_surface(X, Y, dados[i], cmap=mapas_cores[i])
    elif estilos[i] == 'wireframe':
        surf = ax.plot_wireframe(X, Y, dados[i], color='black')
    
    ax.set_title(titulos[i])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel(titulos[i])
    
    fig.colorbar(surf)
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

# Modificando o estilo para wireframe
surf = ax.plot_wireframe(x, y, z, color='black')
# surf = ax.plot_surface(x, y, z, cmap='viridis')

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
z2 =calcula_momento_My_5p2(x, y)
# Plotagem do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_wireframe(x, y, z2, color='black')
# surf = ax.plot_surface(x, y, z2, cmap='viridis')

# Configurações adicionais
ax.set_xlabel('Comprimento (x)')
ax.set_ylabel('Largura (y)')
ax.set_zlabel('Momento (M_y)')
fig.colorbar(surf, shrink=0.5, aspect=5)

# Exibição do gráfico
plt.show()

##PLota momento Mx
M_x_5p2 = calcula_momento_Mx_5p2(x,y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('M_x')
ax.set_title('Gráfico 3D da função M_x')

# Plotagem do gráfico de superfície
# surf = ax.plot_wireframe(x, y, z2, color='black')
# ax.plot_surface(x, y, M_x_5p2, cmap='viridis')
# ax.plot_surface(x, y, M_x_5p2, cmap='viridis')
surf = ax.plot_wireframe(x, y, M_x_5p2, color='black')
# Mostrar o gráfico
plt.show()

M_xy = calcula_mxy_5p2(x,y)

# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('M_xy')
ax.set_title('Gráfico da função M_xy')

# Plotagem do gráfico de superfície
ax.plot_surface(x, y, M_xy, cmap='viridis')

# Mostrar o gráfico
plt.show()

####Plota Qx
Qx_5p2 = calcula_qx_5p2(x,y)
# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Função Q_x')

# Gráfico superfície
ax.plot_surface(x, y, Qx_5p2, cmap='viridis')

plt.show()

Qy_5p2 = calcula_qy_5p2(x,y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Função Q_y')

# Plotagem do gráfico de superfície
ax.plot_surface(x, y, Qy_5p2, cmap='viridis')

# Mostrar o gráfico
plt.show()

##########Plotar RX
Rx_5p2 = calcula_Rx_5p2(x,y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Função R_x')

# Plotagem do gráfico de superfície
ax.plot_surface(x, y, Rx_5p2, cmap='viridis')
plt.show()


############# PLota Ry
Ry_5p2 = calcula_Ry_5p2(x,y)
# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('y')
ax.set_ylabel('x')
ax.set_title('Gráfico 3D da função R_y')

# Plotagem do gráfico de superfície
ax.plot_surface(x, y, Ry_5p2, cmap='viridis')

# Mostrar o gráfico
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

p = 1e2  # Carga 
D = 200e9 
# Intervalo de valores para a e b
a_values = np.linspace(0, 5, 100)
b_values = np.linspace(0, 10, 100)

# Criação da malha de valores
A, B = np.meshgrid(a_values, b_values)

# Cálculo de w_max para cada combinação de a e b
W_max = w_max_5p3(p, A, B, 5, 5, D)  # Aqui, assumimos m = n = 1

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

a,b,w  = determina_w_9p1(a,b)
ax.plot_surface(a, b, w, cmap='viridis')

# Configurar os rótulos dos eixos
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('w')

# Exibir o gráfico 3D
plt.show()
