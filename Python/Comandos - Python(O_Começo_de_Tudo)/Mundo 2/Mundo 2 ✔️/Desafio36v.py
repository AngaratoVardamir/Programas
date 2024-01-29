print('<'*8,' Calcule o Emprestimo ','>'*8)
Valor_Casa = float(input('Qual é o Valor da Casa? R$'))
salario = float(input('Qual é o Seu Salário? R$'))
anos_Pagamento = int(input('Quantos Anos Você pode Pagar?: '))
Pestação = Valor_Casa // (anos_Pagamento*12)
salario30 = ((salario*130)/100)
print('='*40)
if Pestação <= salario30:
    print(f'Seu Empréstimo de {anos_Pagamento} Anos Foi Aprovado, Você Vai pagar R${Pestação:.2f} por mes')
else:
    print(f'Seu Empréstimo de {anos_Pagamento} Anos Foi Negado, Você Não tem Dinheiro Suficiente')