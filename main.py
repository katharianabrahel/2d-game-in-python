import pygame, sys
from settings import *
from level import Level

tela_dimensoes = (1280, 720)
tela = pygame.display.set_mode((tela_dimensoes))
clock = pygame.time.Clock()
level = Level(level_map, tela)
jogar = False

pygame.init()  
color = (255,255,255)  
color_light = (170,170,170)  
color_dark = (100,100,100)  
smallfont = pygame.font.SysFont('Corbel',35)  
text = smallfont.render('Iniciar' , True , color)  

while True:
    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:  
            pygame.quit()  
            
        if ev.type == pygame.MOUSEBUTTONDOWN:  
                    if 640 <= mouse[0] <= 780 and 360 <= mouse[1] <= 400:  
                        jogar = True 
    tela.fill((0,0,0))  
    mouse = pygame.mouse.get_pos()  
    if 640 <= mouse[0] <= 780 and 360 <= mouse[1] <= 400:  
        pygame.draw.rect(tela,color_light,[640,360,140,40])  
    else:  
        pygame.draw.rect(tela,color_dark,[640,360,140,40])  
    tela.blit(text,(670,360))  


    if jogar == True:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            tela.fill('black')
            level.run()
            pygame.display.update()
            clock.tick(60)

    pygame.display.update()
