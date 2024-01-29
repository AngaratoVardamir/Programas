#Imports
from random import randint
from time import sleep

# Contadore / Listas
lista = []
dados = []
lista_de_listas = []
cont = 0

#linha 1
print('-'*50)

#Entrada
print('{: ^50}'.format('Jogo da Mega Sena'))

#linha 2
print('-'*50)

# Variavel de Controle
sort = int(input('Quantos Jogos Você quer que eu Sorteie?: '))

#Area do Loop
while True:
    Num_random = randint(1,60)
    lista.append(Num_random)
    if len(lista) == 6:
        dados.append(lista.copy())
        lista.clear()
    if len(dados) == sort:
        break
#Sorteando
print('{:-^50}'.format(f' Sorteando {sort} Jogos '))
#Em Execusão
for jogo in range(1,sort+1):
    print(f'Jogo {jogo}: {dados[cont]} ')
    sleep(0.5) # Parada de 0.5seg
    cont = cont+1
#final
print('{:-^50}'.format('< Boa Sorte! >'))