cont = 0
cont2 = 0
valores = []
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