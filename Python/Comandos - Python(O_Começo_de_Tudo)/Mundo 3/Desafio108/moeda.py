def Metade(preço=0):
    res = preço // 2
    return res


def Dobro(preço=0):
    res = preço * 2
    return res


def Aumentar(preço=0, Taxa=0):
    Taxa = 10
    res = preço + (preço * Taxa/100)
    return res


def Diminuir(preço=0, Taxa=0):
    Taxa = 13
    res = preço - (preço * Taxa/100)
    return res


def Moeda(preço=0 , Moeda='R$'):
    return f'{Moeda}{preço:>0.2f}'.replace('.',',')