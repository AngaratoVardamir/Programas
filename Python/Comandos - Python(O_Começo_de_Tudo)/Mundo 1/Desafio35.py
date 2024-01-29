import math
l1=float(input('Linha 1='))
l2=float(input('Linha 2='))
l3=float(input('Linha 3='))

triangulo1=math.sin(math.radians(l1))
triangulo2=math.cos(math.radians(l2))
triangulo3=math.tan(math.radians(l3))

igual=l1
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Virou  Triângulo")
else:
    print("Não Virou  Triângulo")
