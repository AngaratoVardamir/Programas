def Escreva():
    print('~'*len(texto))
    print(texto)
    print('~'*len(texto))

texto = ''
while texto != '999':
    texto = str(input('Escreva Alguma Coisa [999_Stop]: '))
    if texto == '999':
        break
    Escreva()