# Listagem
Lista_Cop_Dados = []
Lista_dos_Dados = {}
Nome_da_Loja = []
Nome_do_Produtor = []
Preço_do_Produtor = []
# Contadores
Produtor = 0
Total = 0
Loja = 0
# Pricipal
print('\033[36m{:=^70}\033[m'.format('\033[34m Loja Gustavo \033[36m'))
while True:  # Loop do Programa
    Loja += 1
    Nome_da_Loja.append(str(input(f'\033[34mNome da Loja {Loja}: \033[m')).strip().capitalize())
    print('\033[33m-=-\033[m'*20)
    while True: # Loop da Loja / Produtos e Preços
        Nome_do_Produtor.append(str(input('\033[34mNome do Produtor: \033[m')).strip().capitalize()) 
        Preço_do_Produtor.append(float(input(f'\033[34mPreço do {Nome_do_Produtor[Produtor]} R$\033[m')))
        Total = Total + Preço_do_Produtor[Produtor]
        print('\033[33m-=-\033[m'*20)
        Produtor += 1
        Finalizar_Loop = str(input('\033[34mIsso é Tudo? [Sim/Não]: \033[m')).strip().capitalize()[0]
        print('\033[33m-=-\033[m'*20)
        if Finalizar_Loop == 'S':
            break
    Mais_Loja = str(input('\033[34mTem Mais uma Loja? [Sim/Não]:\033[m ')).strip().capitalize()[0]
    print('\033[33m-=-\033[m'*20)
    # Controle
    Lista_dos_Dados ["Loja"] = Nome_da_Loja
    Lista_dos_Dados ["Produtor"] = Nome_do_Produtor
    Lista_dos_Dados ["Preço"] = Preço_do_Produtor
    Lista_Cop_Dados.append(Lista_dos_Dados.copy())
    Lista_dos_Dados.clear()
    # Saida do Loop
    if Mais_Loja == 'N':
        break
#Testing
print(Lista_Cop_Dados)

# Ficha
for ilo,xlo in enumerate (Lista_Cop_Dados[0]["Loja"]):
    print(f'\033[34m{xlo}')
for ipr,xpr in enumerate (Lista_Cop_Dados[0]["Produtor"]):
    print(f'\033[36m{xpr}\033[m = ',end='')
    print(f'\033[32mR${Lista_Cop_Dados[0]["Preço"][ipr]}\033[m')
print(f'\033[37mValor Total: \033[32mR${Total}\033[m')