oper=int(input('''Escolha o Operador Arítmética

[ 1 ] +(ADIÇÃO)
[ 2 ] -(SUBTRAÇÃO)
[ 3 ] x(MULTIPLICAÇÃO)
[ 4 ] %(DIVISÃO)

Qual é a opção:'''))
nu=int(input('Digite o Número Final:'))
num=(nu+1)
div=int(input('Qual é o Divisor?:'))

for n in range(0,num):
    if oper == 1:
        igual=(n+div)
        print('{}+{}={}'.format(n,div,igual))
    elif oper == 2:
        igual=(n-div)
        print('{}-{}={}'.format(n,div,igual))
    elif oper == 3:
        igual=(n*div)
        print('{}x{}={}'.format(n,div,igual))
    elif oper == 4:
        igual=(n//div)
        print('{}%{}={}'.format(n,div,igual))
    else:
        print('erro de numero')
