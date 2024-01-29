print('\033[0;34;47m-\033[m'*40)
def voto():
    from datetime import date
    Ano_Real = date.today().year
    Idade_agora = Ano_Real - Ano_de_Nascimento 
    if 18 <= Idade_agora and Idade_agora <= 70: # Voto obrigatorio
        print(f'\033[0;32;47mCom {Idade_agora} Anos: Voto Obrigatorio.\033[m')
    else:
        print(f'\033[0;31;47mCom {Idade_agora} Anos: Voto Opcional.\033[m')


Ano_de_Nascimento = (int(input('\033[0;34;47mEm que ano Você Nasceu?: \033[m')))
voto()
print('\033[0;34;47m-\033[m'*40)