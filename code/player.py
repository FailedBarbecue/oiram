import pygame
from code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
    def update(self,):
        pass

    def move(self, keys):
        pass
