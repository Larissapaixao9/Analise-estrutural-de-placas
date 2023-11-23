from Const import *

# Variáveis são iniciadas no arquivo 'Const.py'

# Equações para comparação de erro para cada número de iterações, para verificação
termo1apenas = 0.00416*p0*a**4/D                                # Equação para apenas o primeiro termo
sol_exata = 0.00406*p0*a**4/D                                   # Equação para os 4 primeiros termos


# Equação (b), W_max
for m in range (1,lim,2):
    for n in range (1,lim,2):

        print(f'\nIteração (Deflexão): m = {m}, n = {n}')

        # Cálculo de W_max
        s += ((-1)**((m+n)/2-1))/(m*n*((m/a)**2+(n/b)**2)**2)
        WMAX = 16 * p0 / (pi ** 6 * D) * s

        # Contagem de iterações
        k += 1

        if(k>=2):
            er = round(abs((WMAX - cache_wmax) / cache_wmax * 100), n_dec)
            print(f'Erro (relativo à anterior)= {er}%')

        cache_wmax = WMAX

        if(er<lim_er):
            m5 = m; n5 = n
            break
    if (er < lim_er):
        m5 = m; n5 = n
        break
    m5 =m
    n5 = n

for m in range (1,m5+1,2):
    for n in range (1,n5+1,2):
        # Cálculo de W_max
        ss += (np.sin(m*pi*X/a)*np.sin(n*pi*Y/b))/(m*n*((m/a)**2+(n/b)**2)**2)
        Wp = 16 * p0 / (pi ** 6 * D) * ss

        cache_wp = Wp

Wplot = Wp                                                                      # Última iteração de Wp
k = 0                                                                           # Contagem de iterações
