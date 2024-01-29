import random
num = random.randint(0,20)



tabela = ('Botafogo','Flamengo','Fluminense','Palmeiras','Bragantino','Grêmio','Athletico-PR','Cuiabá','São Paulo','Atlético-MG','Cruzeiro','Internacional','Fortaleza','Corinthians','Goiás','Bahia','Santos','Coritiba','Vasco','América-MG',)
print('\033[32mTabela do Campeonato Brasileiro\033[m')
print('Em Ordem Alfabetica')
alfa = (sorted(tabela))
print(f'''\033[34m
{alfa[0]}
{alfa[1]}
{alfa[2]}
{alfa[3]}
{alfa[4]}
{alfa[5]}
{alfa[6]}
{alfa[7]}
{alfa[8]}
{alfa[9]}
{alfa[10]}
{alfa[11]}
{alfa[12]}
{alfa[13]}
{alfa[14]}
{alfa[15]}
{alfa[16]}
{alfa[17]}
{alfa[18]}
{alfa[19]}
\033[m''')

print('\033[31m><\033[m'*20)

print(f'''Os \033[33m5\033[m \033[35mPrimeiros\033[m Colocados
1º {tabela[0]}
2º {tabela[1]}
3º {tabela[2]}
4º {tabela[3]}
5) {tabela[4]}
''')
print('\033[31m><\033[m'*20)
print(f'''   Os \033[35mÚltimos\033[m \033[33m4\033[m Colocados
20º {tabela[19]}
19º {tabela[18]}
18º {tabela[17]}
17º {tabela[16]}
''')
print('\033[31m><\033[m'*20)
print(f'Posição Aleatorio: {tabela[num]} {num+1}° Posição')