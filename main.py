import pygame
from towers.Tower import Tower
from Game import Game
from Map import Map
from utils import get_screen_size

pygame.init()
screen = pygame.display.set_mode(get_screen_size())

map = Map('Map_TW.png', 'route')

tower = Tower()

towers = [tower]

game = Game(towers, map, screen)

running = True
while running:

    screen.fill((73, 178, 216))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.display(screen)
    running = game.run()

    pygame.display.flip()
