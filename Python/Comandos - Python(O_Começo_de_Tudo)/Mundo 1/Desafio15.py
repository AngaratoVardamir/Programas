#dias=8
#km=720
#total R$:588.00

dia=int(input("Quantos dias o Carro foi Alugado?"))
km=int(input("Quantos Km Rodados do Carro?"))
dakm=((dia*60.0)+(km*0.15))
print("Vocé tem que Pagar R$:{}".format(dakm))
