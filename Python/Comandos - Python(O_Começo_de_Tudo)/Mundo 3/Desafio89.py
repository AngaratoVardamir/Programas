#Imports
from time import sleep
#Contadores/Listas
contador = 0
code_aluno = 0
nomes = []
lista_de_medias = []
primeiras_notas = []
segundas_notas = []
# Área de Loop
while True:
    contador = contador +1
    print('{:=^40}'.format(f' Aluno {contador} '))
    nome = str(input('Nome: ')).strip().capitalize()
    nomes.append(nome) # listador 1
    primeira_nota = float(input('Nota 1: '))
    primeiras_notas.append(primeira_nota)#Listagem primeiras notas
    segunda_nota = float(input('Nota 2: '))
    segundas_notas.append(segunda_nota)#Listagem segundas notas
    media = (primeira_nota + segunda_nota)/2 #Media
    lista_de_medias.append(media)
    continuar = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
#Linha 1
print('-'*40)
#no.nome/media
print(f'{"No.":<4}{"nome":<10}{"Média":>26}')
#Linha 2
print('-'*40)
#Nomes and Médias
for n in range (0,contador):
    print(f'{n:<4}{nomes[n]:<10}{lista_de_medias[n]:>26}')
#Linha 3
print('-'*40)
# Area de Loop 2
while True:
    code_aluno = int(input(f'Mostrar Notas de qual Aluno? [[ 0/{contador-1} ]/ou 999 para Finalizar]: '))
    if code_aluno == 999:
        break
    if code_aluno <= contador-1:
        print(f'Notas de {nomes[code_aluno]} São [{primeiras_notas[code_aluno]} {segundas_notas[code_aluno]}]')
    else:
        code_aluno = int(input(f'Tente Novamente. Mostrar Notas de qual Aluno? [[0/{contador-1}]/ou 999 para Finalizar]: '))
# Final
print('Finalizando...')
sleep(0.5)#Stop 0.5seg
print('{:=^40}'.format('< Volte Sempre >'))   