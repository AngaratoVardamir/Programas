nome = ''
preço = 0
mais1000 = 0
total=0
maior=0
menor=0
quantidade = 0
carrinhon = [nome]  # carrinho de Nomes
carrinhop = [preço] # carrinho de Preços
linha = ('><'*10)
maiorno = menorno = ''

print('\033[33m{:=^90}\033[m'.format('\033[0;34;44m Lojas Angarato \033[m\033[33m'))
while True:
    quantidade = quantidade + 1
    print('\033[33m{}\033[m    Produto \033[36m{}\033[m   \033[33m{}\033[m'.format(linha,quantidade,linha))
    print(' ')
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preço = float(input('Preço do produto R$: '))
    print('\033[33m><\033[m'*40)
    #Mais que 1000
    if preço > 1000:
        mais1000 = mais1000 +1


    #Maior e menor
    if quantidade == 1:
        maior = menor = preço
        maiorno = menorno = nome
    else:
        if preço > maior:
            maior = preço
            maiorno = nome
        if preço < menor:
            menor = preço
            menorno = nome


    
    total = total + preço
    mais = str(input('Deseja adicionar outro produto ao carrinho?: ')).strip().upper()[0]
    if mais == 'N':
        Finalizando = str(input('Deseja concluir sua compra?: ')).strip().upper()[0]
        if Finalizando == 'S':
            Final = print('Compra concluída obrigado por comprar na loja Angarato')
            break

print('\033[33m><\033[m'*40)
# Final
print(f'''
Você comprou \033[32m{mais1000}\033[m produtos que custam mais de R$:1000 Reais
O nome do produtor mais barato que você comprou foi: \033[32m{menorno}\033[m com Preço de \033[32mR$:{menor}\033[m
O nome do produtor mais caro que você comprou foi:   \033[32m{maiorno}\033[m com Preço de \033[32mR$:{maior}\033[m''')   
print('\033[33m><\033[m'*40)
print(f'Gasto total em compras:                       \033[32m{total}\033[m')
