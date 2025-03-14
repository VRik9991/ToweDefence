import pygame
from map import Map
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
x_length_of_screen = user32.GetSystemMetrics(0)
y_length_of_screen = user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((x_length_of_screen, y_length_of_screen))

map_image = pygame.image.load('images/Map_TW.png')
mon_image = pygame.image.load('images/mon.png')


play_map = Map(map_image, ((1200, 880), (1200, 600), (400, 600), (400, 250), (1650, 250), (1650, 470)))
route = play_map.route_returner()

monsters = []

running = True
clock = pygame.time.Clock()
timer = 150

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    play_map.display(screen)

    pygame.display.flip()
    clock.tick(timer)

'''pygame.mouse.get_pos()'''