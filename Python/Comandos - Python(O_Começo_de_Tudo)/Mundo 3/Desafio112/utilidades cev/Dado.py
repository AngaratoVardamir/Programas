import moeda
def leiadinhero(preço):
    global res
    Preço = f'{preço}'.replace(',','.')
    res = Preço
    return res



preço = float(input('Digite o preço: R$'))
leiadinhero(preço)
preço = float(res)
moeda.Resumo(preço)