print('{:~^40}'.format('\033[32m Desafio 29 ✔️ \033[m'))#25/08/2023
print(f'{" Não Passe dos 80Km ou Será Multado ":=^50}')
km = int(input('Qual é a Velocidade do Seu Carro? Km'))
real = ((km-80)*7.00)
if km <=80:
    print('Boa Viagem e \033[33mSiga As Regras\033[m')
else:
    print('''\033[31mVocé foi Multado !!!\033[m
O Preço da Sua Multa é \033[32mR${}\033[m'''.format(real))