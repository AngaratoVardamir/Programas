itens = ('Pedra','Papel','Tesoura')
from time import sleep
import random
print('{:=^40}'.format(' Jokenpõ '))
num = random.randint(0,2)
print(num)
jokenpo = int(input('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura

Escolha, Pedra Papel ou Tesoura ?:'''))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-'*20)
sleep(1)
print('Computador Jogou {}'.format(itens[num]))
sleep(1)
print('Jogador Jogou {}'.format(itens[jokenpo]))

print('-=-'*20)
if num == 0:
        if jokenpo == 0:
                print('JOGADOR EMPATOU')
        elif jokenpo == 1:
                print('JOGADOR VENCEU')
        elif jokenpo == 2:
                print('JOGADOR PERDEU')
elif num == 1:
        if jokenpo == 1:
                print('JOGADOR EMPATOU')
        elif jokenpo == 2:
                print('JOGADOR VENCEU')
        elif jokenpo == 0:
                print('JOGADOR PERDEU')
elif num == 2:
        if jokenpo == 2:
                print('JOGADOR EMPATOU')
        elif jokenpo == 0:
                print('JOGADOR VENCEU')
        elif jokenpo == 1:
                print('JOGADOR PERDEU')
else:
        print('Erro tente novamente')
