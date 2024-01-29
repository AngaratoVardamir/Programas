cont = 0
cont2 = 0
valores = []
maior2 = []
somapar = 0
impar = []
while True:
    valores.append(int(input(f'Digite um valor para [{cont2},{cont}]: ')))
    cont = cont +1
    if cont >= 3:
        cont = cont -3
        cont2 = cont2 +1
        if cont2 >= 3:
            break
print(f'''
[  {valores[0]}  ][  {valores[1]}  ][  {valores[2]}  ]
[  {valores[3]}  ][  {valores[4]}  ][  {valores[5]}  ]
[  {valores[6]}  ][  {valores[7]}  ][  {valores[8]}  ]''')
for i, x in enumerate (sorted(valores)):
    if x % 2 == 0:
        somapar = somapar +x
    else:
        impar.append(x)
soma3 = valores[6]+valores[7]+valores[8]
maior2.append(valores[3])
maior2.append(valores[4])
maior2.append(valores[5])
print(f'A soma de Todos os \033[32mValores Pares Digitados: {somapar}\033[m')
print(f'A soma dos valores \033[33mda Terceira Coluna é {soma3}\033[m')
print(f'O Maior Valor \033[36mda Segunda Linha é {max(maior2)}\033[m')