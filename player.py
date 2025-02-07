import pygame
class Player(pygame.sprite.Sprite):
     def __init__(self,pos_x,pos_y):
          super().__init__()

          self.walk = []
          self.hp = 100
          self.exp = 0
          self.lvl = 0
          
          self.is_animating = False
          self.walk.append(pygame.image.load('walk/1.png'))
          self.walk.append(pygame.image.load('walk/2.png'))
          self.walk.append(pygame.image.load('walk/3.png'))
          self.walk.append(pygame.image.load('walk/4.png'))
          self.walk.append(pygame.image.load('walk/5.png'))
          self.current_walk = 0
          self.image = self.walk[self.current_walk]
          self.image2 = pygame.transform.flip(self.walk[self.current_walk], True, False)
          self.is_walking = False

          self.rect = self.image.get_rect()
          self.rect.topleft = [pos_x,pos_y]

          self.flip = False

          self.attack = []
          self.attack.append(pygame.image.load('attack/f1.png'))
          self.attack.append(pygame.image.load('attack/f2.png'))
          self.attack.append(pygame.image.load('attack/f3.png'))
          self.attack.append(pygame.image.load('attack/f4.png'))
          self.attack.append(pygame.image.load('attack/f5.png'))
          self.attack.append(pygame.image.load('attack/f6.png'))
          self.current_attack = 0
          self.image_attack = self.attack[self.current_attack]
          self.is_attack = False
          
          self.attack_cooldown = 500
          self.last_attack_time = 0
          
          self.death_animation = []
          self.death_animation.append(pygame.image.load('death/d1.png'))
          self.death_animation.append(pygame.image.load('death/d2.png'))
          self.death_animation.append(pygame.image.load('death/d3.png'))
          self.death_animation.append(pygame.image.load('death/d4.png'))
          self.death_animation.append(pygame.image.load('death/d5.png'))
          self.current_death_frame = 0
          self.image_death = self.death_animation[self.current_death_frame]
          self.is_dying = False

     def update(self):
        if self.is_dying:
            self.is_animating = False
            self.current_death_frame += 0.15
            if self.current_death_frame >= len(self.death_animation):
                self.current_death_frame = len(self.death_animation) - 1
                self.is_animating = True
            self.image_death = self.death_animation[int(self.current_death_frame)]
        if self.is_animating == True and self.is_walking==True:
            self.current_walk += 0.15
            self.current_attack = 0
        if self.current_walk >= len(self.walk):
            self.current_walk = 0
            self.is_animating = False
        self.image = self.walk[int(self.current_walk)]
        if self.flip == True:
             self.image = pygame.transform.flip(self.walk[int(self.current_walk)],True, False)
        if self.is_attack==True and self.is_animating==True:
            self.current_attack += 0.13
            self.current_walk = 0
        if self.current_attack >= len(self.attack):
            self.current_attack = 0
            self.is_attack = False
            self.is_animating = False
        self.image_attack = self.attack[int(self.current_attack)]
        if self.flip == True:
            self.image_attack = pygame.transform.flip(self.attack[int(self.current_attack)],True,False)

     def animate(self):
         self.is_animating = True

     def move(self):
            if self.is_dying:
                return
            key=pygame.key.get_pressed()
            if key[pygame.K_a]==True:
                self.flip = True
                self.is_attack = False
                self.is_walking = True
                self.animate()
                self.rect.x -= 2
            elif key[pygame.K_d]==True:
                self.flip = False
                self.is_attack = False
                self.is_walking = True
                self.animate()
                self.rect.x += 2
            elif key[pygame.K_c]==True:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_attack_time > self.attack_cooldown:
                    self.is_attack = True
                    self.last_attack_time = current_time
                    self.is_walking = False
                    self.animate()
                #self.rect.move_ip(0,0)
                 
     def death(self,enemy):
        if self.rect.colliderect(enemy.rect):
            self.is_dying = True
            
