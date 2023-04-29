import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        

    def update(self, user_imput):
        # si el dino esta corriendo es True
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        
        # colocar en cero a step_index caundo es mayor a 10
        if self.step_index > 10:
            self.step_index = 0

        # Actulizar variable si el dino salta o corre basado en la entrada del teclado
        if user_imput[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        # En el eje y
        self.dino_rect.y -= self.jump_speed*4
        self.jump_speed -= 0.8
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED