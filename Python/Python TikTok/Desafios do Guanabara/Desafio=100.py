# imports
import random
# Lista
Numeros = []

#Funções
def Sorteia():
    for rep in range(1,6):
        Numeros.append(random.randint(0,9))


def Somapar():
    Somapar = 0
    for pos,num in enumerate (Numeros):
        if num % 2 == 0:
            Somapar = Somapar + num
    res = Somapar
    return res


Sorteia()
print(f'Sorteando 5 Valores da Lista: {Numeros} Pronto')
print(f'Somando os Valores Pares de {Numeros}, Temos {Somapar()}')#Somapar = Somapar + num