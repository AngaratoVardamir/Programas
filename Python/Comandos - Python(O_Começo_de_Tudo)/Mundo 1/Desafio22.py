nome=str(input('Digite seu nome completo:')).strip()
separa=nome.split()

print('Analisando...')
print('Seu Nome em Maiúsculo é {}'.format(nome.upper()))
print('Seu Nome em Minúsculo é {}'.format(nome.lower()))
print('Seu Nome tem ao todo {} Letras'.format(len(nome)-nome.count(' ')))
print('Seu Primeiro nome é {} ele tem {} Letras'.format(separa[0],nome.find(' ')))
