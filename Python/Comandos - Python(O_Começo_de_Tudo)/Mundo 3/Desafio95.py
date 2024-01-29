#   Imports
from time import sleep
#   Contadores
Total = 0
Pessoa = 1
#   Dicionarios / Listas
Pasta = []   # Pasta para gurda Dados das Pessoas
Dados_Dos_Jogadores = {}
Gols_Dos_Jogadores = []  #LIstagem de Gols
#   Reptidor
print('{:=^60}'.format(f' Jogador {Pessoa} '))
while True:
    Pessoa = Pessoa +1
    #   Nome do Jogador:
    Dados_Dos_Jogadores["Nome"] = str(input('Nome do Jogador: ')).strip().capitalize()
    Partidas = int(input(f'Quantas Partidas {Dados_Dos_Jogadores["Nome"]} Jogou?: ')) # Partidas
    print('-='*20) # Linha 1
    sleep(0.5)
    for partida in range (0,Partidas):#   Loop 1
        Gols_Dos_Jogadores.append(int(input(f"Quantos Gols na partida {partida}? ")))
        Total = Total + Gols_Dos_Jogadores[partida]
    print('-='*20) # Linha 2
    sleep(0.5)
    # Gols e o Total
    Dados_Dos_Jogadores["Gols"] = Gols_Dos_Jogadores.copy()
    Dados_Dos_Jogadores["Total"] = Total
    #   Loop 2
    for k,v in Dados_Dos_Jogadores.items():
        print(f'O Campo {k} tem o valor {v}.')
    print('-='*20) # Linha 3
    sleep(0.5)
    print(f'O Jogador {Dados_Dos_Jogadores["Nome"]} Jogou {Partidas} Partidas.') 
    #   Loop 3
    sleep(0.5)
    for partida in range (0,Partidas):
        print(f'=> Na Partida {partida}, fez {Gols_Dos_Jogadores[partida]} Gols.')
    #   Final
    print(f'Foi um Total de {Dados_Dos_Jogadores["Total"]} Gols.')
    print('-='*20) # Linha 4
    sleep(0.5)
    # Linha de Controle:
    certeza = str(input('Você quer finalizar o Programa?: ')).strip().capitalize()[0]
    if certeza == 'N':
        Pasta.append(Dados_Dos_Jogadores.copy())
        print('-='*20) # linha 5 P1
        sleep(0.5)
        print('{:=^60}'.format(f' Jogador {Pessoa} '))
        # Limpador de Listas Contadores e Dicionarios
        Dados_Dos_Jogadores.clear()
        Gols_Dos_Jogadores.clear()
        Total = Total - Total
    elif certeza == 'S':
        Pasta.append(Dados_Dos_Jogadores.copy())
        break
# Desafio 095
print('-='*20)# linha 5 P2
print(f'{"Cod":<4}{"Nome":<20}{"Gols":<20}{"Total":>8}')
print('-'*52)
for k,v in enumerate (Pasta):
    Ne = str(v["Nome"])
    Gs = str(v["Gols"])
    Tl = str(v["Total"])
    print('{:<4}{:<20}{:<20}{:>8}'.format(k,Ne,Gs,Tl))
escolha_Jogador = 0 # Contador da Escolha
print('-'*52)
while True:
    escolha_Jogador = int(input(f'Mostra Dados de Qual Jogador? [0,{Pessoa-2}/ 999 para finalizar]: '))
    if escolha_Jogador == 999:
        break
    print('------ Levantamento do Jogador Padrão:')
    for cod in range (0,Partidas):
        print(f'    No Jogo {cod} fez {Pasta[escolha_Jogador]["Gols"][cod]} Gols.')
print('-'*52)