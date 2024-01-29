#                        Jogador
Jogador = {} # Dicionario
partidas = []    #Listagem
soma = 0     #Somandor
Jogador["nome"] = str(input('Nome do \033[34mJogador:\033[m ')).strip().capitalize()
Partidas = int(input(f'Quantas Partidas \033[34m{Jogador["nome"]} Jogou?:\033[m '))
for p in range (0,Partidas):
    partidas.append(int(input(f'Quantos \033[34mGols \033[35mna partida \033[36m{p}\033[35m?:\033[m ')))
    Jogador["Gols"] = partidas
    soma = soma + partidas[p]
Jogador["Total"] = soma
print('\033[33m=--=\033[m'*20)
print(Jogador)
for k,v in Jogador.items():
    print(f'O Campo \033[31m{k} \033[34mtem o valor \033[32m{v}\033[m')
print('\033[33m=--=\033[m'*20)
for i,x in enumerate (partidas):
    print(f'=> Na \033[34mPartida {i},fez {x} Gols\033[m')
print(f'Foi um \033[34mTotal de \033[31m{soma} \033[34mGols\033[m')