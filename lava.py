import pygame
from support import lava

class Lava(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.contador_coin = 0
        self.index = 0
        self.image = lava[self.index]
        self.rect = self.image.get_rect(topleft = pos)

    def animation_lava(self):
        self.index += 0.15
        if self.index >= len(lava):
            self.index = 0
        self.image = lava[int(self.index)]
        

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animation_lava()