#Lista
Converso = ['Binario','Octal','Hexadecimal']
Des_Lig = True
while Des_Lig:
    numero = int(input('Qual é o Número?: '))
    print('''Escolha uma Das Opções abaixo para Conversão:
    [0] Converter para Binario
    [1] Converter para Octal
    [2] Converter para Hexadecimal
    [3] Sair''')
    Des_Lig = True
    escolha = int(input('Qual é Sua Escolha?: '))
    if escolha == 3:
        break
    def escolhido():
        cms = [bin(numero),oct(numero),hex(numero)] # Comandos
        if escolha == escolha:
            print(f'{numero} Convertido para {Converso[escolha]} é igual a {cms[escolha]}')
            Des_Lig = False
        else:
            print('Opção inválida Tente Novamente')
    escolhido()
    