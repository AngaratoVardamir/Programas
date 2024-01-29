nu=int(input("Digite um Número:"))
num=(nu+1)
div=int(input('Qual é o Divisor?:'))

for n in range(0,num):
    igual=(n*div)
    print('{}x{}={}'.format(n,div,igual))
