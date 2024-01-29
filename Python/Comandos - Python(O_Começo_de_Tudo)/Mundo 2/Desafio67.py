#contadores
contador = 0
valor = 0
print('\033[33m{:=^60}\033[m'.format(' Desafio \033[34m67\033[33m '))
print(' ')
valor=int(input('Quer ver a Tabuada de Qual Valor?: '))
print('\033[33m><\033[m'*20)
while True:
    contador = contador +1
    soma = contador * valor
    print(f'{valor} x {contador} = {soma}')

    if contador == 10:
        print('\033[33m><\033[m'*20)
        print('Para finalizar o programa digite [ \033[31m-1\033[m ]')
        print('\033[33m><\033[m'*20)
        valor=int(input('Quer ver a Tabuada de Qual Valor?: '))
        contador = contador - 10
    if valor < 0:
        break
print('\033[33m><\033[m'*20)
print('\033[31mPrograma Finalizando\033[m')