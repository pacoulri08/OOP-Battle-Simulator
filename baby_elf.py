from enemy import Enemy

class Baby_Elf(Enemy):
    #new ability
    def cry():
        print("waaaaaaaaaaaaaaaaaahhhhhhhh")

    #override take damage
    def take_damage(self, damage):
        print("you hit a baby dawg what the freak")
        return super().take_damage(damage)