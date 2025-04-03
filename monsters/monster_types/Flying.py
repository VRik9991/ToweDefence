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

        self.image = pygame.image.load('monsters/assets/flying.png')
        self.rect = self.image.get_rect(center=spawn)
        self.hp = 6
        self.counter = 0

    def move(self, coordinates):
        dx = coordinates[0] - self.rect.x
        dy = (coordinates[1]-50) - self.rect.y
        distance = math.hypot(dx, dy)

        if distance > self.speed:

            self.rect.x += self.speed * (dx / distance)
            self.rect.y += self.speed * (dy / distance)
        else:

            self.rect.x = coordinates[0]
            self.rect.y = coordinates[1]-50
            self.counter += 1

        if self.counter == 6:
            self.is_alive = False

        if self.hp <= 0:
            self.is_alive = False

    def display(self, screen):
        screen.blit(self.image, self.rect)
