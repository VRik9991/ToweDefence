import pygame
from utils import get_screen_size


class Map:
    def __init__(self, image_path, route_path):
        self.map_size = get_screen_size()
        self.route = []
        self.placement_space = [
            pygame.Rect(0, 0, 310, 1075),
            pygame.Rect(327, 684, 705, 392),
            pygame.Rect(1037, 683, 90, 199),
            pygame.Rect(324,0,1596 , 171),
            pygame.Rect(1513, 518, 1000, 225)
        ]

        dots = open(route_path, 'r').readlines()
        for i in range(len(dots)):
            route_half_part = (dots[i].split(' '))
            route_part = ((int(route_half_part[0]) * self.map_size[0]) / 1920), (
                    (int(route_half_part[1]) * self.map_size[1]) / 1080)
            self.route.append(route_part)

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.image = pygame.transform.scale(pygame.image.load(image_path), self.map_size)

    def display(self, screen):
        screen.blit(self.image, self.rect)
