import pygame
class Enemy(pygame.sprite.Sprite):
     def __init__(self,pos_x,pos_y):
        super().__init__()
        self.is_animating = False
        self.is_dead = False
        self.hp = 75
        self.idle = []
        self.idle_break = False
        self.left = True
        self.idle.append(pygame.image.load('enemy/e1.png'))
        self.idle.append(pygame.image.load('enemy/e2.png'))
        self.idle.append(pygame.image.load('enemy/e3.png'))
        self.idle.append(pygame.image.load('enemy/e4.png'))
        
        
        self.death_list = []
        self.death_list.append(pygame.image.load('enemy/d1.png'))
        self.death_list.append(pygame.image.load('enemy/d2.png'))
        self.death_list.append(pygame.image.load('enemy/d3.png'))
        
        
        self.current_idle = 0
        self.current_death_frame = 0
        
        self.image = self.idle[self.current_idle]
        self.image_d = self.death_list[self.current_death_frame]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        

     def animate(self):
         self.is_animating = True
        
     def update(self):
      self.death()
      if not self.idle_break:
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
         
      if self.is_dead == True:
         self.is_animating = False

         self.current_death_frame += 0.15
         if self.current_death_frame >= len(self.death_list):
                self.current_death_frame = len(self.death_list) - 1

         self.image_d = self.death_list[int(self.current_death_frame)]
         self.image = self.image_d
         if self.current_death_frame == len(self.death_list)-1:
            self.rect = pygame.Rect(0, 0, 0, 0)
      
     def death(self):
         if self.hp<=0:
            self.idle_break = True
            self.is_dead = True
            
     def stop(self):
         self.is_animating = False
         self.idle_break = True