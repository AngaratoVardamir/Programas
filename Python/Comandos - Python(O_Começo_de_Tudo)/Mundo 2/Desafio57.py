print('{:~^40}'.format('\033[32m Desafio 57 ✔️ \033[m'))#02/08/2023

sexo = str(input('informe seu Sexo [\033[32mM\033[m/\033[31mF\033[m]: ')).strip().upper()[0]  # noqa: E501
while sexo not in 'MF':
    sexo = str(input('Sexo invalido tente novamente [\033[32mM\033[m/\033[31mF\033[m]: ')).strip().upper()[0]  # noqa: E501
if sexo == 'F':
    print('\033[31m', end='')
    sexoc = sexo
else:
    print('\033[32m', end='')
    sexoc = sexo
print('Sexo {}\033[m Registrado com Sucesso'.format(sexoc))
