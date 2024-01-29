contm = -1
contn = -1
print('\033[35m><\033[m'*30)
num = [int(input('Digite um valor na \033[34mPosição 0:\033[m ')),
int(input('Digite um valor na \033[34mPosição 1:\033[m ')),
int(input('Digite um valor na \033[34mPosição 2:\033[m ')),
int(input('Digite um valor na \033[34mPosição 3:\033[m ')),
int(input('Digite um valor na \033[34mPosição 4:\033[m '))]
print('\033[35m><\033[m'*30)
print(f'O Maior Valor Digitado foi \033[33m{max(num):2}\033[m nas Posiçoes: ',end='')
for m in (num):
    contm = contm +1
    if m == (max(num)):
        maximo = f'\033[36m...{contm}\033[m'
        print(maximo,end='')
print(f'\nO Menor Valor Digitado foi \033[33m{min(num):2}\033[m nas Posiçoes: ',end='')
for n in (num):
    contn = contn +1
    if n == (min(num)):
        minimo = f'\033[36m...{contn}\033[m'
        print(minimo,end='')
print('\n\033[35m><',end='')
print('\033[35m><\033[m'*29)