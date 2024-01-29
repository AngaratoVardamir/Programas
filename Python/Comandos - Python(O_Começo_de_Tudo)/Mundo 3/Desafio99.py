Lista_de_Valores = []
# Digitação de Valores
for v in range (1,7):
    Valor = int(input(f'Digite o {v}° Valor: '))
    Lista_de_Valores.append(Valor)

# Analise dos Valores
print('~'*40)
print('Analisando os Valores Passados...')
for i,x in enumerate (Lista_de_Valores):
    print(f'{x}',end=' ')
print(' Foram informados 6 Valores Ao Todo.')
print(f'O Maior Valor informado foi {max(Lista_de_Valores)}.')
print('~'*40)