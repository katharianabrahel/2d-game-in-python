import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('images/tile5.png')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
        