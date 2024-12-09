import pygame
from code.Entity import Entity
from code.Const import WIN_WIDTH, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_ATTACK

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image_right = pygame.image.load(f'./assets/{name}.png').convert_alpha()
        self.image_left = pygame.image.load(f'./assets/{name}_left.png').convert_alpha()
        self.attack_images = [ 
            pygame.image.load(f'./assets/{name}_attack1.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack2.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack3.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack4.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack5.png').convert_alpha(),
        ]
        self.attack_images_left = [
            pygame.image.load(f'./assets/{name}_attack1_left.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack2_left.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack3_left.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack4_left.png').convert_alpha(),
            pygame.image.load(f'./assets/{name}_attack5_left.png').convert_alpha(),
        ]
        self.direction = 'right'
        self.is_attacking = False  
        self.attack_frame = 0  # 
        self.attack_timer = 0
        self.surf = self.image_right
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 3
            if self.direction != 'right':  
                self.direction = 'right' 
                self.surf = self.image_right
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= 3
            if self.direction != 'left':  # Atualiza a direção
                self.direction = 'left'
                self.surf = self.image_left
        pass

    def attack(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_ATTACK[self.name]] and not self.is_attacking:
            self.is_attacking = True
            self.attack_frame = 0 

    def update_attack(self):
        if self.is_attacking:
            self.attack_timer += 1  # Incrementa o temporizador

            # Troca de imagem a cada 5 ticks (ajuste conforme necessário)
            if self.attack_timer % 5 == 0:
                if self.direction == 'right':
                    self.surf = self.attack_images[self.attack_frame]
                else:
                    self.surf = self.attack_images_left[self.attack_frame]
                self.attack_frame += 1  # Avança para o próximo frame

                # Finaliza o ataque se a sequência de imagens terminar
                if self.attack_frame >= len(self.attack_images):
                    self.is_attacking = False
                    self.attack_timer = 0
                    self.surf = pygame.image.load(f'./assets/{self.name}.png').convert_alpha()
