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
    tempo_restante = tempo - tempo_atual + ticks
    if tempo_restante == 0:
        pygame.quit()
        exit()
    return tempo_restante

def andar(velocidade):
    global player_status, player_direita
    keys = pygame.key.get_pressed()
    if velocidade:
        if keys[pygame.K_RIGHT]:
            player_direita = True
            player_status = 'Run'
            player_rect.x += 8
        elif keys[pygame.K_LEFT]:
            player_direita = False
            player_status = 'Run'
            player_rect.x -= 8
    else:
        if keys[pygame.K_RIGHT]:
            player_status = 'Walk'
            player_direita = True
            player_rect.x += 4
        elif keys[pygame.K_LEFT]:
            player_status = 'Walk'
            player_direita = False
            player_rect.x -= 4

def animacao_coletavel():
    global coletavel1, coletavel2, coletavel3, coin_index
    coin_index += 0.1
    if coin_index >= len(coin):
        coin_index = 0
    coletavel1 = coin[int(coin_index)]
    coletavel2 = coin[int(coin_index)]
    coletavel3 = coin[int(coin_index)]

def animacao_player():
    global player_index, player_direita, player_status, player_animacao, player
    player_index += 0.3
    if player_index > 10:
        player_index = 0
    if player_status == 'Idle':
        if not player_direita:
            player = player_animacao_idle[int(player_index)]
        else:
            player = pygame.transform.flip(player_animacao_idle[int(player_index)], True, False)
    elif player_status == 'Walk':
        if not player_direita:
            player = player_animacao_walk[int(player_index)]
        else:
            player = pygame.transform.flip(player_animacao_walk[int(player_index)], True, False)
    elif player_status == 'Run':
        if not player_direita:
            player = player_animacao_run[int(player_index)]
        else:
            player = pygame.transform.flip(player_animacao_run[int(player_index)], True, False)
    elif player_status == 'Jump':
        if not player_direita:
            player = player_animacao_jump[int(player_index)]
        else:
            player = pygame.transform.flip(player_animacao_jump[int(player_index)], True, False)

def animacao_inimigo():
    global inimigo_index, movimento, inimigo
    inimigo_index += 0.2
    if inimigo_index >= 10:
        inimigo_index = 0
    if movimento == 'direita':
        inimigo = pygame.transform.flip(inimigo_walk[int(inimigo_index)], True, False)
    else:
        inimigo = inimigo_walk[int(inimigo_index)]

pygame.init()
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('NOME DO JOGO')
fonte = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

background_teste = pygame.Surface((1280, 720))
background_teste.fill('black')

piso_teste = pygame.Surface((1280, 300))
piso_teste.fill('gray')

inimigo_index = 0
inimigo_walk_1 = pygame.image.load('images/enemy/walk/walk1.png')
inimigo_walk_2 = pygame.image.load('images/enemy/walk/walk2.png')
inimigo_walk_3 = pygame.image.load('images/enemy/walk/walk3.png')
inimigo_walk_4 = pygame.image.load('images/enemy/walk/walk4.png')
inimigo_walk_5 = pygame.image.load('images/enemy/walk/walk5.png')
inimigo_walk_6 = pygame.image.load('images/enemy/walk/walk6.png')
inimigo_walk_7 = pygame.image.load('images/enemy/walk/walk7.png')
inimigo_walk_8 = pygame.image.load('images/enemy/walk/walk8.png')
inimigo_walk_9 = pygame.image.load('images/enemy/walk/walk9.png')
inimigo_walk_10 = pygame.image.load('images/enemy/walk/walk10.png')

inimigo_walk = [inimigo_walk_1, inimigo_walk_2, inimigo_walk_3, inimigo_walk_4, inimigo_walk_5, inimigo_walk_6, inimigo_walk_7, inimigo_walk_8, inimigo_walk_9, inimigo_walk_10]

inimigo = inimigo_walk[int(inimigo_index)]
inimigo_rect = inimigo.get_rect(bottomleft = (1230, 607))
movimento = 'esquerda'

player_status = 'Idle'
player_direita = True
player_index = 0
player_animacao_idle_1 = pygame.image.load('images/player/idle/Idle(1).png')
player_animacao_idle_2 = pygame.image.load('images/player/idle/Idle(2).png')
player_animacao_idle_3 = pygame.image.load('images/player/idle/Idle(3).png')
player_animacao_idle_4 = pygame.image.load('images/player/idle/Idle(4).png')
player_animacao_idle_5 = pygame.image.load('images/player/idle/Idle(5).png')
player_animacao_idle_6 = pygame.image.load('images/player/idle/Idle(6).png')
player_animacao_idle_7 = pygame.image.load('images/player/idle/Idle(7).png')
player_animacao_idle_8 = pygame.image.load('images/player/idle/Idle(8).png')
player_animacao_idle_9 = pygame.image.load('images/player/idle/Idle(9).png')
player_animacao_idle_10 = pygame.image.load('images/player/idle/Idle(10).png')
player_animacao_idle = [player_animacao_idle_1, player_animacao_idle_2, player_animacao_idle_3, player_animacao_idle_4, player_animacao_idle_5, player_animacao_idle_6, player_animacao_idle_7, player_animacao_idle_8, player_animacao_idle_9, player_animacao_idle_10]

player_animacao_walk_1 = pygame.image.load('images/player/walk/Walk(1).png')
player_animacao_walk_2 = pygame.image.load('images/player/walk/Walk(2).png')
player_animacao_walk_3 = pygame.image.load('images/player/walk/Walk(3).png')
player_animacao_walk_4 = pygame.image.load('images/player/walk/Walk(4).png')
player_animacao_walk_5 = pygame.image.load('images/player/walk/Walk(5).png')
player_animacao_walk_6 = pygame.image.load('images/player/walk/Walk(6).png')
player_animacao_walk_7 = pygame.image.load('images/player/walk/Walk(7).png')
player_animacao_walk_8 = pygame.image.load('images/player/walk/Walk(8).png')
player_animacao_walk_9 = pygame.image.load('images/player/walk/Walk(9).png')
player_animacao_walk_10 = pygame.image.load('images/player/walk/Walk(10).png')
player_animacao_walk = [player_animacao_walk_1, player_animacao_walk_2, player_animacao_walk_3, player_animacao_walk_4, player_animacao_walk_5, player_animacao_walk_6, player_animacao_walk_7, player_animacao_walk_8, player_animacao_walk_9, player_animacao_walk_10]

player_animacao_run_1 = pygame.image.load('images/player/run/Run(1).png')
player_animacao_run_2 = pygame.image.load('images/player/run/Run(2).png')
player_animacao_run_3 = pygame.image.load('images/player/run/Run(3).png')
player_animacao_run_4 = pygame.image.load('images/player/run/Run(4).png')
player_animacao_run_5 = pygame.image.load('images/player/run/Run(5).png')
player_animacao_run_6 = pygame.image.load('images/player/run/Run(6).png')
player_animacao_run_7 = pygame.image.load('images/player/run/Run(7).png')
player_animacao_run_8 = pygame.image.load('images/player/run/Run(8).png')
player_animacao_run_9 = pygame.image.load('images/player/run/Run(9).png')
player_animacao_run_10 = pygame.image.load('images/player/run/Run(10).png')
player_animacao_run = [player_animacao_run_1, player_animacao_run_2, player_animacao_run_3, player_animacao_run_4, player_animacao_run_5, player_animacao_run_6, player_animacao_run_7, player_animacao_run_8, player_animacao_run_9, player_animacao_run_10]

player_animacao_jump_1 = pygame.image.load('images/player/jump/Jump(1).png')
player_animacao_jump_2 = pygame.image.load('images/player/jump/Jump(2).png')
player_animacao_jump_3 = pygame.image.load('images/player/jump/Jump(3).png')
player_animacao_jump_4 = pygame.image.load('images/player/jump/Jump(4).png')
player_animacao_jump_5 = pygame.image.load('images/player/jump/Jump(5).png')
player_animacao_jump_6 = pygame.image.load('images/player/jump/Jump(6).png')
player_animacao_jump_7 = pygame.image.load('images/player/jump/Jump(7).png')
player_animacao_jump_8 = pygame.image.load('images/player/jump/Jump(8).png')
player_animacao_jump_9 = pygame.image.load('images/player/jump/Jump(9).png')
player_animacao_jump_10 = pygame.image.load('images/player/jump/Jump(10).png')
player_animacao_jump = [player_animacao_jump_1, player_animacao_jump_2, player_animacao_jump_3, player_animacao_jump_4, player_animacao_jump_5, player_animacao_jump_6, player_animacao_jump_7, player_animacao_jump_8,player_animacao_jump_9, player_animacao_jump_10 ]

player = player_animacao_idle[player_index]
player_rect = player.get_rect(midbottom = (100, 600))
player_gravity = 20

coin1 = pygame.image.load('images/coin/coin_1.png')
coin2 = pygame.image.load('images/coin/coin_2.png')
coin3 = pygame.image.load('images/coin/coin_3.png')
coin4 = pygame.image.load('images/coin/coin_4.png')
coin5 = pygame.image.load('images/coin/coin_5.png')
coin6 = pygame.image.load('images/coin/coin_6.png')
coin7 = pygame.image.load('images/coin/coin_7.png')
coin8 = pygame.image.load('images/coin/coin_8.png')
coin = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8]
coin_index = 0

coletavel1 = coin[coin_index]
coletavel1_rect = coletavel1.get_rect(topleft = (300, 400))

coletavel2 = coin[coin_index]
coletavel2_rect = coletavel1.get_rect(topleft = (600, 400))

coletavel3 = coin[coin_index]
coletavel3_rect = coletavel1.get_rect(topleft = (900, 400))

energia_coletavel = pygame.image.load('images/energy.png')
energia_coletavel_rect = coletavel1.get_rect(topleft = (800, 400))

vida_coletavel = pygame.image.load('images/vida_coletavel.png')
vida_coletavel_rect = vida_coletavel.get_rect(topleft = (100, 400))

n_coletaveis = 0
vidas = 3

tres_vidas = pygame.image.load('images/tres_vidas.png')
duas_vidas = pygame.image.load('images/duas_vidas.png')
uma_vida = pygame.image.load('images/uma_vida.png')

velocidade = False


pygame.init()  
res = (1280,720)  
screen = pygame.display.set_mode(res)  
color = (255,255,255)  
color_light = (170,170,170)  
color_dark = (100,100,100)  
width = screen.get_width()  
height = screen.get_height()  
smallfont = pygame.font.SysFont('Corbel',35)  
text = smallfont.render('Iniciar' , True , color)  
iniciar = False
while True:  
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            
        if event.type == pygame.MOUSEBUTTONDOWN:  
                    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                        ticks = int(pygame.time.get_ticks() / 1000)
                        iniciar = True
    screen.fill((0,0,0))  
    mouse = pygame.mouse.get_pos()  

    if iniciar == True:
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

            animacao_inimigo()
            tela.blit(inimigo, inimigo_rect)
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

            animacao_player()
            tela.blit(player, player_rect) 
            if player_rect.colliderect(energia_coletavel_rect):
                velocidade = True
                energia_coletavel_rect.x = -300
            if event.type == pygame.KEYDOWN:
                andar(velocidade)
                if event.key == pygame.K_UP and player_rect.bottom >= 600:
                    player_gravity = -20
            else:
                player_status = 'Idle'

            if player_rect.x < -20:
                player_rect.x = -20
            elif player_rect.x > 1200:
                player_rect.x = 1200

            animacao_coletavel()
            tela.blit(coletavel1, coletavel1_rect)
            tela.blit(coletavel2, coletavel2_rect)
            tela.blit(coletavel3, coletavel3_rect)
            tela.blit(energia_coletavel, energia_coletavel_rect)
            tela.blit(vida_coletavel, vida_coletavel_rect)
            tela.blit(score, score_rect)
            if player_rect.colliderect(coletavel1_rect) or player_rect.colliderect(coletavel2_rect) or player_rect.colliderect(coletavel3_rect):
                n_coletaveis += 1
                pygame.mixer.music.load('sounds/coin.wav')
                pygame.mixer.music.play(0)
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
                    player_rect = player.get_rect(midbottom = (100, 600))
                    inimigo_rect = inimigo.get_rect(bottomleft = (1230, 600))
            if player_rect.colliderect(vida_coletavel_rect):
                if vidas < 3:
                    vidas += 1
                vida_coletavel_rect.x = -500
            if player_rect.bottom >= 600:
                player_rect.bottom = 600
            elif player_rect.bottom < 600:
                player_status = 'Jump'

            contador_vidas()
            pygame.display.update()
            clock.tick(60)
    
    
    
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])  
        
    else:  
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])  
    
    
    screen.blit(text ,(width/2+30,height/2))  
    pygame.display.update()
