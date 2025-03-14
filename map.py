import pygame

class Map:
    def __init__(self, image, route):
        self.route = route
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.image = image
    def display(self, screen):
        screen.blit(self.image, self.rect)
    def route_returner(self):
        return self.route