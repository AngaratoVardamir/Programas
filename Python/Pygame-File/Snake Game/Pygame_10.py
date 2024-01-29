# Pygame Aula #10 - O Jogo da Cobrianha (Snake Game) Parte 3

# Imports
import pygame                                # Importação da blibioteca Pygame
from pygame.locals import *                  # Sub-Modulo da Blibioteca Pygame / O * é para importa tudo Dentro do Modulo
from sys import exit                         # Quando Clicar Fechar Janela ela fechar a janela
from random import randint
pygame.init()                                # Inicializador da Blibiotecar pygame

#Musicas
pygame.mixer.music.set_volume(0.30) # Volume de fundo do jogo# Recomedado por 0 ou 1
Musica_de_Fundo = pygame.mixer_music.load('Pygame_10Musicadefundo.mp3') # Musica de Fundo
pygame.mixer_music.play(-1) # Musica Infinita

Barulho_Colisao = pygame.mixer.Sound('Pygame_10Efeito.wav') # Efeito sonoro da Colisão o efeito Sonoro tem que estar em .Wav senão da erro
Barulho_Colisao.set_volume(0.40)  # Volume do efeito sonoro do jogo# Recomedado por 0 ou 1
# Variaveis do Tamanho da Tela
Largura = 640
Altura  = 480

# Variaveis de Movimento
x_Cobra = int(Largura/ 2)
y_Cobra = int(Altura / 2)

# Velocidade
Velocidade = 10

# Controle
X_Controle = Velocidade
Y_Controle = 0

# Invocão do Demonio Azul kkkk
x_Maca = randint(40, 600)
y_Maca = randint(50, 430)
# Pontos
Pontos = 0
# Fonte Texto
# Para Saber As Fontes Disponiveis degite :pygame.font.get_fonts() no terminal
fonte = pygame.font.SysFont('arial', 40 , True , True)

Tela = pygame.display.set_mode((Largura, Altura))   # Essa Função Set_mode Vai receber uma Tupla e essa Tapla vai receber A Largura e Autura
pygame.display.set_caption('Snake Game')                                   # Altera o Nome da Janela
# Frames controle
Relogio = pygame.time.Clock()
# Aumetar Cobra 
Lista_Cobra = []
Comprimento_Inicial = 5 # Comprimeto Inicial da Cobra
def Aumetar_Cobra(Lista_Cobra):
    for XeY in Lista_Cobra:
        # XeY = [x , Y]
        pygame.draw.rect(Tela, (0,255,0), (XeY[0], XeY[1], 20,20)) # Corpo da Cobra

def Reiniciar_Jogo():
    global Pontos ,Comprimento_Inicial ,x_Cobra ,y_Cobra ,Lista_Cobra ,Lista_Cabeca ,x_Maca ,y_Maca ,Morreu
    Pontos = 0
    Comprimento_Inicial = 11
    x_Cobra = int(Largura/ 2)
    y_Cobra = int(Altura / 2)
    Lista_Cobra = []
    Lista_Cabeca = []
    x_Maca = randint(40, 600)
    y_Maca = randint(50, 430)
    Morreu = False

# Todo o jogo se passar em Loop Infinito
while True:
    Relogio.tick(30)              # Quantos Frames por Segundo o jogo vai ter
    Tela.fill((255,255,255))          # Pecher a Tela com uma Cor determinada
    Mensagem = f'Pontos: {Pontos}' # Mensagem na Tela
    Texto_Formatado = fonte.render(Mensagem, True, (0,0,0)) # Mesagem Pontos , Pixelado sim=False Não=True, Cores RGB
    for event in pygame.event.get():       # O Loop For vai Checar se ocorreu um Evento
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN: # Controle do teclado
            if event.key == K_a: # a tecla "A" for Presionada vai acontecer Algo
                if X_Controle == Velocidade:
                    pass
                else:
                    X_Controle =- Velocidade       # move pra Esquerda
                    Y_Controle =  0
            if event.key == K_d:
                if X_Controle == -Velocidade:
                    pass
                else:
                    X_Controle =  Velocidade
                    Y_Controle =  0
            if event.key == K_w:
                if X_Controle == Velocidade:
                    pass
                else:
                    X_Controle =  0
                    Y_Controle =- Velocidade
            if event.key == K_s:
                if X_Controle == -Velocidade:
                    pass
                else:
                    X_Controle =  0
                    Y_Controle =  Velocidade

    x_Cobra = x_Cobra + X_Controle
    y_Cobra = y_Cobra + Y_Controle
    
    Cobra = pygame.draw.rect(Tela, (0,255,0), (x_Cobra,y_Cobra,20,20))      # Onde Retragulo vai ser Desnhado , A Cor do Retragulo , Posição X e Y e Largura do Retragulo e Alutura
    Maca = pygame.draw.rect(Tela, (255,0,0), (x_Maca,y_Maca,20,20))

    #Colisor
    if Cobra.colliderect(Maca): #Toda vez que o vermelho colidir com azul vai acontecer isso:
        x_Maca = randint(40, 600)
        y_Maca = randint(50, 430)
        Pontos = Pontos +1
        Barulho_Colisao.play() # Efeito sonoro de Colisão Ativar
        Comprimento_Inicial = Comprimento_Inicial +1 #crecimento da cobra
        Morreu = False
        
    #Lista de Crecimento
    Lista_Cabeca = []
    Lista_Cabeca.append(x_Cobra)
    Lista_Cabeca.append(y_Cobra)
    
    Lista_Cobra.append(Lista_Cabeca)

    if Lista_Cobra.count(Lista_Cabeca) > 1: # EmCostar nela mesma
        fonte2 = pygame.font.SysFont('arial',20,True,True)#fonte , tamanho , Negrito
        Mensagem = 'Game Over! Pressione a Tecla R Para Jogar Novamente'
        Texto_Formatado = fonte2.render(Mensagem, True, (0,0,0))
        ret_texto = Texto_Formatado.get_rect()

        Morreu = True
        while Morreu:
            
            Tela.fill((255,255,255))
            for event in pygame.event.get():       # O Loop For vai Checar se ocorreu um Evento
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        Reiniciar_Jogo()
            ret_texto.center = (Largura//2, Altura // 2)
            Tela.blit(Texto_Formatado, ret_texto)  # texto morreu
            pygame.display.update()

    if x_Cobra > Largura:
        x_Cobra = 0
    if x_Cobra < 0:
        x_Cobra = Largura

    if y_Cobra > Altura:
        y_Cobra = 0
    if y_Cobra < 0:
        y_Cobra = Altura


    if len(Lista_Cobra) > Comprimento_Inicial:
        del Lista_Cobra[0]

    Aumetar_Cobra(Lista_Cobra)

    Tela.blit(Texto_Formatado, (420,40))   # Posição do Texto
    
    pygame.display.update()                # Atualiza à tela do Jogo