print('{:=^80}'.format(' \033[33mSequência de Fibonacci\033[m '))
print(' ')
termo=int(input('Digite Quantos Termos para eu calcular: '))
n1=0
n2=1
print('='*80)
print('\033[32mCalculando...\033[m')
print('{} \033[34m➡\033[m  {}'.format(n1, n2), end='')
cont=3
while cont <= termo:
    n3 = n1 + n2
    print(' \033[34m➡\033[m  {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' \033[34m➡\033[m  Fim')
print('='*80)

#while contador != termo:
