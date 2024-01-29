pessoa = 1
nomes = []
pesos = []
continua = fim = ''
maximo = 0
minimo = 0
print(f'{f" Pessoa {pessoa} ":=^40}')
while True:
    if fim == 'fim':
        break
    pessoa = pessoa +1
    nome = str(input('Nome: '))
    nomes.append(nome)
    peso = float(input('Peso: '))
    pesos.append(peso)
    continua = str(input('Quer Continuar? [S/N]: ')).upper().strip()[0]
    if continua == 'N':
        break
    elif continua == 'S':
        print(f'{f" Pessoa {pessoa} ":=^40}')
    else:
        while True:
            continua = str(input('Tente Novamente, Quer Continuar? [S/N]: ')).upper().strip()[0]
            if continua == 'N':
                fim = 'fim'
                break
            elif continua == 'S':
                print(f'{f" Pessoa {pessoa} ":=^40}')
                break
print('><'*20)
print(f'Ao Todo, Você Cadastrou {pessoa-1} Pessoas.')
print(f'O Maior peso foi de {max(pesos)}Kg. peso de',end='')
for i, x in enumerate (pesos):# i == pessoa 0/...     and         x == pesos em float
    if x == max(pesos):
        print(f' e {nomes[i]}',end='')
print(f'\nO Menor peso foi de {min(pesos)}Kg. peso de',end='')
for i, x in enumerate (pesos):
    if x == min(pesos):
        print(f' e {nomes[i]}',end='')