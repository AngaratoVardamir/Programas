def Preço(preço=0,formata=False):
    res = preço
    return res if formata is False else Moeda(res)
def Metade(preço=0,formata=False):
    res = preço // 2
    return res if formata is False else Moeda(res)


def Dobro(preço=0,formata=False):
    res = preço * 2
    return res if formata is False else Moeda(res)


def Aumentar(preço=0, Taxa=0 , formata=False):
    Taxa = 80
    res = preço + (preço * Taxa/100)
    return res if formata is False else Moeda(res)


def Diminuir(preço=0, Taxa=0, formata=False):
    Taxa = 35
    res = preço - (preço * Taxa/100)
    return res if formata is False else Moeda(res)


def Moeda(preço=0 , Moeda='R$', formata=True):
    return f'{Moeda}{preço:>.2f}'.replace('.',',')
    #return res if formato is false else (res)


def Resumo(preço=0, formata=False):
    print('='*40)
    print('           Resumo do Valor          ')
    print('='*40)
    print(f'''Preço Analizando: {Preço(preço,True):>22}
Dobro do Preço: {Dobro(preço,True):>24}
Metade do Preço: {Metade(preço,True):>23}
Aumentado 80%, temos {Aumentar(preço, 80 ,True):>19}
Reduzindo 35%, temos {Diminuir(preço, 35 ,True):>19}''')
    print('='*40)