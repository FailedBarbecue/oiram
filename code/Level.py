import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY
from code.EntityMediator import EntityMediator
import random

class Level:
  
  def __init__(self, window, name, game_mode):
    self.window = window
    self.name = name
    self.game_mode = game_mode
    self.entity_list: list[Entity] = []
    self.player_list: list[Entity] = []
    self.entity_list.extend(EntityFactory.get_entity('parallax'))
    self.entity_list.append(EntityFactory.get_entity('player1'))
    self.player_list.append(EntityFactory.get_entity('player1'))
    if game_mode in [MENU_OPTION[1]]:
      self.entity_list.append(EntityFactory.get_entity('player2'))
      self.player_list.append(EntityFactory.get_entity('player2'))

    pygame.time.set_timer(EVENT_ENEMY, 2000)
  def run(self):
    clock = pygame.time.Clock()
    while True:
      clock.tick(60)
      for ent in self.entity_list:
        if 'player' in ent.name: 
          ent.move()
          ent.attack()
          ent.update_attack()
        if 'enemy' in ent.name:
          ent.move()
          for player in self.player_list:
            ent.attack(player)
          
        self.window.blit(source=ent.surf, dest=ent.rect)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == EVENT_ENEMY:
          choice = random.choice(('enemy1','enemy2'))
          self.entity_list.append(EntityFactory.get_entity(choice))
      pygame.display.flip()

      #collisions
      EntityMediator.verify_collision(entity_list = self.entity_list)
      EntityMediator.verify_health(entity_list = self.entity_list)

      
      self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
      self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
      pygame.display.flip()
    

  def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
    self.window.blit(source=text_surf, dest=text_rect)