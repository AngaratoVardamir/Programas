num=int(input('Digite um número ?: ')) #Número Inteiro
tot=0
for d in range(1,num +1):
    if num % d == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(d),end='')
print('\n\033[mO número {} foi Divisível \033[35m{}\033[m vezes'.format(num,tot))
if tot == 2:
    print('{} é um Número Primo'.format(num))
elif tot == 1:
    print('O número 1 tem apenas um divisor')
elif tot == 0:
    print('O zero tem infinitos Divisores')
else:
    print('{} é um Número Composto'.format(num))

