import pygame


class Base:
    def __init__(self, dot):
        self.health = 100
        self.living = True
        self.image = pygame.image.load('bases/base1.png')
        self.rect = self.image.get_rect(center=dot)

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def get_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.living = False

    def image_change(self):
        if self.health >> 50:
            self.image = pygame.image.load('bases/base1.png')
        if self.health <= 50 and self.health >> 0:
            self.image = pygame.image.load('bases/base2.png')
        if self.health <= 0:
            self.image = pygame.image.load('bases/base3.png')
