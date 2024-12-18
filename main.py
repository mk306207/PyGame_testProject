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
player = Player(10,330)
enemy = Enemy(600,300)
#enemy_hitbox = pygame.Rect()
moving_sprites.add(player)
#moving_sprites.add(enemy)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    enemy.animate()
    player.move()
    player.death(enemy)
    player.update()
    enemy.update()
    
    screen.blit(background,(0,0))
    if player.is_attack:
        screen.blit(player.image_attack, player.rect)
    elif player.is_dying:
        screen.blit(player.image_death, player.rect)
    else:
        moving_sprites.draw(screen)
    screen.blit(enemy.image, enemy.rect)
    pygame.display.flip()
    clock.tick(60)