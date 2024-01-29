import random
import time

num=random.randint(0,5)

print('Estou Pensando em um Número entre 0 e 5...')
qn=int(input('Qual Número Estou Pensando ?:'))
print('Vamos Ver...')
if qn <=num:
    print('Isso Mesmo o Número é {}, voce tá com Sorte'.format(qn))
else:
    print('Que Falta de Sorte, O Número Não é {}, É {} tente de Novo'.format(qn,num))