import pygame
from pygame.sprite import Sprite

class Boss(Sprite):
    def __init__(self, ai_settings, screen):
        super(Boss, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        
        try:
            self.image = pygame.image.load('boss.png')
        except:
            print("Ошибка загрузки boss.png! Создаю заглушку.")
            self.image = pygame.Surface((80, 80))
            self.image.fill((255, 0, 0))  
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.health = 10
        self.speed = 2  
        
        self.direction = 1  
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False
    
    def update(self):
        self.x += (self.speed * self.direction)
        self.rect.x = self.x
        
        if self.check_edges():
            self.direction *= -1
            self.y += 30  
            self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)