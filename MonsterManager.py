from Monster import Monster
from Map import Map
import time


class MonsterManager:
    def __init__(self, wave_path, spawn_point, screen):
        self.monster_mapping = {
            'Monster': Monster}
        self.screen = screen
        self.time_before = time.time()
        self.delays_between_monsters = []
        self.monsters_waves = []
        self.delays_between_waves = [1]
        self.monsters_on_screen = []
        with open(wave_path, "r") as file:
            opener = file.readlines()
        print(opener)
        for i in range(len(opener)):
            if "wave_delay " in opener[i]:
                self.delays_between_waves.append(float(opener[i].split(" ")[1].strip()))
            elif "delay " in opener[i]:
                self.delays_between_monsters.append(float(opener[i].split(" ")[1].strip()))
            else:
                one_wave_monsters = []
                for g in range(int(opener[i].split(" x")[1].strip())):
                    one_wave_monsters.append(self.monster_mapping[opener[i].split(" x")[0]](spawn_point))
                self.monsters_waves.append(one_wave_monsters)
        self.delay_now = self.delays_between_monsters[0]

    def should_spawn(self, spawn, money):
        time_now = time.time()
        if len(self.monsters_waves) != 0:
            if time_now - self.time_before >= self.delay_now:
                self.time_before = time.time()
                self.delay_now = self.delays_between_monsters
                self.monsters_on_screen.append(self.monsters_waves[0][0])
                self.monsters_waves[0].pop(0)
                if len(self.monsters_waves[0]) == 0:
                    self.monsters_waves.pop(0)
                    self.delays_between_monsters.pop(0)
                    money += 10
                    self.delay_now = self.delays_between_waves[0]
                    self.delays_between_waves.pop(0)
                    return money

    def move_all_spawned_monsters(self, route):
        for i in range(len(self.monsters_on_screen)):
            self.monsters_on_screen[i].move(route[self.monsters_on_screen[i].counter])

    def display_all_spawned_monsters(self):
        for i in range(len(self.monsters_on_screen)):
            self.monsters_on_screen[i].display(self.screen)

    def killer(self, money):
        for i in range(len(self.monsters_on_screen)):
            if self.monsters_on_screen[i].hp <= 0:
                self.monsters_on_screen.pop(i)
                len(self.monsters_waves)
                money += 1
                return money



MonsterManager('map1_monsters', (0, 0))
'''add = lambda x, y: x + y
sub = lambda x, y: x - y
actions = {
    'add': add,
    'sub': sub
}
a = 15
b = 7
for i in range(10):
    a = actions['add'](a, b)
    print(a)'''
