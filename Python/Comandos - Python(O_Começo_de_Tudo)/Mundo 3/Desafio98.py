def Contagem():
    print('~'*34)
    print(f'\033[34m  Contagem de {inicio} até {fim} de {passo} em {passo} \033[36m')
    for numero in range(inicio,fim,passo):
        print(numero,end=' ')
    print('\033[31mFim!\033[m')


inicio = 1
fim = 10+1
passo = 1

Contagem()

inicio = 10
fim = 0-1
passo = -2

Contagem()

print('~'*46)
print('\033[\033[33magora é sua vez de Personalizar a Contagem: \033[m')
inicio = int(input('\033[31minício: \033[m'))
fim = int(input('\033[31mfim: \033[m'))
passo = int(input('\033[31mPasso: \033[m'))
if inicio < fim:
    inicio = inicio
    fim = fim
    passo = +passo
else:
    inicio = inicio
    fim = fim-2
    passo = -passo

Contagem()