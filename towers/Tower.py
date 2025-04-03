import pygame
import math

from towers.Projectile import Projectile
from utils import DamageType


class Tower:
    def __init__(self, spawn: tuple[int, int]):
        self.damage_type: DamageType.EARTH
        self.attack_damage = 1
        self.projectile_speed = 4
        self.image = pygame.image.load("towers/assets/tower_assets/tower.png")
        self.rect = self.image.get_rect(center=spawn)
        self.range = 300
        self.cooldown = 0.2
        self.projectiles = []

    def display(self, screen):
        screen.blit(self.image, self.rect)
        for projectile in self.projectiles:
            projectile.display(screen)

    def place(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)

    def attack(self, monsters):
        count = []
        for monster in monsters:
            count.append(math.hypot(abs(monster.rect.x - self.rect.x), abs(monster.rect.y - self.rect.y)))
        if monsters:
            count_smallest = count.index(min(count))
            self.projectiles.append(Projectile(self.rect.centerx, self.rect.centery, monsters[count_smallest], self.attack_damage, self.projectile_speed))
        self.projectiles = [projectile for projectile in self.projectiles if not projectile.hit]
        for projectile in self.projectiles:
            projectile.move()
