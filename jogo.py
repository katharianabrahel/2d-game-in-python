import pygame
from sys import exit

def colisao_coletavel(player, coletavel):
    if player.colliderect(coletavel):
        coletavel.x = -300

def contador_vidas():
    if vidas == 3:
        tela.blit(tres_vidas, (500, 50))
    elif vidas == 2:
        tela.blit(duas_vidas, (500, 50))
    elif vidas == 1:
        tela.blit(uma_vida, (500, 50))
    else:
        pygame.quit()
        exit()

def cronometro(tempo):
    tempo_atual = int(pygame.time.get_ticks() / 1000)
    tempo_restante = tempo - tempo_atual
    if tempo_restante == 0:
        pygame.quit()
        exit()
    return tempo_restante

def andar(velocidade):
    keys = pygame.key.get_pressed()
    if velocidade:
        if keys[pygame.K_RIGHT]:
            player_rect.x += 8
        elif keys[pygame.K_LEFT]:
            player_rect.x -= 8
    else:
        if keys[pygame.K_RIGHT]:
            player_rect.x += 4
        elif keys[pygame.K_LEFT]:
            player_rect.x -= 4

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

coletavel1 = pygame.Surface((10, 10))
coletavel1.fill('blue')
coletavel1_rect = coletavel1.get_rect(topleft = (300, 400))

coletavel2 = pygame.Surface((10, 10))
coletavel2.fill('blue')
coletavel2_rect = coletavel1.get_rect(topleft = (600, 400))

coletavel3 = pygame.Surface((10, 10))
coletavel3.fill('blue')
coletavel3_rect = coletavel1.get_rect(topleft = (900, 400))

energia_coletavel = pygame.Surface((10, 10))
energia_coletavel.fill('yellow')
energia_coletavel_rect = coletavel1.get_rect(topleft = (800, 400))

vida_coletavel = pygame.image.load('images/vida_coletavel.png')
vida_coletavel_rect = vida_coletavel.get_rect(topleft = (100, 400))

n_coletaveis = 0
vidas = 3

tres_vidas = pygame.image.load('images/tres_vidas.png')
duas_vidas = pygame.image.load('images/duas_vidas.png')
uma_vida = pygame.image.load('images/uma_vida.png')

velocidade = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    score = fonte.render(f'Score: {n_coletaveis}', True, (255, 255, 255))
    score_rect = score.get_rect(topleft = (50, 50))

    tela.blit(background_teste, (0, 0))
    tela.blit(piso_teste, (0, 600))
    tela.blit(fonte.render("Time: " + str(cronometro(100)), True, (255, 255, 255)), (1070, 50))

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
    if player_rect.colliderect(energia_coletavel_rect):
        velocidade = True
        energia_coletavel_rect.x = -300
    if event.type == pygame.KEYDOWN:
        andar(velocidade)
        if event.key == pygame.K_UP and player_rect.bottom >= 600:
            player_gravity = -20

    if player_rect.x < 0:
        player_rect.x = 0
    elif player_rect.x > 1230:
        player_rect.x = 1230

    tela.blit(coletavel1, coletavel1_rect)
    tela.blit(coletavel2, coletavel2_rect)
    tela.blit(coletavel3, coletavel3_rect)
    tela.blit(energia_coletavel, energia_coletavel_rect)
    tela.blit(vida_coletavel, vida_coletavel_rect)
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
    if player_rect.colliderect(vida_coletavel_rect):
        if vidas < 3:
            vidas += 1
        vida_coletavel_rect.x = -500
    if player_rect.bottom >= 600:
        player_rect.bottom = 600

    contador_vidas()
    pygame.display.update()
    clock.tick(60)