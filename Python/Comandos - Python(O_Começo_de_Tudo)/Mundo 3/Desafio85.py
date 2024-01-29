pessoa = 1
valo = []
while pessoa != 8:
    valo.append(int(input(f'Digite o {pessoa}°. Valor: ')))
    pessoa = pessoa +1
print('\033[31m><\033[m'*30)
print('Os Valores Pares Digitados Foram: ',end='')
for i, x in enumerate (sorted(valo)):
    if x % 2 == 0:
        print(f' {x}',end='')
print('\nOs Valores Ímpares Digitados Foram: ',end='')
for i, x in enumerate (sorted(valo)):
    if x % 2 == 1:
        print(f' {x}',end='')