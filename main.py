from Game import Game
from Monster import Monster
from towers.Tower import Tower
from towers import Projectile


import pygame
from Map import Map
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
x_length_of_screen = user32.GetSystemMetrics(0)
y_length_of_screen = user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((x_length_of_screen, y_length_of_screen))

map_image = pygame.image.load('towers/assets/map_assets/Map_TW.png')
route = []


with open('maps', 'r') as file:
    opener = file.readlines()


play_map = Map(map_image, opener)
m = Monster(10,[1200, 880],563837102,pygame.image.load("towers/assets/monster_assets/monstere.jpg"))
t = Tower(10,"air",20)
g = Game([m],[t],play_map)
running = True
clock = pygame.time.Clock()
timer = 150

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    g.display(screen)
    g.run()


    pygame.display.flip()
    clock.tick(timer)
