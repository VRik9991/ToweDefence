import pygame
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
x_length_of_screen = user32.GetSystemMetrics(0)
y_length_of_screen = user32.GetSystemMetrics(1)
map_size = (x_length_of_screen, y_length_of_screen)

class Map:
    def __init__(self, image_path, route_path):

        self.route = []
        for i in range(len(route_path)):
            route_halfpart = (route_path[i].split(' '))
            route_part = ((int(route_halfpart[0])*map_size[0])/1920), ((int(route_halfpart[1])*map_size[1])/1080)
            self.route.append(route_part)

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.image =  pygame.transform.scale(image_path, map_size)
    def display(self, screen):
        screen.blit(self.image, self.rect)

