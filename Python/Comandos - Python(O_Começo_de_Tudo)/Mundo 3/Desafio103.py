print('='*60)
# Escopo Local
def Ficha(Nome_Jogador=0,Nume_Gols=0):
    if Nome_Jogador == '':
        Nome_Jogador = '< Desconhecido >'
    elif Nume_Gols == '':
        Nume_Gols = '0'
    print(f'O Jogador {Nome_Jogador} fez {Nume_Gols} gol(s) no Campeonato.')
# Escopo Global
Nome_Jogador = str(input('Nome do Jogador: ')).strip().capitalize()
Nume_Gols = str(input('Número de Gols: ')).strip().capitalize()
Ficha(Nome_Jogador,Nume_Gols)
print('='*60)