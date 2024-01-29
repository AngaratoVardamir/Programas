objectos = []
expre = str(input('Digite a expressão: '))
for digi in expre:
    if digi == '(':
        objectos.append('(')
    elif digi == ')':
        if len(objectos) > 0:
            objectos.pop()
        else:
            objectos.append(')')

if len( objectos ) == 0:
    print('Sua expressão está Valida!')
else:
    print('Sua expressão está Errada!')