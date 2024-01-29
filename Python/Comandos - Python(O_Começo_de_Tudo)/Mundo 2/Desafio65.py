contador=0
somar=0
continua=''
media=0
maior=0
menor=0
num=0
#Titulo
print('''Desafio 65
''')
#num = int(input('Digite um Número: ')) 
#Reptidor
while continua != 'N': #Reptidor 
    num = int(input('Digite um Número: '))                       #Ex: 6
    continua = str(input('Quer Continuar [ S / N ]: ')).upper()  #EX:S 7x
    contador=contador+1    #Ex vai contar 1, 7 vezes
    somar=somar+num        #Ex somar=0+6
    if contador == 1:
        maior=menor=num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media=somar/contador
#comandos
print('''A Média entre Todos os {} Números é {:.2f}
O Maior Número foi {}
e Menor Número foi {}'''.format(contador,media,maior,menor))