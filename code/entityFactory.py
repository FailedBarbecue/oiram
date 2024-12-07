from code.background import Background
from code.const import WIN_WIDTH

class EntityFactory:

  @staticmethod
  def get_entity(entity_name: str):
    match entity_name:
      case 'parallax':
        list_bg = []
        for i in range(4):
          list_bg.append(Background(f'parallax{i}', (0,0)))
          list_bg.append(Background(f'parallax{i}', (WIN_WIDTH,0)))
        return list_bg