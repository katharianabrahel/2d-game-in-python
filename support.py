import pygame

pygame.init()
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

coin1 = pygame.image.load('images/coin/coin_1.png')
coin2 = pygame.image.load('images/coin/coin_2.png')
coin3 = pygame.image.load('images/coin/coin_3.png')
coin4 = pygame.image.load('images/coin/coin_4.png')
coin5 = pygame.image.load('images/coin/coin_5.png')
coin6 = pygame.image.load('images/coin/coin_6.png')
coin7 = pygame.image.load('images/coin/coin_7.png')
coin8 = pygame.image.load('images/coin/coin_8.png')
coin = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8]


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

uma_vida = pygame.transform.flip(pygame.image.load('images/health_status/uma_vida.png'), True, False)
duas_vidas = pygame.transform.flip(pygame.image.load('images/health_status/duas_vidas.png'), True, False)
tres_vidas = pygame.transform.flip(pygame.image.load('images/health_status/tres_vidas.png'), True, False)

fonte = pygame.font.Font('font/ARCADEPI.TTF', 25)

lava_1 = pygame.image.load('images/lava/lava1.png')
lava_2 = pygame.image.load('images/lava/lava2.png')
lava = [lava_1, lava_2]