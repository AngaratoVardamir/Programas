men=0
mai=0
from datetime import date
temporeal = date.today().year


for n in range (1,8):
    ano=int(input('\033[33mEm que ano a \033[36m{}ª\033[33m Pessoa nasceu?\033[m '.format(n)))
    idade=(temporeal - ano)
    if idade < 18:
        men += 1
    else:
        mai += 1
print('''
\033[32m{}\033[34m Pessoas Já Atigiram a maioridade
\033[31m{}\033[34m Pessoas Não Atigiram a maioridade\033[m'''.format(mai,men))