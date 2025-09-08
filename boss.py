from enemy import Enemy
import random


class George_Washington(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.health = 250
        self.attack_power = random.randint(15, 20)
    def strike(self):
        if random.randint(1, 100) < 95:
            return random.randint(1, self.attack_power)
        else:
            print("Ult")
            return random.randint(75, 125)
    