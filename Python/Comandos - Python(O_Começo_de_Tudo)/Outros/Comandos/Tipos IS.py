algo=str(input("Digite Algo:"))
print('O {} é um Número ?{}'.format(algo,algo.isnumeric()))
print('O {} é uma Letra ?{}'.format(algo,algo.isalpha()))
print('O {} é uma Letra ou Número ?{}'.format(algo,algo.isalnum()))
print('O {} é uma Letra Maiúscula ?{}'.format(algo,algo.isupper()))
print('O {} é um Espaço ?{}'.format(algo,algo.isspacer()))
print('O {} é uma Letra Minúscula ?{}'.format(algo,algo.islower()))
print('O {} é uma Letra Maiúscula ou Minúscula ?{}'.format(algo,algo.istitle()))
