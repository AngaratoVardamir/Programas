# Pygame Aula #12 - Sprites
# Imports
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
# Tamanho da Tela
Largura = 640
Altura = 480
# Cores
Preto = (0,0,0)
# Tela
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Sprites')
# Sprites
class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Sprite = []    #Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_1.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_2.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_3.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_4.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_5.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_6.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_7.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_8.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_9.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_12\Sprites/attack_10.png'))# Adicionar image na Lista
        self.atual = 0
        self.image = self.Sprite[self.atual] #Pegando imagem atual
        self.image = pygame.transform.scale(self.image, (128*3,64*3)) # Tamanho da Imagem

        self.rect = self.image.get_rect()
        self.rect.topleft = 100 , 100               # Posição da sprite

        self.animar = False
    def atacar(self):
        self.animar = True
    def update(self): # Interação
        if self.animar == True:
            self.atual = self.atual +0.5 # Velocidade
            if self.atual >= len(self.Sprite):
                self.atual = 0
                self.animar = False
            self.image = self.Sprite[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3,64*3)) # Tamanho da Imagem

Todas_as_sprites = pygame.sprite.Group()
sapo = Sapo() # objeto
Todas_as_sprites.add(sapo)

Relogio = pygame.time.Clock()
# Loop
while True:
    Relogio.tick(30) # Taxa de Frames
    Tela.fill(Preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()
    
    Todas_as_sprites.draw(Tela)
    Todas_as_sprites.update()
    pygame.display.flip()