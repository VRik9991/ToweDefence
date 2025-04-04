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
