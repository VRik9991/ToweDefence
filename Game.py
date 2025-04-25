
import pygame
from utils import DamageType
from MonsterManager import MonsterManager
from Gold import Golda
from utils import get_screen_size
from towers.TowersButton.TowersButton import TowersButton
from TowerMenu import TowerMenu
from towers.Tower import Tower
from Base import Base
from Healthbar import Healthbar


class Game:
    def __init__(self, towers, map_object, screen):
        self.base = Base(map_object.route[5])
        self.monster_manager = MonsterManager('map1_route', map_object.route[0], screen, self.money_callback, self.base.get_damage)
        self.towers = towers
        self.map = map_object
        self.money = 0
        self.gold = Golda()
        self.screen = screen
        self.menu = TowerMenu([TowersButton(Tower.image, Tower.price, (80, 80), Tower.__name__, self.tower_button_callback), TowersButton(Tower.image, Tower.price, (80, 80), Tower.__name__, self.tower_button_callback)], [10, get_screen_size()[1] - 10 - 120, 510, 120])
        self.healthbar = Healthbar()

    def money_callback(self, money_amount):
        self.money += money_amount

    def tower_button_callback(self, tower_name):
        self.menu.chosen_tower = tower_name

    def display(self, screen):
        self.map.display(screen)
        self.base.display(screen)
        self.monster_manager.display_all_spawned_monsters()
        for monster in self.monster_manager.monsters_on_screen:
            self.healthbar.healthbar_run(screen, monster)
        for tower in self.towers:
            tower.display(screen)
        self.gold.display(self.money, screen)
        self.menu.display(screen)

    def run(self):
        self.monster_manager.run()
        for tower in self.towers:
            # tower.attack(self.monsters)
            tower.attack(self.monster_manager.monsters_on_screen)
        # for monster in self.monsters:
        #     monster.move(self.map.route[monster.counter])
                    
        self.monster_manager.move_all_spawned_monsters(self.map.route)
        # self.monsters = [monster for monster in self.monsters if monster.is_alive]

        self.base.image_change()
        if not self.base.is_alive:
            return False

    def tower_placement(self, item):
        if item != None:
            is_it_collide = 0
            coordinates = pygame.mouse.get_pos()
            for place in self.map.placement_space:
                if place.collidepoint(coordinates):
                    for tower in self.towers:
                        if item(coordinates[0],coordinates[1],DamageType.EARTH).rect.colliderect(tower.rect):
                            is_it_collide +=1
                    if is_it_collide == 0:
                        self.towers.append(item(coordinates[0],coordinates[1],DamageType.EARTH))


