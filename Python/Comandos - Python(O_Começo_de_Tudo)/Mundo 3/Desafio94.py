#    Dicionario
Dados = {}
Todos = {}
Lista = []
nome_das_mulheres = {}
acima_da_media = {}
#    Contadores
soma_de_todas_as_idades = 0
Pessoa_numero = 0
sexend = 0

#    Loop parte 1
while True:
    Pessoa_numero = Pessoa_numero +1 #Contador de Jogadores
    # Nome /Verificado
    Dados[f"Pessoa {Pessoa_numero}"] = str(input('Nome: ')).strip().capitalize()
    certeza = str(input(f'Seu Nome é mesmo {Dados[f"Pessoa {Pessoa_numero}"]}?: ')).strip().capitalize()[0]        # Cofirmação do nome
    if certeza == 'S':
        Todos["nome"] = Dados[f"Pessoa {Pessoa_numero}"] # Todos os Dados
    if certeza == 'N':
        while True:
            Dados[f"Pessoa {Pessoa_numero}"] = str(input('Então qual é seu Nome?: ')).strip().capitalize()
            certeza = str(input(f'Seu Nome é mesmo {Dados[f"Pessoa {Pessoa_numero}"]}?: ')).strip().capitalize()[0]        # Cofirmação do nome
            if certeza == 'S':
                Todos["nome"] = Dados[f"Pessoa {Pessoa_numero}"] # Todos os Dados
                break
    # Sexo /Verificado
    while True:
        if sexend == 2:
            break
        Dados[f"Sexo {Pessoa_numero}"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if 'M' == Dados[f"Sexo {Pessoa_numero}"]:    #filtador de masculino
            certeza = str(input(f'Seu Sexo é {Dados[f"Sexo {Pessoa_numero}"]}?: ')).strip().upper()[0]
            if certeza == 'S':
                Todos["Sexo"] = Dados[f"Sexo {Pessoa_numero}"] # Todos os Dados
                break
        if 'F' == Dados[f"Sexo {Pessoa_numero}"]:    #filtador de feminino
            certeza = str(input(f'Seu Sexo é {Dados[f"Sexo {Pessoa_numero}"]}?: ')).strip().upper()[0]
            if certeza == 'S':
                Todos["Sexo"] = Dados[f"Sexo {Pessoa_numero}"] # Todos os Dados
                nome_das_mulheres[f"Pessoa {Pessoa_numero}"] = (Dados[f"Pessoa {Pessoa_numero}"]) # Mulheres seus nomes
                break
        if Dados[f"Sexo {Pessoa_numero}"] not in 'MF': # se não for masculino e feminino
            while True:
                Dados[f"Sexo {Pessoa_numero}"] = str(input('Erro imforme seu Sexo [M/F]: ')).strip().upper()[0]
                if 'M' == Dados[f"Sexo {Pessoa_numero}"]:#filtador de masculino
                    certeza = str(input(f'Seu Sexo é {Dados[f"Sexo {Pessoa_numero}"]}?: ')).strip().upper()[0]
                    if certeza == 'S':
                        Todos["Sexo"] = Dados[f"Sexo {Pessoa_numero}"] # Todos os Dados
                        sexend = 2
                        break
                if 'F' == Dados[f"Sexo {Pessoa_numero}"]:#filtador de feminino
                    certeza = str(input(f'Seu Sexo é {Dados[f"Sexo {Pessoa_numero}"]}?: ')).strip().upper()[0]
                    if certeza == 'S':
                        Todos["Sexo"] = Dados[f"Sexo {Pessoa_numero}"] # Todos os Dados
                        nome_das_mulheres[f"Pessoa {Pessoa_numero}"] = (Dados[f"Pessoa {Pessoa_numero}"]) # Mulheres seus nomes
                        sexend = 2
                        break
    # Idade /Verificado
    Dados[f"Idade {Pessoa_numero}"] = int(input('Idade: '))
    certeza = str(input(f'Sua Idade é {Dados[f"Idade {Pessoa_numero}"]}?: ')).strip().upper()[0]
    if certeza == 'S':
        Todos["Idade"] = Dados[f"Idade {Pessoa_numero}"] # Todos os Dados
        acima_da_media[f"Pessoa {Pessoa_numero}"] = Dados[f"Idade {Pessoa_numero}"] # Acima_da media
    if certeza == 'N':
        while True:
            Dados[f"Idade {Pessoa_numero}"] = int(input('Então qual é sua Idade: '))
            certeza = str(input(f'Sua Idade é {Dados[f"Idade {Pessoa_numero}"]}?: ')).strip().upper()[0]
            if certeza == 'S':
                Todos["Idade"] = Dados[f"Idade {Pessoa_numero}"] # Todos os Dados
                acima_da_media[f"Pessoa {Pessoa_numero}"] = Dados[f"Idade {Pessoa_numero}"] # Acima_da media
                break
    soma_de_todas_as_idades = soma_de_todas_as_idades + Dados[f"Idade {Pessoa_numero}"] # Soma das Idades
    # Continua /Verificado
    continua = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        Lista.append(Todos.copy())    # lista de dados
        break
    elif continua == 'S':
        Lista.append(Todos.copy())    # lista de dados
        print('><'*20)
    else:
        while True:
            continua = str(input('Erro!, Você Quer Continuar Sim/Não?: ')).strip().upper()[0]
            if continua == 'N':
                conend = 2
                break
            elif continua == 'S':
                break
        if conend == 2:
            break
#     Fim do loop parte 1
print('><'*20)
#     Listagem
media = soma_de_todas_as_idades / Pessoa_numero # media das idades
print(f'- O Grupo tem {Pessoa_numero} Pessoas.')
print(f'- A Média de idade e de {media:.2f}Anos.')
print(f'- As Mulheres Cadastradas foram: ',end='')
for k,v in nome_das_mulheres.items():
    print(f'{v}',end='')
print(f'\n- Lista das pessoas que estão acima da Média:',end=' ')
for k,v in acima_da_media.items():
    if v >= media:
        print(Dados[k],end=' ')
print()
#     Final
for c,d in enumerate (Lista):
    print(f'{d}')
print('{:=^40}'.format(' Encerrado '))