import pygame
from Game import Game
from utils import get_screen_size
from ButtonManager import click_checker
pygame.init()
screen = pygame.display.set_mode(get_screen_size())


game = Game(screen)


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
                game.tower_placement(game.tower)

    game.run()

    pygame.display.flip()

