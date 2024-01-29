print('{:~^40}'.format('\033[33mDesafio 64\033[m'))
print('')
num=0
soma=0
cont=0
while num != 999:
    num=int(input('Digite um Número ou [\033[31m999\033[m] para programar: '))
    soma=soma+num
    cont=cont+1
    if num == 999:
        cont=cont-1
        soma=soma-999
print('Voce digitou \033[34m{}\033[m vezes, a soma total é \033[36m{}\033[m obrigado'.format(cont,soma))