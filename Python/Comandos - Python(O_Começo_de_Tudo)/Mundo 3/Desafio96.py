def linha():
    print('~'*50)

def area():
    area = Largura * Comprimento
    print(f'A área de um Terreno {Largura} x {Comprimento} é de {area}m².')

linha()#aparecer
print(' Controle do Terrenos')#aparecer
linha()#aparecer
Largura = float(input('Largura (m): '))#aparecer
Comprimento = float(input('Comprimento (m): '))#aparecer
area()