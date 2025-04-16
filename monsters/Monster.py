import math

import pygame

from utils import DamageType


class Monster:
    def __init__(self, spawn, money_callback, damage_callback):
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
        self.cost = 1
        self.money_callback = money_callback
        self.damage = 1
        self.damage_callback = damage_callback

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

        if self.hp <= 0 or self.counter == 6:
            self.die()

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def die(self):
        if self.counter == 6:
            self.damage_callback(self.damage)
        self.is_alive = False
        self.money_callback(self.cost)
