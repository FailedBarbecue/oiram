import pygame
from code.entity import Entity
from code.const import WIN_WIDTH

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 3
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 3
        pass
