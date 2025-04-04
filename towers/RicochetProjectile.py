import pygame
import math
from towers.Projectile import Projectile


class RicochetProjectile(Projectile):
    def __init__(self, x, y, target, damage, speed):
        super().__init__(x, y, target, damage, speed)
        self.image = pygame.image.load('towers/assets/projectile_assets/fireball.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.target = target
        self.damage = damage
        self.speed = speed
        self.hit = False