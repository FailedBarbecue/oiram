import pygame
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION

class Level:
  
  def __init__(self, window, name, game_mode):
    self.window = window
    self.name = name
    self.game_mode = game_mode
    self.entity_list: list[Entity] = []
    self.entity_list.extend(EntityFactory.get_entity('parallax'))
    self.entity_list.append(EntityFactory.get_entity('player1'))
    if game_mode in [MENU_OPTION[1]]:
      self.entity_list.append(EntityFactory.get_entity('player2'))
  def run(self):
    clock = pygame.time.Clock()
    while True:
      clock.tick(60)
      for ent in self.entity_list:
        if 'player' in ent.name:
          ent.move()
        self.window.blit(source=ent.surf, dest=ent.rect)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
      pygame.display.flip()
        # printed text
      self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
      self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
      pygame.display.flip()
    

  def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
    self.window.blit(source=text_surf, dest=text_rect)