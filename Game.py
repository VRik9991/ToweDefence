import pygame

import utils
from towers.Tower import Tower
from utils import DamageType


class Game:
    def __init__(self, monsters, towers, map):
        self.monsters = monsters
        self.towers = towers
        self.map = map

    def display(self, screen):
        self.map.display(screen)
        for monster in self.monsters:
            monster.display(screen)
        for tower in self.towers:
            tower.display(screen)

    def run(self):
        for tower in self.towers:
            tower.attack(self.monsters)
        for monster in self.monsters:
            monster.move(self.map.route[monster.counter])
        self.monsters = [monster for monster in self.monsters if monster.is_alive]

    def tower_placement(self, item):
        is_it_collide = 0
        coordinates = pygame.mouse.get_pos()
        for place in self.map.placement_space:
            if place.collidepoint(coordinates):
                for tower in self.towers:
                    if item(coordinates[0],coordinates[1],DamageType.EARTH).rect.colliderect(tower.rect):
                        is_it_collide +=1
                if is_it_collide == 0:
                    self.towers.append(item(coordinates[0],coordinates[1],DamageType.EARTH))



