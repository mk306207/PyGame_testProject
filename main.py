import pygame, sys
from player import Player
from enemy import Enemy
#--------------------------------------------------------------------------------------
pygame.init()
clock = pygame.time.Clock()
#--------------------------------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
background = pygame.image.load('background.png')

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME")
#--------------------------------------------------------------------------------------
moving_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player(10,330)
enemy1 = Enemy(600,340)
#enemy_hitbox = pygame.Rect()

moving_sprites.add(player)
enemies.add(enemy1)


print(f"Grupy {enemy1}: {enemy1.groups()}")  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    enemy1.animate()
    player.move()
    #player.death(enemies)
    player.update(enemies)
    enemy1.update()
    
    
    screen.blit(background,(0,0))
    for e in enemies:
        if player.is_attack:
            screen.blit(player.image_attack, player.rect)
        elif player.is_dying:
            screen.blit(player.image_death, player.rect)
        elif e.is_dead:
            screen.blit(e.image_d, e.rect)
        else:
            moving_sprites.draw(screen)
        screen.blit(e.image, e.rect)
    
    
    pygame.display.flip()
    clock.tick(60)