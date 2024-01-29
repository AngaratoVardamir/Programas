#   Ano do Programa 2018
print('A posentadoria 2018')
#   Imports
from datetime import date
#   Ano mes Dia do pc
Ano_Real = date.today().year
Mes_Real = date.today().month
Dia_Real = date.today().day
#   Contadores
soma = 0
#   Dicionarios
dic = {}
#   Entrada
dic['nome'] = str(input('\033[34mNome:\033[m ')).strip().capitalize()
dic['Idade'] = Ano_Real-(int(input('\033[34mAno de \033[36mNascimento:\033[m ')))  # Idade da pessoa
dic['Carteira de Trabalho'] = int(input('\033[34mDigite o Numeiro da \033[36mCarteira de Trabalho (ou 0 se não tiver):\033[m '))
dic['Contratação'] = int(input('\033[34mAno de \033[mContratação: '))
dic['Salário'] = float(input('\033[34mSalário:\033[33m R$\033[m'))
dic['Aposentadoria'] = ((dic["Contratação"] + 35) - Ano_Real) + dic["Idade"]
#   Calculos
Anos_trabalho = (Ano_Real-dic['Contratação'])# Anos de Trabalho
#   Divisor
print('\033[31m><\033[m'*20)
#   Loop
for k,v in dic.items():
    print(f'\033[34m{k} \033[35mtem o valor \033[36m{v}')