print('{:~^40}'.format('\033[32m Desafio 74 ✔️ \033[m'))#18/08/2023
cont = 0
maior = 0
menor = 0
#Random
import random
num = (random.randint(1,10),random.randint(1,10),
random.randint(1,10),random.randint(1,10),random.randint(1,10))

print(f'Os Valores sorteados foram')
for n in num:
    print(f'\033[34m{ n } \033[m',end='')
    cont = cont +1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('')
print('\033[33m><\033[m'*20)
print(f'Maior Valor \033[31m{maior}\033[m')
print(f'Menor Valor \033[32m{menor}\033[m')