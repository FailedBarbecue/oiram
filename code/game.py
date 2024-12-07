import pygame
from code.menu import Menu
from code.level import Level
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Game:

  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Oiram")   
    self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) 
  
                    
  def run(self):
    while True:
      menu = Menu(self.window)
      menu_return = menu.run()
      
      if menu_return == MENU_OPTION[0]:
        level = Level(self.window, "Level1", menu_return)
      elif menu_return == MENU_OPTION[2]:
         pygame.quit()
         quit()
      else:
        pass
    

        
                          

