import pygame
import math


class Projectile:
    def __init__(self, x, y, target, damage, speed):
        self.image = pygame.image.load('fireball.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.target = target
        self.damage = damage
        self.speed = speed
        self.hit = False

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, target):
        if not self.hit:
            a = abs(self.rect.x - target.rect.x)
            b = abs(self.rect.y - target.rect.y)
            c = math.hypot(a, b)
            if c > self.speed:
                cos = a / c
                sin = b / c
                lx = self.speed * cos
                ly = self.speed * sin
                self.rect.x += lx
                self.rect.y += ly
            else:
                self.hit = True
                target.hp -= self.damage