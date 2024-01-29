print('{:~^40}'.format('\033[32m Desafio 25 ✔️ \033[m'))#25/08/2023
nome = str(input('Qual é o Seu Nome Completo? ')).strip().lower()
print()
print('Seu nome tem Silva? = ',end='')
print('silva' in nome)