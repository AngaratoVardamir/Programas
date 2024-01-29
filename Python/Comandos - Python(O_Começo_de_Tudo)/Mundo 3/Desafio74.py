cont = 0
maior = 0
menor = 0
#Random
import random
while cont != 5:
    cont = cont +1
    num = random.randint(1,9)
    if cont == 1:
        a = num
    if cont == 2:
        b = num
    if cont == 3:
        c = num
    if cont == 4:
        d = num
    if cont == 5:
        e = num
    
    
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


abc = (f'{a} '+f'{b} '+f'{c} '+f'{d} '+f'{e}')
print(f'Listagem de Números \033[34m{abc}\033[m')
print('\033[33m><\033[m'*20)
print(f'Maior Valor \033[31m{maior}\033[m')
print(f'Menor Valor \033[32m{menor}\033[m')




