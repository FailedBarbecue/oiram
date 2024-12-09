from code.background import Background
from code.player import Player
from code.enemy import Enemy
from code.const import WIN_WIDTH
import random 
class EntityFactory:

  @staticmethod
  def get_entity(entity_name: str):
    match entity_name:
      case 'parallax':
        list_bg = []
        for i in range(4):
          list_bg.append(Background(f'parallax{i}', (0,0)))
        return list_bg
      case 'player1':
        return Player('player1', (10,260))
      case 'player2':
        return Player('player2', (100,260))
      case 'enemy1':
        return Enemy('enemy1', (WIN_WIDTH + 10, 290))
      case 'enemy2':
        return Enemy('enemy2', (-10, 290))