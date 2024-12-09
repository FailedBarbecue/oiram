import pygame
from code.entity import Entity
from code.const import WIN_WIDTH, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image_right = pygame.image.load(f'./assets/{name}.png').convert_alpha()
        self.image_left = pygame.image.load(f'./assets/{name}_left.png').convert_alpha()
        self.surf = self.image_right
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 3
            if self.surf != self.image_right:  
                self.surf = self.image_right
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 3
            if self.surf != self.image_left:  
                self.surf = self.image_left
        pass
