contador = 0
palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

while True:
    print(f'\nA Palavra \033[33m{palavras[contador]}\033[m tem essas Vogais: ',end='')
    for v in palavras[contador]:
        if v == 'A' or v == 'E' or v == 'I' or v == 'O' or v == 'U':
            print(f'\033[36m{v}\033[m ',end='')
    contador = contador +1
    if contador == (len(palavras)):
        break
