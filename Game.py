from MonsterManager import MonsterManager
from Base import Base
from Healthbar import Healthbar


class Game:
    def __init__(self, towers, map_object, screen):
        self.base = Base(map_object.route[5])
        self.monster_manager = MonsterManager('map1_route',map_object.route[0],screen,self.money_callback,self.base.get_damage)
        self.towers = towers
        self.map = map_object
        self.money = 0
        self.user = 0
        self.healthbar = Healthbar()

    def money_callback(self, money_amount):
        self.money += money_amount

    def display(self, screen):
        self.map.display(screen)
        self.base.display(screen)
        self.monster_manager.display_all_spawned_monsters()
        for monster in self.monster_manager.monsters_on_screen:
            self.healthbar.healthbar_run(screen, monster)
        for tower in self.towers:
            tower.display(screen)

    def run(self):
        self.monster_manager.run()
        for tower in self.towers:
            tower.attack(self.monster_manager.monsters_on_screen)
        self.monster_manager.move_all_spawned_monsters(self.map.route)
        self.base.image_change()
        if not self.base.is_alive:
            return False
        return True
