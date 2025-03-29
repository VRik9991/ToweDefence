import pygame
import math

from towers.Projectile import Projectile
from utils import DamageType

class Tower:
    def __init__(self, attack_speed: float, damage_type: DamageType, damage: int,x,y):
        self.attack_speed = attack_speed
        self.damage_type: DamageType = damage_type
        self.attack_damage = damage
        self.image = pygame.image.load("towers/assets/tower_assets/small_tower.png")
        self.rect = self.image.get_rect(center=(x, y))
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
            count.append(math.hypot(abs(monster.rect.x - self.rect.x),abs(monster.rect.y - self.rect.y)))
        count_smallest = count.index(min(count))
        self.projectiles.append(Projectile(*self.rect.center,monsters[count_smallest],4,1))
        self.projectiles = [projectile for projectile in self.projectiles if not projectile.hit]
        for projectile in self.projectiles:
            projectile.move()
