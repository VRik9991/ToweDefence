import pygame
import math
from utils import DamageType


class Tower:
    def __init__(self, attack_speed: float, damage_type: DamageType, demage: int):
        self.attack_speed = attack_speed
        self.damage_type: DamageType = damage_type
        self.attack_damage = demage
        self.rect = None
        self.image = pygame.image.load("—Pngtree—stereo 2.5d building tower defense_4055247.png")
        self.range = 40
        self.cooldown = 0.2
        self.projectiles = []

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def place(self, x, y):
        self.rect = pygame.rect(x, y, 10, 10)
    def attack(self,monsters):
        count = []
        for monster in monsters:
            count.append(math.sqrt((monster.rect.center.x - self.rect.center.x)**2 + (monster.rect.center.y - self.rect.center.y)**2))
        self.projectiles.append(monsters[count.index(min(count))])
        return monsters[count.index(min(count))]



