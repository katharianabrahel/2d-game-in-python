import pygame
from sys import exit

pygame.init()
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('NOME DO JOGO')
clock = pygame.time.Clock()

background_teste = pygame.Surface((1280, 720))
background_teste.fill('black')

piso_teste = pygame.Surface((1280, 300))
piso_teste.fill('gray')

inimigo_teste = pygame.Surface((50, 50))
inimigo_teste.fill('yellow')
inimigo_rect = inimigo_teste.get_rect(bottomleft = (1230, 600))
movimento = 'esquerda'

player_teste = pygame.Surface((50, 50))
player_teste.fill('red')
player_rect = player_teste.get_rect(midbottom = (100, 600))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.blit(background_teste, (0, 0))
    tela.blit(piso_teste, (0, 600))
    
    if inimigo_rect.x <= 1230 and inimigo_rect.x > 2 and movimento == 'esquerda':
        inimigo_rect.x -= 2
    elif inimigo_rect.x == 2 and movimento == 'esquerda':
        movimento = 'direita'
        inimigo_rect.x += 2
    elif inimigo_rect.x >= 2 and inimigo_rect.x < 1230 and movimento == 'direita':
        inimigo_rect.x += 2
    elif inimigo_rect.x == 1230 and movimento == 'direita':
        movimento = 'esquerda'
        inimigo_rect.x -= 2
    tela.blit(inimigo_teste, inimigo_rect)
    tela.blit(player_teste, player_rect)

    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_rect.x += 4
        elif keys[pygame.K_LEFT]:
            player_rect.x -= 4
        if event.key == pygame.K_UP and player_rect.bottom >= 600:
            player_gravity = -20
    
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 600:
        player_rect.bottom = 600

    pygame.display.update()
    clock.tick(60)