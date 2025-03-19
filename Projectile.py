import pygame
import time


class Projectile:
    def __init__(self, x, y, target, damage, speed):
        self.image = pygame.image.load('fireball.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.target = target
        self.damage = damage
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.speed
        self.rect.y += self.speed


class Test:
    def __init__(self):
        self.image = pygame.image.load('fireball.png')
        self.rect = self.image.get_rect(center=(400,350))

    def display(self, screen):
        screen.blit(self.image, self.rect)


test = Test()
projectile = Projectile(100, 100, test, 10, 1)

screen = pygame.display.set_mode((800, 800))
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    projectile.display(screen)
    projectile.move()

    test.display(screen)

    pygame.display.flip()
