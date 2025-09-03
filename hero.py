import random

chance = random.randint(60, 75)
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.attack_power = random.randint(15, 20)
        self.special_ability = chance

    def strike(self):
        if random.randint(1, 10) > 1:
            return random.randint(1, self.attack_power)
        else:
            return random.randint(35, self.special_ability)
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    #TODO define is_alive
    def is_alive(self):
        return self.health > 0
