print('{:~^40}'.format('\033[32m Desafio 60 ✔️ \033[m'))#02/08/2023
c = 0
print('Olá sou Sr.Pc :-)')
num=int(input('Digite um Numero para eu Revelar seu Fatorial: '))
som = 1
while c < num:
    c = c + 1
    c2 = (num+1) - c
    som = c * som
    print('\033[35m{}\033[m'.format(c2),end='')
    print(' = 'if c > num-1 else ' x ',end='')
print('{}'.format(som),end='')
print('''
O Fatorial de\033[33m {} \033[mé\033[m \033[32m{}\033[m'''.format(num,som))
print('Falou ¨_¨')