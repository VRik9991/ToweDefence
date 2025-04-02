import math

import pygame
from monsters.Monster import Monster
from utils import DamageType


class Flying(Monster):
    def __init__(self, spawn):
        super().__init__(spawn)
        self.speed = 5
        self.is_alive = True
        self.resistances = {
            DamageType.EARTH: 0,
            DamageType.WATER: 0,
            DamageType.AIR: 1,
            DamageType.FIRE: -1
        }
        self.image = pygame.image.load('monsters/assets/monster.png')
        self.rect = self.image.get_rect(center=spawn)
        self.hp = 6
        self.counter = 0