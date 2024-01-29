def Metade(preço):
    res = preço // 2
    return res


def Dobro(preço):
    res = preço * 2
    return res


def Aumentar(preço, Taxa):
    Taxa = 10
    res = preço + (preço * Taxa/100)
    return res


def Diminuir(preço, Taxa):
    Taxa = 13
    res = preço - (preço * Taxa/100)
    return res