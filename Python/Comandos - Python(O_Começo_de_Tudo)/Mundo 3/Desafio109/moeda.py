def Metade(preço=0,formata=False):
    res = preço // 2
    return res if formata is False else Moeda(res)


def Dobro(preço=0,formata=False):
    res = preço * 2
    return res if formata is False else Moeda(res)


def Aumentar(preço=0, Taxa=0 , formata=False):
    Taxa = 10
    res = preço + (preço * Taxa/100)
    return res if formata is False else Moeda(res)


def Diminuir(preço=0, Taxa=0, formata=False):
    Taxa = 13
    res = preço - (preço * Taxa/100)
    return res if formata is False else Moeda(res)


def Moeda(preço=0 , Moeda='R$', formata=True):
    return f'{Moeda}{preço:>.2f}'.replace('.',',')
    #return res if formato is false else moeda(res)