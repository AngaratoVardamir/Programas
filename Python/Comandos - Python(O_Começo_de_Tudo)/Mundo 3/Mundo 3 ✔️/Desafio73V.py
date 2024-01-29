print('{:~^40}'.format('\033[32m Desafio 73 ✔️ \033[m'))#18/08/2023

import random
num = random.randint(0,20)

tabela = ('Botafogo','Flamengo','Fluminense','Palmeiras',
'Bragantino','Grêmio','Athletico-PR','Cuiabá','São Paulo',
'Atlético-MG','Cruzeiro','Internacional','Fortaleza','Corinthians',
'Goiás','Bahia','Santos','Coritiba','Vasco','América-MG',)

print('\033[32mTabela do Campeonato Brasileiro 2023\033[m')
print('Em Ordem Alfabetica')
alfa = (sorted(tabela))
for a in alfa:
    print(f'\033[34m{a}\033[m')

print('\033[31m><\033[m'*20)
print('Os \033[33m5\033[m \033[35mPrimeiros\033[m Colocados')   
print(f'\033[36m{tabela[:5]}\033[m')

print('\033[31m><\033[m'*20)

print('Os \033[35mÚltimos\033[m \033[33m4\033[m Colocados')
print(f'\033[36m{tabela[-4:]}\033[m')

print('\033[31m><\033[m'*20)

print(f'Posição Aleatorio: \033[34m{tabela[num]}\033[m \033[33m{num+1}° Posição\033[m')