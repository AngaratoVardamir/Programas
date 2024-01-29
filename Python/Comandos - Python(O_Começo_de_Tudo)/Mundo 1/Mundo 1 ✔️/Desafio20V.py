print('{:~^40}'.format('\033[32m Desafio 20 ✔️ \033[m'))#24/08/2023
import random
lista = [str(input("Qual é o nome do primeiro Aluno?: ")),
str(input("Qual é o nome do Segundo  Aluno?: ")),
str(input("Qual é o nome do Terceiro Aluno?: ")),
str(input("Qual é o nome do Quarto   Aluno?: "))]
print('><'*20)
random.shuffle(lista)
print("Ordem dos vencendores é:")
print(lista)