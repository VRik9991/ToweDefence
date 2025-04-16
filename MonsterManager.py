
from Map import Map
import time

from monsters.Monster import Monster


class MonsterManager:
    def __init__(self, wave_path, spawn_point, screen, money_callback,damage_callback):
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
        for i in range(len(opener)):
            if "wave_delay " in opener[i]:
                self.delays_between_waves.append(float(opener[i].split(" ")[1].strip()))
            elif "delay " in opener[i]:
                self.delays_between_monsters.append(float(opener[i].split(" ")[1].strip()))
            elif opener[i] != "\n":
                one_wave_monsters = []
                for g in range(int(opener[i].split(" x")[1].strip())):
                    one_wave_monsters.append(
                        self.monster_mapping[opener[i].split(" x")[0]](spawn_point, money_callback, damage_callback))
                self.monsters_waves.append(one_wave_monsters)
        self.delay_now = self.delays_between_monsters[0]

    def should_spawn(self):
        time_now = time.time()
        if len(self.monsters_waves) != 0:

            if time_now - self.time_before >= self.delay_now:
                self.time_before = time.time()
                self.delay_now = self.delays_between_monsters[0]
                self.monsters_on_screen.append(self.monsters_waves[0][0])
                self.monsters_waves[0].pop(0)
                if len(self.monsters_waves[0]) == 0:
                    self.monsters_waves.pop(0)
                    self.delays_between_monsters.pop(0)
                    self.delay_now = self.delays_between_waves[0]
                    self.delays_between_waves.pop(0)
    def run(self):
        self.should_spawn()
        self.killer()


    def move_all_spawned_monsters(self, route):
        for monster in self.monsters_on_screen:
            monster.move(route[monster.counter])

    def display_all_spawned_monsters(self):
        for monster in self.monsters_on_screen:
            monster.display(self.screen)

    def killer(self):
        self.monsters_on_screen = [monster for monster in self.monsters_on_screen if monster.is_alive]