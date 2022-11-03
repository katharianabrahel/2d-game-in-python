import pygame, sys
from settings import *
from level import Level


pygame.init()
tela_dimensoes = (1280, 720)
tela = pygame.display.set_mode((tela_dimensoes))
clock = pygame.time.Clock()
level = Level(level_map, tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tela.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)