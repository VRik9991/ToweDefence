import pygame
from towers.Tower import Tower
from monsters.Monster import Monster
from Game import Game
from Map import Map
from utils import DamageType,get_screen_size
pygame.init()
screen = pygame.display.set_mode(get_screen_size())

map = Map('Map_TW.png','route')

monster = Monster(map.route[0])

tower = Tower((500,400))

towers = [tower]
monsters = [monster]

game = Game(monsters,towers,map)

running = True
while running:

    screen.fill((73, 178, 216))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.display(screen)
    game.run()

    pygame.display.flip()