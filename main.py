import pygame, sys
from settings import *
from level import Level
from support import fonte
from pygame import mixer

def cronometro(level):
    if level.game_status == 'play':
        tempo = 100
        tempo_atual = int(pygame.time.get_ticks() / 1000)
        tempo_restante = tempo - tempo_atual + ticks
        font = fonte
        display_tempo = font.render(str(tempo_restante), False, (255, 255, 255))
        tela.blit(display_tempo, (1170, 40))
        clock = pygame.image.load('images/powerup/clock.png')
        tela.blit(clock, (1125, 35))
        if tempo_restante == 0:
            level.game_status = 'game-over'

pygame.init()
mixer.init()
pygame.display.set_caption('Lost Coin')
tela_dimensoes = (1280, 720)
tela = pygame.display.set_mode((tela_dimensoes))
clock = pygame.time.Clock()
level = Level(level_map, tela)
cont = 0

while True:
    if level.game_status == 'play':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        color = (20, 23, 51)
        tela.fill(color)
        level.run()
        cronometro(level)

    elif level.game_status == 'start':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ticks = int(pygame.time.get_ticks() / 1000)
                    level.game_status = 'play'
        while cont == 0:
            pygame.mixer.init()
            pygame.mixer.music.load("sounds/song.mp3")
            pygame.mixer.music.play(-1)
            cont = 1
        title = pygame.image.load('images/logo.png')
        tela.fill('black')
        tela.blit(title, (100, 70))
        font = pygame.font.Font('font/ARCADEPI.TTF', 15)
        comecar = font.render('PRESSIONE ESPACO PARA COMECAR', False, (255, 255,255))
        instrucoes1 = font.render('INSTRUCOES', False, (255, 255,255))
        instrucoes2 = font.render('Colete as 10 moedas perdidas para ganhar o jogo', False, (255, 255,255))
        instrucoes3 = font.render('Aperte <- para mover para esquerda e -> para mover para direita', False, (255, 255,255))
        instrucoes4 = font.render('Aperte cima para pular. Pule nos inimigos e derrote-os', False, (255, 255,255))
        tela.blit(comecar, (450, 400))
        tela.blit(instrucoes1, (550, 500))
        tela.blit(instrucoes2, (350, 530))
        tela.blit(instrucoes3, (250, 560))
        tela.blit(instrucoes4, (325, 590))
    
    elif level.game_status == 'game-over':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
        font = pygame.font.Font('font/ARCADEPI.TTF', 17)
        while cont == 1: 
            mixer.init() 
            mixer.music.load("sounds/over.mp3") 
            mixer.music.play(0) 
            cont = 2
        game_over = pygame.image.load('images/game_over.png')
        fim = font.render('VOCE FALHOU AO TENTAR COLETAR AS MOEDAS PERDIDAS.', False, (255, 255, 255))
        fim1 = font.render('SUA ARMADURA JUNTOU-SE AO EXERCITO DE ESQUELETOS FORMADO POR AQUELES QUE OUTRORA FALHARAM.', False, (255, 255, 255))
        fim2 = font.render('TENTE NOVAMENTE EM OUTRA JORNADA.', False, (255, 255, 255))
        fechar = font.render('PRESSIONE ESPACO PARA FINALIZAR', False, (255, 255, 255))
        tela.fill('black')
        tela.blit(game_over, (0, 0))
        tela.blit(fim, (300, 350))
        tela.blit(fim1, (30, 400))
        tela.blit(fim2, (390, 450))
        tela.blit(fechar, (400, 550))
    elif level.game_status == 'win':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
        while cont == 1: 
            mixer.init() 
            mixer.music.load("sounds/win.mp3") 
            mixer.music.play(0) 
            cont = 2
        font = pygame.font.Font('font/ARCADEPI.TTF', 17)
        win = pygame.image.load('images/win.png')
        texto = font.render('PARABENS! VOCE CONSEGUIU!', False, (255, 255, 255))
        texto1 = font.render('VOCE REUNIU AS MOEDAS PERDIDAS. AGORA VOCE E VISTO COMO UM HEROI!', False, (255, 255, 255))
        texto2 = font.render('APROVEITE SUA VIDA DE RIQUEZAS E GLORIAS!', False, (255, 255, 255))
        finalizar = font.render('PRESSIONE ESPACO PARA FINALIZAR', False, (255, 255, 255))
        tela.fill('black')
        tela.blit(win, (0, 0))
        tela.blit(texto, (460, 350))
        tela.blit(texto1, (220, 400))
        tela.blit(texto2, (350, 450))
        tela.blit(finalizar, (400, 550))

    pygame.display.update()
    clock.tick(60)