from code.entity import Entity
from code.enemy import Enemy
from code.const import WIN_WIDTH
class EntityMediator:
  @staticmethod
  def __verify_collision_window(ent: Entity):
    if isinstance(ent, Enemy):
      if ent.name == 'enemy1':
        if ent.rect.right < 0:
          ent.health = 0
      else:
        if ent.rect.right > WIN_WIDTH:
          ent.health = 0

  @staticmethod
  def verify_collision(entity_list: list[Entity]):
    for i in range(len(entity_list)):
      test_entity = entity_list[i]
      EntityMediator.__verify_collision_window(test_entity)

  @staticmethod
  def verify_health(entity_list: list[Entity]):
    for ent in entity_list:
      if ent.health <= 0:
        entity_list.remove(ent)