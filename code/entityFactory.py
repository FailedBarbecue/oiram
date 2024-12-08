from code.background import Background
from code.player import Player
from code.const import WIN_WIDTH

class EntityFactory:

  @staticmethod
  def get_entity(entity_name: str):
    match entity_name:
      case 'parallax':
        list_bg = []
        for i in range(4):
          list_bg.append(Background(f'parallax{i}', (0,0)))
        return list_bg
      case 'Player1':
        return Player('Player1', (10,200) )