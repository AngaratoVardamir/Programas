numero=int(input('Digite um Número ?'))
numero2=int(input('Digite outro Número ?'))

adicao=(numero+numero2)
subtracao=(numero-numero2)
multiplicacao=(numero*numero2)
divisao=(numero/numero2)
potencia=(numero**numero2)
divisaoint=(numero//numero2)
resto=(numero%numero2)
igual=(numero==numero2)





print('{}+{}={}'.format(numero,numero2,adicao))
print(' ')
print('{}-{}={}'.format(numero,numero2,subtracao))
print(' ')
print('{}*{}={}'.format(numero,numero2,multiplicacao))
print(' ')
print('{}/{}={}'.format(numero,numero2,divisao))
print(' ')
print('{}**{}={}'.format(numero,numero2,potencia))
print(' ')
print('{}//{}={}'.format(numero,numero2,divisaoint))
print(' ')
print('{}%{}={}'.format(numero,numero2,resto))
print(' ')
print('{}=={}={}'.format(numero,numero2,igual))
