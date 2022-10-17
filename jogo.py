import pygame
from sys import exit

def colisao_coletavel(player, coletavel):
    if player.colliderect(coletavel):
        coletavel.x = -300

def contador_vidas():
    if vidas == 3:
        tela.blit(tres_vidas, (500, 50))
    elif vidas == 2:
        tela.blit(duas_vidas, (500,50))
    elif vidas == 1:
        tela.blit(uma_vida, (500,50))
    else:
        pygame.quit()
        exit()

pygame.init()
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('NOME DO JOGO')
fonte = pygame.font.Font(None, 50)
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
player_gravity = 20

coletavel1 = pygame.Surface ((10, 10))
coletavel1.fill('blue')
coletavel1_rect = coletavel1.get_rect(topleft = (300, 400))

coletavel2 = pygame.Surface ((10, 10))
coletavel2.fill('blue')
coletavel2_rect = coletavel1.get_rect(topleft = (600, 400))

coletavel3 = pygame.Surface ((10, 10))
coletavel3.fill('blue')
coletavel3_rect = coletavel1.get_rect(topleft = (900, 400))

n_coletaveis = 0
vidas = 3
counter, timer = 100, '100'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

tres_vidas = pygame.image.load('images/tres_vidas.png')
duas_vidas = pygame.image.load('images/duas_vidas.png')
uma_vida = pygame.image.load('images/uma_vida.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            if counter > 0:
                timer = str(counter).rjust(3)
            else:
                pygame.quit()
                exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    score = fonte.render(f'Score: {n_coletaveis}', True, (255,255,255))
    score_rect = score.get_rect(topleft = (50, 50))

    tela.blit(background_teste, (0, 0))
    tela.blit(piso_teste, (0, 600))
    tela.blit(fonte.render("Time: " + timer, True, (255, 255, 255)), (1070, 50))
    
    tela.blit(inimigo_teste, inimigo_rect)
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
    
    tela.blit(player_teste, player_rect)
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_rect.x += 4
        elif keys[pygame.K_LEFT]:
            player_rect.x -= 4
        if event.key == pygame.K_UP and player_rect.bottom >= 600:
            player_gravity = -20

    tela.blit(coletavel1, coletavel1_rect)
    tela.blit(coletavel2, coletavel2_rect)
    tela.blit(coletavel3, coletavel3_rect)
    tela.blit(score, score_rect)
    if player_rect.colliderect(coletavel1_rect) or player_rect.colliderect(coletavel2_rect) or player_rect.colliderect(coletavel3_rect):
        n_coletaveis += 1
    colisao_coletavel(player_rect, coletavel1_rect)
    colisao_coletavel(player_rect, coletavel2_rect)
    colisao_coletavel(player_rect, coletavel3_rect)
    
    player_gravity += 1
    player_rect.y += player_gravity
    if player_gravity > 20:
        player_gravity = 21
    if player_rect.colliderect(inimigo_rect):
        if 0 <= player_gravity <= 20:
            inimigo_rect.x = -500
            player_gravity = -10
        else:
            vidas -= 1
            player_rect = player_teste.get_rect(midbottom = (100, 600))
            inimigo_rect = inimigo_teste.get_rect(bottomleft = (1230, 600))
    if player_rect.bottom >= 600:
        player_rect.bottom = 600

    contador_vidas()
    pygame.display.update()
    clock.tick(60)