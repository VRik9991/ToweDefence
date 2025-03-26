import pygame
import math
from utils import DamageType


class Tower:
    def __init__(self, attack_speed: float, damage_type: DamageType, damage: int,x,y):
        self.attack_speed = attack_speed
        self.damage_type: DamageType = damage_type
        self.attack_damage = damage
        self.image = pygame.image.load("towers/assets/tower_assets/small_tower.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.range = 40
        self.cooldown = 0.2
        self.projectiles = []

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def place(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)

    def attack(self, monsters):
        count = []
        for monster in monsters:
            count.append(math.sqrt(
                (monster.rect.x - self.rect.x) ** 2 + (monster.rect.y - self.rect.y) ** 2))
        count_smallest = count.index(min(count))
        self.projectiles.append(monsters[count_smallest])
        return monsters[count_smallest]
