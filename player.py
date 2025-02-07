import pygame
class Player(pygame.sprite.Sprite):
     def __init__(self,pos_x,pos_y):
          super().__init__()

          self.walk = []
          self.hp = 100
          self.exp = 0
          self.lvl = 0
          
          self.start_x = pos_x
          self.start_y = pos_y
          
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


     def death(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect) and not self.is_attack:
                self.is_dying = True
                print("ha ha ha")
                self.rect.topleft = [self.start_x, self.start_y]
                self.hp = 100 
                break 
            
            
     def attack_func(self, enemies):
        for e in enemies.copy():  # Używamy kopii, aby nie modyfikować listy w trakcie iteracji
            if self.rect.colliderect(e.rect):
                print("hit!")
                e.hp -= 10
                if e.hp <= 0:
                    print("dead!")
                    set(enemies)
                    print(f"usuwam {e}")
                    e.kill()  # Usunięcie TYLKO tego przeciwnika
                    print(f"Enemies in group: {len(enemies)}")

                     
                     
                     
     def update(self,enemies):
        if self.rect.x < 0 or self.rect.x > 800 or self.rect.y < 0 or self.rect.y > 600:
    # Może ustaw pozycję gracza na domyślną, jeśli jest poza ekranem
            self.rect.topleft = [self.start_x,self.start_y]
        self.attack_func(enemies)
        self.death(enemies)
        if self.hp <= 0:  # Jeśli gracz ma 0 zdrowia, nie może się poruszać ani atakować
            self.is_dying = True
            self.current_death_frame += 0.15
            if self.current_death_frame >= len(self.death_animation):
                self.current_death_frame = len(self.death_animation) - 1
                #self.is_animating = True
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
                
        