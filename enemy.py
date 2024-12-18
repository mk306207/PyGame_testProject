import pygame
class Enemy(pygame.sprite.Sprite):
     def __init__(self,pos_x,pos_y):
        self.is_animating = False
        self.hp = 75
        self.idle = []
        self.left = True
        self.idle.append(pygame.image.load('enemy/e1.png'))
        self.idle.append(pygame.image.load('enemy/e2.png'))
        self.idle.append(pygame.image.load('enemy/e3.png'))
        self.idle.append(pygame.image.load('enemy/e4.png'))
        
        self.current_idle = 0
        self.image = self.idle[self.current_idle]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        

     def animate(self):
         self.is_animating = True
        
     def update(self):
      if self.is_animating == True:
            if self.left:
               self.rect.x -= 2
               self.current_idle += 0.1
            if not self.left:
               self.rect.x += 2
               self.current_idle += 0.1          
      if self.current_idle >= len(self.idle):
         self.current_idle = 0
         self.is_animating = False
      if(self.rect.x == 0):
            self.left = False
      if self.rect.x == 800:
         self.left = True
      self.image = self.idle[int(self.current_idle)]