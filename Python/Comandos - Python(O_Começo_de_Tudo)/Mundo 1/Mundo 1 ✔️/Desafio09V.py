contador = 0
print('{:~^40}'.format('\033[32m Desafio 09 ✔️ \033[m'))#23/08/2023
num=int(input("\033[36mDigite um Número Pra Ver sua Tabuada: \033[m"))
print('\033[33m><\033[m'*20)
while contador != 10:
    contador = contador+1
    soma = (num * contador)
    print(f'\033[32m{num} x {contador:2} = {soma}\033[m')

print('\033[33m><\033[m'*20)