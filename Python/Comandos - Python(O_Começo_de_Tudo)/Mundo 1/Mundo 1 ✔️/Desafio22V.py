print('{:~^40}'.format('\033[32m Desafio 22 ✔️ \033[m'))#25/08/2023

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando...')
print('Seu Nome em Maiúsculo é {}'.format(nome.upper()))
print('Seu Nome em Minúsculo é {}'.format(nome.lower()))
print('Seu Nome tem ao todo {} Letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu Primeiro nome é {} ele tem {} Letras'.format(separa[0], len(separa[0])))