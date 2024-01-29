Nome = str(input('Qual é o seu Nome?: ')).strip().capitalize()
if Nome == '':
    Nome = 'Desconhecido'
print(f'Olá {Nome}! Prazer em te Conhecer!')