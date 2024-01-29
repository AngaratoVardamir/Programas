print('{:~^40}'.format('\033[32m Desafio 04 ✔️ \033[m'))#30/07/2023

y7=input("Digite Algo no Teclado:")
print('Essa é A Class de {}:'.format(y7),type(y7))
print('Ele é um Número ?:',y7.isnumeric())
print('Ele é uma Letra ?: ',y7.isalpha())
print('Ele é uma Letra ou Um Número?: ',y7.isalnum())
print('Ele é uma Letra Maiúscula?: ',y7.isupper())
print('Ele é Só espaços?: ',y7.isspace())