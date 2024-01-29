valor1=int(input('Valor A: '))
valor2=int(input('Valor B: '))
valor3=int(input('Valor C: '))

menor=valor1

if valor2<valor1 and valor2<valor3:
    menor = valor2
if valor3<valor1 and valor3<valor2:
    menor = valor3

maior=valor1

if valor2>valor1 and valor2>valor3:
    maior = valor2
if valor3>valor1 and valor3>valor2:
    maior = valor3
    
print('O Maior Valor é: {}'.format(maior))
print('O Menor Valor é: {}'.format(menor))
