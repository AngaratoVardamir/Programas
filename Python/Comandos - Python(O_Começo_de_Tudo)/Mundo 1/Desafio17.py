
co=int(input("Qual é o Comprimento do Cateto Oposto ?"))
ca=int(input("Qual é o Comprimento do Cateto adjacente ?"))

coca=co**2
caco=ca**2
hipo=(coca+caco)
xhipo=hipo**(1/2)

print("O Comprimento do hipotenusa é:{}".format(xhipo))
