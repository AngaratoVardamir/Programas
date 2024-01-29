print('{:~^40}'.format('\033[32m Desafio 12 ✔️ \033[m'))#24/08/2023

preço = float(input("Digite o Preço do Produto R$"))
desconto = int(input('Quanto de Desconto Você Quer? '))

proganho = (preço-(preço * desconto / 100))

print(f'{f"{desconto}% Desconto":.^30}')
print(" ")
print("Produto Original     :R${}  ".format(preço))
print("Desconto Ganho       : {:.0f}% ".format(desconto))
print("Produto com Desconto :R${:.2f}  ".format(proganho))