from MonsterManager import MonsterManager


class Game:
    def __init__(self, towers, map_object, screen):
        self.monster_manager = MonsterManager('map1_monsters', map_object.route[0], screen, self.money_callback)
        self.towers = towers
        self.map = map_object
        self.money = 0

    def money_callback(self, money_amount):
        self.money += money_amount

    def display(self, screen):
        self.map.display(screen)
        self.monster_manager.display_all_spawned_monsters()
        for tower in self.towers:
            tower.display(screen)

    def run(self):
        self.monster_manager.run()
        for tower in self.towers:
            tower.attack(self.monster_manager.monsters_on_screen)
        self.monster_manager.move_all_spawned_monsters(self.map.route)


