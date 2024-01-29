cont9 = 0
nomesdosvalores = ('zero','Primera','Segunda','Tercera','Quarta')      #Atualisação
valor = (int(input('Qual é o \033[34mPrimero Valor:\033[m ')),
int(input('Qual é o \033[34mSegundo Valor:\033[m ')),
int(input('Qual é o \033[34mTercero Valor:\033[m ')),
int(input('Qual é o \033[34mQuarto Valor :\033[m ')))

print('\033[33m><\033[m'*20)

print(f'Listagem de Números: \033[35m{valor}\033[m')
print(f'O Valor \033[36m9 Apareceu: {valor.count(9)} Vezes\033[m')
if 3 in valor:
    print(f'O Valor \033[32m3 foi digitado na {nomesdosvalores[valor.index(3)+1]} Posição\033[m')
else:
    print('O Valor \033[31m3 Não foi Digitado\033[m')
print('Esses São os Números Pares Digitados: ',end='')
for v in valor:
    if v % 2 == 0:
        print(f'\033[34m{v} \033[m',end='')
print('\n')
print('\033[33m><\033[m'*20)