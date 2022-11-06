import pygame
from support import coin

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.coin_index = 0
        self.animation_speed = 0.1
        self.image = coin[self.coin_index]
        self.rect = self.image.get_rect(topleft = pos)

    def animation_coins(self):
        self.coin_index += self.animation_speed
        if self.coin_index >= len(coin):
            self.coin_index = 0
        self.image = coin[int(self.coin_index)]
        

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animation_coins()