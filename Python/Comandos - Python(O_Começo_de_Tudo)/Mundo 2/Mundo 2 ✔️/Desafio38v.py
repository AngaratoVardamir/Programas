print('\033[33m<'*10,'\033[36mComparação de Valores\033[m','\033[33m>\033[m'*10)
Pri_Núm = int(input('Primeiro Número: '))
Seg_Núm = int(input('Segundo Número: '))
print('\033[33m<'*21,'\033[33m>\033[m'*21)
if Seg_Núm < Pri_Núm:
    print('O Primeiro Valor é Maior')
elif Seg_Núm > Pri_Núm:
    print('O Segundo Valor é Maior')
else:
    print('Não existe Valor Maior, Os dois são iguais')
print('\033[33m<'*21,'\033[33m>\033[m'*21)