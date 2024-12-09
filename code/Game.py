import pygame
from code.Menu import Menu
from code.Level import Level
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Game:

  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Oiram")   
    self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) 
  
                    
  def run(self):
    while True:
      menu = Menu(self.window)
      menu_return = menu.run()
      
      if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
        level = Level(self.window, "Level1", menu_return)
        Level.run(level)
      elif menu_return == MENU_OPTION[2]:
        # score.show()
        pass
      elif menu_return == MENU_OPTION[3]:
        pygame.quit()
        quit()
      else:
        pygame.quit()  
        quit() 
    

        
                          

