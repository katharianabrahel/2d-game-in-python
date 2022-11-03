import pygame, sys
from support import uma_vida, duas_vidas, tres_vidas, coin, fonte
from player import Player
from tiles import Tile
from settings import tile_size, tela_dimensoes
from player import Player
from coins import Coin
from powerup import Boost, HP
from enemy import Enemy, Invi_wall

class Level:
    def __init__(self, level_data, surface):
        #level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.coin = pygame.sprite.Group()
        self.boost = pygame.sprite.GroupSingle()
        self.heart = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.invi_wall = pygame.sprite.Group()
        
        for linha_index, linha in enumerate(layout):
            for coluna_index, celula in enumerate(linha):
                x = coluna_index * tile_size
                y = linha_index * tile_size
                if celula == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if celula == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if celula == 'C':
                    coin_sprite = Coin((x,y))
                    self.coin.add(coin_sprite)
                if celula == 'B':
                    boost_sprite = Boost((x,y))
                    self.boost.add(boost_sprite)
                if celula == 'H':
                    heart_sprite = HP((x,y))
                    self.heart.add(heart_sprite)
                if celula == 'E':
                    enemy_sprite = Enemy((x,y))
                    self.enemy.add(enemy_sprite)
                if celula == 'W':
                    invi_wall_sprite = Invi_wall((x,y), tile_size)
                    self.invi_wall.add(invi_wall_sprite)

                    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if not player.boost_speed:
            if player_x < (tela_dimensoes[0] / 4) and direction_x < 0:
                self.world_shift = 4 
                player.speed = 0
            elif player_x > (tela_dimensoes[0] * 3/4) and direction_x > 0:
                self.world_shift = -4
                player.speed = 0
            else:
                self.world_shift = 0
                player.speed = 1
        else:
            if player_x < (tela_dimensoes[0] / 4) and direction_x < 0:
                self.world_shift = 6
                player.speed = 0
            elif player_x > (tela_dimensoes[0] * 3/4) and direction_x > 0:
                self.world_shift = -6
                player.speed = 0
            else:
                self.world_shift = 0
                player.speed = 1

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.avaliable_jump = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def enemy_move(self):
        for sprite_enemy in self.enemy:
            for sprite_invi in self.invi_wall:
                if sprite_enemy.rect.colliderect(sprite_invi.rect):
                    if sprite_enemy.esquerda:
                        sprite_enemy.esquerda = False
                    else:
                        sprite_enemy.esquerda = True
    
    def enemy_death(self):
        player = self.player.sprite
        for sprite in self.enemy:
            if sprite.rect.colliderect(player.rect):
                if sprite.rect.top < player.rect.bottom < sprite.rect.centery and player.status == 'fall':
                    player.direction.y = -10
                    sprite.esquerda = True
                    sprite.rect.x = -5000
                else:
                    if not player.invencible:
                        player.contador_hp -= 1
                        player.invencible = True
                        player.hurt_time = pygame.time.get_ticks()
                    
    def player_death(self):
        player = self.player.sprite
        if player.rect.y > 720:
            pygame.quit()
            sys.exit()
        if player.contador_hp == 0:
            pygame.quit()
            sys.exit()
                    
    def collect_coins(self):
        player = self.player.sprite
        for sprite in self.coin.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.rect.x = -5000
                player.contador_coins += 1
        
            
    def collect_powerup(self):
        player = self.player.sprite

        for sprite in self.boost.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.rect.x = -5000
                player.boost_speed = True
                
        
        for sprite in self.heart.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.rect.x = -5000
                if player.contador_hp < 3:
                   player.contador_hp += 1

    def display_health(self):
        player = self.player.sprite
        if player.contador_hp == 1:
            self.vida = uma_vida
        elif player.contador_hp == 2:
            self.vida = duas_vidas
        elif player.contador_hp == 3:
            self.vida = tres_vidas
        self.vida_rect = self.vida.get_rect(topleft = (30, 10))
        self.display_surface.blit(self.vida, self.vida_rect)

    def display_coins(self):
        player = self.player.sprite
        self.coin_display = coin[0]
        self.coin_display_rect = self.coin_display.get_rect(topleft = (10, 50))
        self.font = fonte
        self.amount_count = self.font.render(str(player.contador_coins), False, (255, 255, 255))
        self.amount_count_rect = self.amount_count.get_rect(midleft = (self.coin_display_rect.right, self.coin_display_rect.centery + 1))
        self.display_surface.blit(self.coin_display, self.coin_display_rect)
        self.display_surface.blit(self.amount_count, self.amount_count_rect)

    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.invi_wall.update(self.world_shift)
        self.invi_wall.draw(self.display_surface)
        self.scroll_x()
        
        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        #coletável
        self.coin.update(self.world_shift)
        self.coin.draw(self.display_surface)
        self.collect_coins()

        #powerups
        self.boost.update(self.world_shift)
        self.boost.draw(self.display_surface)
        self.heart.update(self.world_shift)
        self.heart.draw(self.display_surface)
        self.collect_powerup()

        #layout
        self.enemy.update(self.world_shift)
        self.enemy.draw(self.display_surface)
        self.enemy_move()
        self.enemy_death()
        self.player_death()
        self.display_health()
        self.display_coins()
        
       