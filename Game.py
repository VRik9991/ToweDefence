

class Game:
    def __init__(self,monsters,towers,map):
        self.monsters=monsters
        self.towers=towers
        self.map = map
        self.route = self.map.route
    def display(self):
        for monster in self.monsters:
            monster.display()
        for tower in self.towers:
            tower.display()
        self.map.display()
    def run(self):
        for tower in self.towers:
            tower.attack()
        for monster in self.monsters:
            monster.move(self.route[monster.counter])


