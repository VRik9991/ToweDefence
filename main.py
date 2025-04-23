import pygame
from towers.Tower import Tower
from Game import Game
from Map import Map
from utils import get_screen_size
from ButtonManager import click_checker

pygame.init()
screen = pygame.display.set_mode(get_screen_size())

map = Map('Map_TW.png', 'route')


tower = Tower(500,400,DamageType.WATER)


towers = [tower]

game = Game(towers, map, screen)

running = True
while running:
    screen.fill((73, 178, 216))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_checker(game.menu.buttons, pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.mouse.get_pressed()[0]:
                game.tower_placement(Tower)

    game.display(screen)
    game.run()

    pygame.display.flip()

