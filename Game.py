from MonsterManager import MonsterManager
from Gold import Golda
from utils import get_screen_size
from towers.TowersButton.TowersButton import TowersButton
from TowerMenu import TowerMenu
from towers.Tower import Tower
from Base import Base
from Healthbar import Healthbar
from Map import Map


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.map = Map('Map_TW.png', 'route')
        self.tower = Tower()
        self.towers = [self.tower]
        self.base = Base(self.map.route[5])
        self.monster_manager = MonsterManager('map1_route', self.map.route[0], self.screen, self.money_callback, self.base.get_damage)
        self.money = 0
        self.gold = Golda()
        self.menu = TowerMenu([TowersButton(Tower.image, Tower.price, (80, 80), Tower.__name__, self.tower_button_callback), TowersButton(Tower.image, Tower.price, (80, 80), Tower.__name__, self.tower_button_callback)], [10, get_screen_size()[1] - 10 - 120, 510, 120])
        self.healthbar = Healthbar()

    def money_callback(self, money_amount):
        self.money += money_amount

    def tower_button_callback(self, tower_name):
        self.menu.chosen_tower = tower_name

    def display(self):
        self.map.display(self.screen)
        self.base.display(self.screen)
        self.monster_manager.display_all_spawned_monsters()
        for tower in self.towers:
            tower.display(self.screen)
        for monster in self.monster_manager.monsters_on_screen:
            self.healthbar.healthbar_run(self.screen, monster)
        self.gold.display(self.money, self.screen)
        self.menu.display(self.screen)

    def go(self):
        self.monster_manager.run()
        for tower in self.towers:
            tower.attack(self.monster_manager.monsters_on_screen)
        self.monster_manager.move_all_spawned_monsters(self.map.route)
        self.base.image_change()

    def run(self):
        self.go()
        self.display()
