print('='*50)
Algo = str(input('Digite Algo: ')).capitalize().strip()
num_let = Algo.isnumeric()
# Controle
if Algo == 'True':
    Classe = 'Bool'
elif '.' in Algo:
    Classe = 'Float'
elif Algo == 'False':
    Classe = 'Bool'
elif num_let == True:
    Classe = 'Int'
else:
    Classe = 'Str'

print(f'O Tipo Primitivo desse Valor é Class {Classe}')
print('='*50)