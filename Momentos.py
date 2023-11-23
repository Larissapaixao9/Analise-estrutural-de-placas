from Const import *

# Variáveis são iniciadas no arquivo 'Const.py'
Mx = 0; My = 0; Mxy_pos = 0; Mxy_neg =0

# Equações para comparação de erro para cada número de iterações
termo1apenas = 0.0534*p0*a**2


# Para que tenhamos um valor mais exato de Mxy, vamos aumentar a precisão, aumentando o número de iterações do somatório.

x = a/2
y = b/2

# Para que tenhamos um valor mais exato de Mxy, vamos aumentar a precisão, aumentando o número de iterações do somatório.

Mx_lista = np.array([])
My_lista = np.array([])
Mxy_lista = np.array([])

# Calculando os momentos Mx, My, Mxy:
# while ((errx>lim_er) or (erry>lim_er) or (errxy>lim_er)):

for m in range (1,lim,2):
    for n in range (1,lim,2):

        print(f'\n\nIteração (Momentos): m = {m}, n = {n}')
        # Para que tenhamos um valor mais exato de Mxy, vamos aumentar a precisão, aumentando o número de iterações do somatório.
        # Cálculo de W_max
        sx += (((m/a) ** 2 + poi * (n / b) ** 2) / (m * n * ((m / a) ** 2 + (n / b) ** 2) ** 2)) * (np.sin(m * pi * x / a)) * (np.sin(n * pi * y / b))
        Mx = (16 * p0 / (pi ** 4)) * sx
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        sy += ((poi * (m / a) ** 2 + (n / b) ** 2) / (m * n * ((m / a) ** 2 + (n / b) ** 2) ** 2)) * (np.sin(m * pi * x / a)) * (np.sin(n * pi * y / b))
        My = (16 * p0 / (pi ** 4)) * sy
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        # Para Mxy, o maior valor absoluto se encontra nas 4 pontas. Admitindo x=0,y=b:
        sxy_pos += ((1) / (((m / a) ** 2 + (n / b) ** 2) ** 2)) * (np.cos(m * pi * 0 / a)) * (np.cos(n * pi * b / b))
        Mxy_pos = -16 * p0 * (1 - poi) / (pi ** 4 * a * b) * sxy_pos
        # print(f'Mxypos = {Mxy_pos}')
        # Para Mxy, o menor valor se encontra em duas das 4 pontas. Admitindo x=0,y=0:
        sxy_neg += ((1) / (((m / a) ** 2 + (n / b) ** 2) ** 2)) * (np.cos(m * pi * 0 / a)) * (np.cos(n * pi * 0 / b))
        Mxy_neg = -16 * p0 * (1 - poi) / (pi ** 4 * a * b) * sxy_neg
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

        My_lista = np.append(My_lista, My)
        Mx_lista = np.append(Mx_lista, Mx)
        Mxy_lista = np.append(Mxy_lista, Mxy_pos)

        # print(f'Mx_max = {round(Mx,n_dec)}')
        # print(f'My_max = {round(My,n_dec)}')
        # print(f'Mxy_max = {round(Mxy_pos,n_dec)}\n')

        # Contagem de iterações
        k+=1

        if(k>=2):
            erro_x = (Mx - cache_Mxmax) / cache_Mxmax * 100    # Erro relativo entre as iterações Mx
            errx = abs(round(erro_x, n_dec))
            print(f'Erro X (relativo à anterior)= {errx}%')

            erro_y = (My - cache_Mymax) / cache_Mymax * 100    # Erro relativo entre as iterações My
            erry = abs(round(erro_y, n_dec))
            print(f'Erro Y (relativo à anterior)= {erry}%')

            erro_xy = (Mxy_pos - cache_Mxymax) / cache_Mxymax * 100  # Erro relativo entre as iterações My
            errxy = abs(round(erro_xy, n_dec))
            print(f'Erro XY (relativo à anterior)= {errxy}%\n')


        cache_Mxmax = Mx
        cache_Mymax = My
        cache_Mxymax = Mxy_pos
        if ((errx<lim_er) and (erry<lim_er) and (errxy<lim_er)):
            m5 = m
            n5 = n
            break

    if ((errx < lim_er) and (erry < lim_er) and (errxy< lim_er)):
        m5 = m
        n5 = n
        break
    m5 =m
    n5 =n

z = t/2
Sigma_x = 12*Mx*z/t**3
Sigma_y = 12*My*z/t**3
Sigma_xy = 12*Mxy_pos*z/t**3
# print(f'Sigma X_max  = {round(Sigma_x/10**6,n_dec)} MPa\nSigma Y_max  = {round(Sigma_y/10**6,n_dec)} MPa\nSigma XY_max = {round(Sigma_xy/10**6,n_dec)} MPa')

## Mx My Mxy

# X = np.linspace(0,a,100)
# Y = np.linspace(0,b,100)
# X, Y = np.meshgrid(X, Y)
# print(X,'\n')

sxp  =0
syp  =0
sxyp =0

for m in range(1, m5+1, 2):
    for n in range(1, n5+1, 2):
        # print(f'\nIteração (plot): m = {m}, n = {n}')

        # Cálculo de W_max
        sxp += (((m / a) ** 2 + poi * (n / b) ** 2) / (m * n * ((m / a) ** 2 + (n / b) ** 2) ** 2)) * (
            np.sin(m * pi * X / a)) * (np.sin(n * pi * Y / b))
        Mxp = (16 * p0 / (pi ** 4)) * sxp
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        syp += ((poi * (m / a) ** 2 + (n / b) ** 2) / (m * n * ((m / a) ** 2 + (n / b) ** 2) ** 2)) * (
            np.sin(m * pi * X / a)) * (np.sin(n * pi * Y / b))
        Myp = (16 * p0 / (pi ** 4)) * syp
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        sxyp += ((1) / (((m / a) ** 2 + (n / b) ** 2) ** 2)) * (np.cos(m * pi * X / a)) * (np.cos(n * pi * Y / b))
        Mxyp = -16 * p0 * (1 - poi) / (pi ** 4 * a * b) * sxyp
        # --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# print(Mxp,Myp,Mxyp)
Sigma_x = 12*Mxp*z/t**3
Sigma_y = 12*Myp*z/t**3
Sigma_xy = 12*Mxyp*z/t**3
# print(f'Sigma X  = {Sigma_x/10**6} MPa\nSigma Y  = {Sigma_y/10**6} MPa\nSigma X = {Sigma_xy/10**6} MPa')
