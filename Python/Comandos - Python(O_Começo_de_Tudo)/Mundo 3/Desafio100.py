#Imports
from random import randint
#Contadores
soma = 0
#Lista
Numeros = []
NumPars = []
def Sorteia():
    num = randint(1,9)
    par_ou_impar = num % 2
    Numeros.append(num)
    if par_ou_impar == 0:
        NumPars.append(num)
    

Sorteia()
Sorteia()
Sorteia()
Sorteia()
Sorteia()
for i,x in enumerate (Numeros):
    Vl = x % 2
    if Vl == 0:
        soma = soma + x

print(f'Sorteando \033[32m{len(Numeros)}\033[m Valores de Lista:\033[33m',end=' ')
for i,x in enumerate (Numeros):
    print(f'{x}',end=' ')
print('\033[mPronto')
print(f'Somando os valores pares de \033[31m{NumPars}\033[m, Temos \033[31m{soma}\033[m.')