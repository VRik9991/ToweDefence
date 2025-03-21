import pygame
import ctypes

class Map:
    def __init__(self, image_path, route_path):
        self.user32 = ctypes.windll.user32
        self.user32.SetProcessDPIAware()
        self.x_length_of_screen = self.user32.GetSystemMetrics(0)
        self.y_length_of_screen = self.user32.GetSystemMetrics(1)
        self.map_size = (self.x_length_of_screen, self.y_length_of_screen)
        self.route = []
        for i in range(len(route_path)):
            route_halfpart = (route_path[i].split(' '))
            route_part = ((int(route_halfpart[0])*self.map_size[0])/1920), ((int(route_halfpart[1])*self.map_size[1])/1080)
            self.route.append(route_part)

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.image =  pygame.transform.scale(image_path, self.map_size)
    def display(self, screen):
        screen.blit(self.image, self.rect)

