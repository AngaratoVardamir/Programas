#Tuplas/Listas/contadores/Dicionários
dados = {}
#Inputs
dados ['nome'] = nome = str(input('Nome: ')).strip().capitalize()
dados ['média'] = media = float(input(f'Média de {dados["nome"]}: '))
#Prints
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["média"]}')
#Reprov/Aprov
if dados["média"] >= 5.00:
    dados ['situação'] = 'Aprovado'
else:
    dados ['situação'] = 'Reprovado'
print(f'Situação é igual a {dados["situação"]}')