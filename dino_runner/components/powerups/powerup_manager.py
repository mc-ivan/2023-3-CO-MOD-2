import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.utils.constants import SHIELD_TYPE

class PowerupManager:
    def __init__(self):
        self.powerups = []
        self.duration = random.randint(3, 5)
        self.appears_when = random.randint(50, 70) # score entre 50 y 70

    def update(self, game):
        # Controlamos las apariciones del powerup
        if len(self.powerups) == 0 and self.appears_when == game.score.count:
            self.generate_powerup()

        # Llamamos a la animacion del powerup
        for powerup in self.powerups:
            powerup.update(game.game_speed, self.powerups)
            # Si el dino colisiona con el powerup, el powerup desaparece
            if game.player.dino_rect.colliderect(powerup.rect):
                self.powerups.remove(powerup)
                powerup.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = SHIELD_TYPE
                game.player.power_up_time = powerup.start_time + (self.duration * 1000)

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)

    def reset_powerups(self, game):
        self.powerups = []
        self.appears_when = random.randint(50, 70) # score entre 50 y 70

    def generate_powerup(self):
        self.appears_when = random.randint(200, 300)
        powerup = Shield()
        self.powerups.append(powerup)