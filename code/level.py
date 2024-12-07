import pygame
from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
  
  def __init__(self, window, name, menu_option):
    self.window = window
    self.name = name
    self.menu_option = menu_option
    self.entity_list: list[Entity] = []
    self.entity_list.extend(EntityFactory.get_entity('parallax'))

  def run(self):
    while True:
      for ent in self.entity_list:
        self.window.blit(source=ent.surf, dest=ent.rect)
      pygame.display.flip()
    pass