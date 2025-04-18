import pygame


class Base:
    def __init__(self, dot):
        self.max_hp = 100
        self.current_hp = 100
        self.is_alive = True
        self.damaged = False
        self.image = pygame.image.load('bases/base1.png')
        self.rect = self.image.get_rect(center=dot)

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def get_damage(self, damage):
        self.current_hp -= damage
        self.damaged = True
        if self.current_hp <= 0:
            self.is_alive = False

    def image_change(self):
        if self.current_hp > 50:
            self.image = pygame.image.load('bases/base1.png')
        if 50 >= self.current_hp > 0:
            self.image = pygame.image.load('bases/base2.png')
        if self.current_hp <= 0:
            self.image = pygame.image.load('bases/base3.png')
