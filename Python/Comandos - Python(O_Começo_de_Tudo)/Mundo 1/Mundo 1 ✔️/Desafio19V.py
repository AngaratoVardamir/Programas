print('{:~^40}'.format('\033[32m Desafio 19 ✔️ \033[m'))#24/08/2023

from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo  Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto   Aluno: '))
lista = [n1,n2,n3,n4]
escolha = choice(lista)
print(f'O Aluno Escolhido foi {escolha}')