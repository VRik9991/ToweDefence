import pygame
import math


class Projectile:
    def __init__(self, x, y, target, damage, speed):
        self.image = pygame.image.load('towers/assets/projectile_assets/fireball.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.target = target
        self.damage = damage
        self.speed = speed
        self.hit = False

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        if not self.hit:
            coordinates = self.target.rect.center
            dx = coordinates[0] - self.rect.x
            dy = coordinates[1] - self.rect.y
            distance = math.hypot(dx, dy)

            if distance > self.speed:

                self.rect.x += self.speed * (dx / distance)
                self.rect.y += self.speed * (dy / distance)

            else:
                self.hit = True
                self.target.hp -= self.damage