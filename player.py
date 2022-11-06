import pygame
from math import sin
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.contador_coins = 0
        self.player_index = 0
        self.animation_speed = 0.3
        self.status = 'idle'
        self.direita = True
        self.image = pygame.transform.flip(player_animacao_idle[int(self.player_index)], True, False)
        self.rect = self.image.get_rect(topleft = pos)
        self.boost_speed = False

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1
        self.gravity = 0.8
        self.jump_speed = -16
        self.avaliable_jump = True

        #player health
        self.contador_hp = 3
        self.invencible = False
        self.invincibility_duration = 750
        self.hurt_time = 0

    def animation_player(self):
        self.player_index += self.animation_speed
        if self.player_index > 10:
            self.player_index = 0
        if self.status == 'idle':
            if not self.direita:
                self.image = player_animacao_idle[int(self.player_index)]
            else:
                self.image = pygame.transform.flip(player_animacao_idle[int(self.player_index)], True, False)
        elif self.status == 'walk':
            if not self.direita:
                self.image = player_animacao_walk[int(self.player_index)]
            else:
                self.image = pygame.transform.flip(player_animacao_walk[int(self.player_index)], True, False)
        elif self.status == 'run':
            if not self.direita:
                self.image = player_animacao_run[int(self.player_index)]
            else:
                self.image = pygame.transform.flip(player_animacao_run[int(self.player_index)], True, False)
        elif self.status == 'jump':
            if not self.direita:
                self.image = player_animacao_jump[int(self.player_index)]
            else:
                self.image = pygame.transform.flip(player_animacao_jump[int(self.player_index)], True, False)
        elif self.status == 'fall':
            if not self.direita:
                self.image = player_animacao_jump[int(self.player_index)]
            else:
                self.image = pygame.transform.flip(player_animacao_jump[int(self.player_index)], True, False)

        if not self.invencible:
            self.image.set_alpha(255)
        else:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >=0:
            return 255
        else:
             return 0

    def invincibility_timer(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.hurt_time >= self.invincibility_duration:
            self.invencible = False

    def get_status(self):
        if self.direction.y < 0 :
            self.status = 'jump'
        elif self.direction.y > 1 :
            self.status = 'fall'
            self.avaliable_jump = False
        else:
            if not self.boost_speed:
                if self.direction.x != 0:
                    self.status = 'walk'
                else:
                    self.status = 'idle'
            else:
                if self.direction.x != 0:
                    self.status = 'run'
                else:
                    self.status = 'idle'

    def get_input(self):
        keys = pygame.key.get_pressed()
        if not self.boost_speed:
            if keys[pygame.K_RIGHT]:
                self.direita = True
                self.direction.x = 4
            elif keys[pygame.K_LEFT]:
                self.direita = False
                self.direction.x = -4
            else:
                self.direction.x = 0
        else:
            if keys[pygame.K_RIGHT]:
                self.direita = True
                self.direction.x = 6
            elif keys[pygame.K_LEFT]:
                self.direita = False
                self.direction.x = -6
            else:
                self.direction.x = 0

        if keys[pygame.K_UP]:
            if self.avaliable_jump:
                self.jump()
                self.avaliable_jump = False
                        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        
    def update(self):
        self.get_input()
        self.get_status()
        self.animation_player()
        self.invincibility_timer()