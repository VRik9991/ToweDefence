from dataclasses import dataclass

import pygame
import math


@dataclass
class MonsterResistances:
    air: float
    ground: float
    fire: float
    water: float


class Monster:
    def __init__(self, speed, spawn, hp, image, resistances: MonsterResistances):
        self.x = spawn[0]
        self.y = spawn[1]
        self.speed = speed
        self.live = True
        self.resistances = resistances
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.health = hp
        self.counter = 0

    def move(self, coordinates):
        if self.live:

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

            if self.health <= 0:
                self.live = False

    def display(self, screen):
        screen.blit(pygame.image.load(self.image), self.rect)
