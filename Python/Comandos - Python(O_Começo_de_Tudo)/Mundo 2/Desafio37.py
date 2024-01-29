num=int(input('Qual é o Número ?'))
print("""Escolha uma Das Opções abaixo para Conversão:
[1] Converter para Binario
[2] Converter para Octal
[3] Converter para Hexadecimal""")
escolha=int(input('Sua Opção: '))
if escolha == 1:
    print('{} Convertido para Binário é igual a {}'.format(num, bin(num)))
elif escolha == 2:
    print('{} Convertido para Octal é igual a {}'.format(num, oct(num)))
elif escolha == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida Tente Novamente')
