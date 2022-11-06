import pygame
from support import inimigo_walk

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.enemy_index = 0
        self.animation_speed = 0.2
        self.esquerda = True
        self.image = inimigo_walk[self.enemy_index]
        self.rect = self.image.get_rect(topleft = pos)

    def animation_enemy(self):
        self.enemy_index += self.animation_speed
        if self.enemy_index >= len(inimigo_walk):
            self.enemy_index = 0
        if self.esquerda:
            self.image = inimigo_walk[int(self.enemy_index)]
        else:
            self.image = pygame.transform.flip(inimigo_walk[int(self.enemy_index)], True, False)

    def move(self):
        if self.esquerda:
            self.rect.x -= 2
        else:
            self.rect.x += 2

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animation_enemy()
        self.move()

class Invi_wall(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift