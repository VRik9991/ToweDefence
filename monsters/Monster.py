import math
import random
import pygame

from utils import DamageType


class Monster:
    def __init__(self, spawn):
        self.speed = 1
        self.hp = 10000
        self.counter = 0
        self.is_alive = True
        self.resistances = {
            DamageType.EARTH: 0,
            DamageType.WATER: 0,
            DamageType.AIR: 0,
            DamageType.FIRE: 0
        }
        self.nunber_of_image = random.randint(0, 1)
        self.regulator_images = 0
        self.images = [pygame.image.load("monsters\monster_types\monster.png"),
                      pygame.image.load('monsters\monster_types\monster2.png')
                      ]
        self.image = pygame.image.load('monsters\monster_types\monster.png')
        self.images_counter = 0
        self.spawn = spawn
        self.rect = self.image.get_rect(center=self.spawn)
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
        if self.hp <= 0:
            self.is_alive = False

    def display(self, screen):
        self.regulator_images += 0.1
        screen.blit(self.images[self.nunber_of_image], self.rect)
        if self.regulator_images >= 2:
            self.nunber_of_image = random.randint(0, 1)
            screen.blit(self.images[self.nunber_of_image], self.rect)
            self.regulator_images = 0