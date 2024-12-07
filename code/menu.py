import pygame

from code.const import WIN_WIDTH, COLOR_WHITE, COLOR_RED, GAME_NAME, MENU_OPTION

class Menu:

  def __init__(self, window):
    self.window = window
    self.surf = pygame.image.load("assets/menu.jpg")
   


  def run(self,):
  # LOAD MENU MUSIC
  #  pygame.mixer_music.load('./assets/menu.mp3')
  #  pygame.mixer_music.play(-1)

   menu_option = 0
   while True: 

  # DRAW IMAGE AND MENU TEXT
    self.window.blit(self.surf, (0, 0)) 
    self.menu_text(80, GAME_NAME, COLOR_WHITE, ((WIN_WIDTH / 2), 100))
    for i in range(len(MENU_OPTION)):
      if i == menu_option:
        self.menu_text(50, MENU_OPTION[i], COLOR_RED, ((WIN_WIDTH / 2), 300 + 40 * i))
      else:
        self.menu_text(50, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 300 + 40 * i))
    pygame.display.flip()   
    
  # EVENT CHECKS
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
           if menu_option < len(MENU_OPTION) - 1:
              menu_option += 1
           else: 
              menu_option = 0
        if event.key == pygame.K_UP:
           if menu_option > 0:
              menu_option -= 1
           else: 
              menu_option = len(MENU_OPTION) - 1
        if event.key == pygame.K_RETURN:
          return MENU_OPTION[menu_option]


  def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    self.window.blit(source=text_surf, dest=text_rect)