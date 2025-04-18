import math
import pygame
from monsters.Monster import Monster
from utils import DamageType


class FlyingMonster(Monster):
    def __init__(self, spawn, money_callback, damage_callback):
        super().__init__(spawn, money_callback, damage_callback)
        self.speed = 5
        self.resistances = {
            DamageType.EARTH: 0,
            DamageType.WATER: 0,
            DamageType.AIR: 1,
            DamageType.FIRE: -1
        }
        self.image = pygame.image.load('monsters/assets/flying.png')
        self.max_hp = 6
        self.current_hp = 6

    def move(self, coordinates):
        dx = coordinates[0] - self.rect.x
        dy = coordinates[1] - 50 - self.rect.y
        distance = math.hypot(dx, dy)

        if distance > self.speed:

            self.rect.x += self.speed * (dx / distance)
            self.rect.y += self.speed * (dy / distance)
        else:

            self.rect.x = coordinates[0]
            self.rect.y = coordinates[1] - 50
            self.counter += 1

        if self.current_hp <= 0 or self.counter == 6:
            self.die()
