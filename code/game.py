import pygame
from code.menu import Menu

class Game:

  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Oiram")   
    screen = pygame.display.set_mode((1450, 900)) 
    self.window = screen
    clock = pygame.time.Clock()  
    background = pygame.image.load("assets/backgrounds/dawn.png")
    screen.blit(background, (0, 0))  
    pygame.display.flip()           
    clock.tick(144)  
                    
  
  def run(self):
    running = True
    while running:
      menu = Menu(self.window)
      menu.run()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        
                          

