from MonsterManager import MonsterManager
from Gold import Golda
from utils import get_screen_size
from towers.TowersButton.TowersButton import TowersButton
from TowerMenu import TowerMenu
from towers.Tower import Tower


class Game:
    def __init__(self, towers, map_object, screen):
        self.monster_manager = MonsterManager('map1_route', map_object.route[0], screen, self.money_callback)
        self.towers = towers
        self.map = map_object
        self.money = 0
        self.gold = Golda()
        self.screen = screen
        self.menu = TowerMenu([TowersButton(Tower.image, Tower.price, (80, 80), Tower.__name__, self.tower_button_callback), TowersButton(Tower.image, Tower.price, (80, 80), Tower.__name__, self.tower_button_callback)], [10, get_screen_size()[1] - 10 - 120, 510, 120])

    def money_callback(self, money_amount):
        self.money += money_amount

    def tower_button_callback(self, tower_name):
        self.menu.chosen_tower = tower_name

    def display(self, screen):
        self.map.display(screen)
        self.monster_manager.display_all_spawned_monsters()
        for tower in self.towers:
            tower.display(screen)
        self.gold.display(self.money, screen)
        self.menu.display(screen)

    def run(self):
        self.monster_manager.run()
        for tower in self.towers:
            tower.attack(self.monster_manager.monsters_on_screen)
        self.monster_manager.move_all_spawned_monsters(self.map.route)
