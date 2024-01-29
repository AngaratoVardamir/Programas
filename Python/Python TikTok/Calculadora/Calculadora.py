# imports
from tkinter import *
from tkinter import ttk

# Cores
Cor_Preta = "#1e1f1e"
Cor_Branca = "#feffff"
Cor_Azul = "#38576b"
Cor_Cinza = "#ECEFF1"
Cor_Laranja = "#FFAB40"

# Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=Cor_Preta)

# Frames
framedatela = Frame(janela, width=235, height=50, bg=Cor_Azul)
framedatela.grid(row=0, column=0)

frame_Corpo = Frame(janela, width=235, height=268)
frame_Corpo.grid(row=1, column=0)

# Variavel Todos Valores

Todos_Valores = ''

#Label
Valor_Texto = StringVar()

#Função
def Entrar_Valores(event):

    global Todos_Valores

    Todos_Valores = Todos_Valores + str(event)

    #Passando Valor para Tela
    Valor_Texto.set(Todos_Valores)

#Função para Calcular

def Calcular():
    global Todos_Valores
    Resultado = eval(Todos_Valores)

    Valor_Texto.set(str(Resultado))

# Função Limpar Tela

def Limpar_Tela():
    global Todos_Valores
    Todos_Valores = ""
    Valor_Texto.set("")


app_label = Label(framedatela, textvariable=Valor_Texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 ') ,bg=Cor_Azul ,fg=Cor_Branca)
app_label.place(x=0,y=0)

#Botoes
Botão_1 = Button(frame_Corpo, command = Limpar_Tela ,text="C", width=11, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_1.place(x=0, y=0)

Botão_2 = Button(frame_Corpo, command = lambda: Entrar_Valores('%') , text="%", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_2.place(x=118, y=0)

Botão_3 = Button(frame_Corpo, command = lambda: Entrar_Valores('//') ,text="/", width=5, height=2, bg=Cor_Laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_3.place(x=177, y=0)

Botão_4 = Button(frame_Corpo, command = lambda: Entrar_Valores('7') ,text="7", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_4.place(x=0, y=52)

Botão_5 = Button(frame_Corpo, command = lambda: Entrar_Valores('8') ,text="8", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_5.place(x=59, y=52)

Botão_6 = Button(frame_Corpo, command = lambda: Entrar_Valores('9') ,text="9", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_6.place(x=118, y=52)

Botão_7 = Button(frame_Corpo, command = lambda: Entrar_Valores('*') ,text="*", width=5, height=2, bg=Cor_Laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_7.place(x=177, y=52)

Botão_8 = Button(frame_Corpo, command = lambda: Entrar_Valores('4') ,text="4", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_8.place(x=0, y=104)

Botão_9 = Button(frame_Corpo, command = lambda: Entrar_Valores('5') ,text="5", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_9.place(x=59, y=104)

Botão_9 = Button(frame_Corpo, command = lambda: Entrar_Valores('6') ,text="6", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_9.place(x=118, y=104)

Botão_9 = Button(frame_Corpo, command = lambda: Entrar_Valores('-') ,text="-", width=5, height=2, bg=Cor_Laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_9.place(x=177, y=104)

Botão_10 = Button(frame_Corpo, command = lambda: Entrar_Valores('1') ,text="1", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_10.place(x=0, y=156)

Botão_11 = Button(frame_Corpo, command = lambda: Entrar_Valores('2') ,text="2", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_11.place(x=59, y=156)

Botão_12 = Button(frame_Corpo, command = lambda: Entrar_Valores('3') ,text="3", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_12.place(x=118, y=156)

Botão_13 = Button(frame_Corpo, command = lambda: Entrar_Valores('+') ,text="+", width=5, height=2, bg=Cor_Laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_13.place(x=177, y=156)
#Aqui
Botão_14 = Button(frame_Corpo, command = lambda: Entrar_Valores('0') ,text="0", width=11, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_14.place(x=0, y=208)

Botão_15 = Button(frame_Corpo, command = lambda: Entrar_Valores('.') ,text=".", width=5, height=2, bg=Cor_Cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_15.place(x=118, y=208)

Botão_16 = Button(frame_Corpo, command = Calcular ,text="=", width=5, height=2, bg=Cor_Laranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Botão_16.place(x=177, y=208)



janela.mainloop()