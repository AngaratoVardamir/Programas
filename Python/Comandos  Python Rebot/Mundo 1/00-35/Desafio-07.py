#Lista
Notas = []
#Cotadores
End = ''
Prova = 0
Soma = 0
#Pricipal
print('='*50)
while True:
    if End == '010111001':
        break
    Prova = Prova +1
    Notas.append(float(input(f'Nota-0{Prova}: ')))
    Soma = Soma + Notas[Prova-1]
    while True:
        Acabou = str(input('Finalizar?: ')).strip().upper()[0]
        if Acabou == 'S':
            End = '010111001'
            break
        elif Acabou == 'N':
            break
# Finalizando
space = '     ' * len(Notas)
print('='*50)
print(f'[ Números{space} ][ Média ]')
media = Soma // Prova
print(f'   {Notas}          {media}')
print('='*50)