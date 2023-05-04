from dino_runner.components.powerups.powerup import Powerup
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(Powerup):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)