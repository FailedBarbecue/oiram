import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT

class Game:

  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Oiram")   
    self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) 
  
                    
  def run(self):
    while True:
      menu = Menu(self.window)
      menu.run()
      pass
    

        
                          

