import pygame
# C
COLOR_WHITE = (255,255,255)
COLOR_RED = (139,0,0)
# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
  'player1': 100,
  'player2': 100,
  'enemy1': 100,
  'enemy2': 100,
  'parallax0': 999,
  'parallax1': 999,
  'parallax2': 999,
  'parallax3': 999,

}
# G 
GAME_NAME = 'Oiram'
# M
MENU_OPTION = ('NEW GAME - 1P',
              'COOP - 2P',
             'SCORE',
             'EXIT')
# P
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,
                    'player2': pygame.K_d}
PLAYER_KEY_LEFT ={'player1': pygame.K_LEFT,
                  'player2': pygame.K_a}
# W 
WIN_WIDTH = 1280
WIN_HEIGHT = 720

# T
TIMEOUT_LEVEL = 20000  # 20s