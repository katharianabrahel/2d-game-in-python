import pygame

class Boost(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('images/powerup/energy.png')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        self.image

class HP(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('images/powerup/heart.png')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift
        self.image