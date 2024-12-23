import pygame.image
from code.Const import ENTITY_HEALTH
from abc import ABC, abstractmethod

class Entity(ABC):
  def __init__(self, name: str, position: tuple):
    self.name = name
    self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
    self.rect = self.surf.get_rect(left=position[0], top=position[1])
    self.health =  ENTITY_HEALTH[self.name]

  @abstractmethod
  def move(self,):
    pass