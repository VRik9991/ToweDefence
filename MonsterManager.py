from Monster import Monster


monster_mapping = {
    'Monster': Monster
}

class MonsterManager:
    def __init__(self, wave_path, spawn_point):
        self.delays_between_monsters = []
        self.monsters_waves = []
        self.delays_between_waves = []
        with open(wave_path,"r") as file:
            opener = file.readlines()
        for i in range(len(opener)):
            if "wave_delay " in opener[i]:
                self.delays_between_waves.append(int(opener[i].split(" ")[1].strip()))
            elif "delay " in opener[i]:
                self.delays_between_monsters.append(int(opener[i].split(" ")[1].strip()))
            else:
                one_wave_monsters = []
                for g in range(int(opener[i].split(" x")[1].strip())):
                    one_wave_monsters.append(monster_mapping[opener[i].split(" x")[0]](spawn_point))
                self.monsters_waves.append(one_wave_monsters)

    def activist_of_all(self, screen):
        for i in range(len(self.monsters_waves)):
            for g in range(len(self.monsters_waves[i])):
                self.monsters_waves[i][g].display(screen)
    def killer(self):
        for i in range(len(self.monsters_waves)):
            for g in range(len(self.monsters_waves[i])):
                if self.monsters_waves[i][g].hp >= 0:
                    len(self.monsters_waves)

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