import pygame
from map import Map
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
x_length_of_screen = user32.GetSystemMetrics(0)
y_length_of_screen = user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((x_length_of_screen, y_length_of_screen))

map_image = pygame.image.load('images/Map_TW.png')
route = []


with open('maps', 'r') as file:
    Opener = file.readlines()

for i in range(len(Opener)):
    route_part = (int((Opener[i].split(' '))[0]), int((Opener[i].split(' '))[1]))
    route.append(route_part)
print(route)
play_map = Map(map_image, route)

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