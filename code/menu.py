import pygame

from code.const import WIN_WIDTH, COLOR_WHITE, GAME_NAME, MENU_OPTION

class Menu:

  def __init__(self, window):
    self.window = window
    self.surf = pygame.image.load("assets/menu/menu.jpg")
   


  def run(self,):
   pygame.mixer_music.load('./assets/menu/menu.mp3')
   pygame.mixer_music.play(-1)
   while True: 
    self.window.blit(self.surf, (0, 0)) 
    self.menu_text(80, GAME_NAME, COLOR_WHITE, ((WIN_WIDTH / 2), 100))

    for i in range(len(MENU_OPTION)):
      self.menu_text(50, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 300 + 40 * i))
    pygame.display.flip()   
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

  def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    self.window.blit(source=text_surf, dest=text_rect)