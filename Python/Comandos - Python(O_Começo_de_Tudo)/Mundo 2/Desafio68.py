#Imports
import random
from time import sleep

#Contadores
contador = 0

print('\033[32m{:=^40}\033[m'.format(' \033[33mDesafio 68\033[32m '))
print('')
print('Vamos Jogar \033[34mPAR\033[m ou \033[36mÌMPAR\033[m')
print('\033[32m><\033[m'*20)
while True:
    pc = random.randint(1,10)
    valor = int(input('Diga um valor: '))
    sleep(1)
    escolha = str(input('\033[34mPAR\033[m ou \033[36mIMPAR?\033[m: ')).strip().upper()[0] #tipo par
    sleep(1)
    print('\033[32m><\033[m'*20)
    if escolha == 'P':
        vip = 0
    elif escolha == 'I':
        vip = 1

    total = pc + valor

    jogadorip = valor % 2
    pcip = pc % 2
    totalip = total % 2
    ip = ['\033[34mPAR\033[m','\033[36mIMPAR\033[m']

    tot = ip[totalip]


    print(f'Você Jogou \033[37m{valor}\033[m e Computador \033[37m{pc}\033[m. Total de \033[35m{total}\033[m Deu {tot}')
    sleep(1)
    print('\033[32m><\033[m'*20)
    if vip == totalip:
        contador = contador + 1
        print('Você \033[32mVenceu!\033[m👑')
        print('🤖Vamos Jogar Novamente...')
    else:
        print('Você Perdeu! 😱')
        break
sleep(1)
print('\033[32m><\033[m'*20)
print(f'\033[31mGAME OVER!\033[m☠️ Você Venceu \033[35m{contador}\033[m Vezes.')