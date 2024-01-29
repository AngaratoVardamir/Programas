import random


nomei=str(input("Qual é o nome do Aluno 1?"))
nomes=str(input("Qual é o nome do Aluno 2?"))
nomee=str(input("Qual é o nome do Aluno 3?"))
nomey=str(input("Qual é o nome do Aluno 4?"))

lista=[nomei,nomes,nomee,nomey]
aluno=random.choice(lista)


print("Quem Venceu foi :{} Eba!!! ".format(aluno))





