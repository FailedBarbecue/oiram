import pygame
from code.entity import Entity
from code.const import WIN_WIDTH

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self,):
      if self.name == 'enemy1':
        self.rect.centerx -= 2
      else:
        self.rect.centerx += 2