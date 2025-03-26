from dataclasses import dataclass

import pygame


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
            cos = coordinates[0] / coordinates[1]
            sin = coordinates[1] / coordinates[0]
            lx = self.speed * cos
            ly = self.speed * sin
            self.rect.x += lx
            self.rect.y += ly
            if self.health <= 0:
                live = False
    def display(self, screen):
        screen.blit(self.image, self.rect)
