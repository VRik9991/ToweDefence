import math

import pygame

from utils import DamageType


class Monster:
    def __init__(self, spawn):
        self.speed = 3
        self.is_alive = True
        self.resistances = {
            DamageType.EARTH: 0,
            DamageType.WATER: 0,
            DamageType.AIR: 0,
            DamageType.FIRE: 0
        }
        self.image = pygame.image.load('monsters/assets/monster.png')
        self.rect = self.image.get_rect(center=spawn)
        self.hp = 10
        self.counter = 0

    def move(self, coordinates):
        dx = coordinates[0] - self.rect.x
        dy = coordinates[1] - self.rect.y
        distance = math.hypot(dx, dy)

        if distance > self.speed:

            self.rect.x += self.speed * (dx / distance)
            self.rect.y += self.speed * (dy / distance)
        else:

            self.rect.x = coordinates[0]
            self.rect.y = coordinates[1]
            self.counter += 1

        if self.counter == 6:
            self.is_alive = False

        if self.hp <= 0:
            self.is_alive = False

    def display(self, screen):
        screen.blit(self.image, self.rect)
