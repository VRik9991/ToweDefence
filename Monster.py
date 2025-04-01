from dataclasses import dataclass

import pygame


@dataclass
class MonsterResistances:
    air: float
    ground: float
    fire: float
    water: float

class Monster:
    def __init__(self, spawn):
        self.x = spawn[0]
        self.y = spawn[1]
        self.speed = 10
        self.live = True
        self.resistances = ["poop_attack", 50, "<- this is %"]
        self.image = "image"
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.health = 10
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
    def tank_improve(self):
        self.health *= 2
        self.speed *= 0.9
        self.resistances += 5