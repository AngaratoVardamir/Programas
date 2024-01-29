print('{:~^40}'.format('\033[32m Desafio 58 ✔️ \033[m'))#02/08/2023
#coltador
colt=0

#imports
import random  # noqa: E402
from time import sleep  # noqa: E402

#random
num=random.randint(0,10)

#comandos
print('olá Sou Sr. pc \033[32m:-)\033[m')
print('Estou Pensando em um Número entre 0 e 10...')
sleep(1)
qn=int(input('Qual Número Estou Pensando ?: '))
sleep(1)
print('Vamos Ver...')
print(' ')

#while
while qn != num:

#if e else
    colt += 1
    if num > qn :
        qn=int(input('''Voce errou !!!
Dica: é um pouco mais \033[31m<3\033[m
tente novamente: '''))
    else:
        qn=int(input('''Voce errou !!!
Dica: é um pouco menos \033[31m<3\033[m
tente novamente: '''))
print(' ')
#final
print('''voce acertou!!!
tetativas = \033[34m{}\033[m
o numero que o Sr.pc estava pensado = \033[35m{}\033[m
o numero que o jogador estava pensado = \033[36m{}\033[m'''.format(colt,num,qn))
print('Muito bem Vamos jogar denovo ? \033[31m;->\033[m')