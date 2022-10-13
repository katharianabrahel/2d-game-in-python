import pygame
from sys import exit

pygame.init()
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('NOME DO JOGO')
clock = pygame.time.Clock()

background_teste = pygame.Surface((1280, 720))
background_teste.fill('black')

piso_teste = pygame.Surface((1280, 300))
piso_teste.fill('Gray')

inimigo_teste = pygame.Surface((50, 50))
inimigo_teste.fill('yellow')
inimigo_x_pos = 1230
movimento = 'esquerda'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.blit(background_teste, (0, 0))
    tela.blit(piso_teste, (0, 600))
    
    if inimigo_x_pos <= 1230 and inimigo_x_pos > 2 and movimento == 'esquerda':
        inimigo_x_pos -= 2
    elif inimigo_x_pos == 2 and movimento == 'esquerda':
        movimento = 'direita'
        inimigo_x_pos += 2
    elif inimigo_x_pos >= 2 and inimigo_x_pos < 1230 and movimento == 'direita':
        inimigo_x_pos += 2
    elif inimigo_x_pos == 1230 and movimento == 'direita':
        movimento = 'esquerda'
        inimigo_x_pos -= 2
    tela.blit(inimigo_teste, (inimigo_x_pos, 550))
  
    pygame.display.update()
    clock.tick(60)