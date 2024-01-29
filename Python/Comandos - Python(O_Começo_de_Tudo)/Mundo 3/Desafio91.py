#        Imports
from random import randint
from operator import itemgetter
#        Dicionario
dados = {}
fim = ''
contador = 0
#Loop infinito
while True:
#        Entrada
    print('\033[32mValores Sorteados:\033[m')
    for jog in range (0,4):
        dados [f'Jogador {jog+1}'] = randint(1,6)
        print(f'O Jogador {jog+1} Tirou {dados[f"Jogador {jog+1}"]}')
    #        Ranking dos Jogadores:
    print('\033[33mRanking dos Jogadores:\033[m')
    ranking = sorted(dados.items(),key = itemgetter(1), reverse=True)
    for k,v in ranking:
        contador = contador+1
        print(f'{contador}º Lugar: {k} com {v}')
    print('\033[31m><\033[m'*20)
    fim = str(input('de Novo?, sim ou Não?: ')).upper().strip()[0]
    print('\033[31m><\033[m'*20)
    contador = contador -4
    if fim == 'N':
        break