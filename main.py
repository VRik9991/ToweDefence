import pygame
from towers.Tower import Tower
from monsters.Monster import Monster
from Game import Game
from Map import Map
from monsters.Monster import MonsterResistances
from utils import DamageType
pygame.init()
a = 0
screen = pygame.display.set_mode((1800, 600))

monsterresistances = MonsterResistances(0,0,0,0)

map = Map('Map_TW.png','route')

monster = Monster(1,map.route[0],10,'monsters/assets/monster.png',monsterresistances)

tower = Tower(1,DamageType.EARTH, 2,500,400)

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