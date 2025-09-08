import random
from goblin import Goblin
from hero import Hero
from boss import George_Washington

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    rounds = 0

    hero_damage = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        hero_damage += damage
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
        print("But George Washington still remains...")
        president = George_Washington("George Washington")
        hero.health = 200  # Restore hero's health for the boss fight

        while hero.is_alive and president.is_alive():
            print("\nNew Round!")
            rounds += 1
            
            # Hero's turn to attack
            damage = hero.strike()
            hero_damage += damage
            print(f"Hero attacks {president.name} for {damage} damage!")
            president.take_damage(damage)

            # Check if the president was defeated
            if not president.is_alive():
                break
            #check if the hero is still alive
            if not hero.is_alive():
                break

            # President's turn to attack
            damage = president.attack()
            print(f"{president.name} attacks hero for {damage} damage!")
            hero.receive_damage(damage)
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    if hero.is_alive():
        print("The hero stands victorious! ༼ つ ◕_◕ ༽つ")
    else:
        print("George Washington mercs the hero :(ಥ_ಥ)")

    print(f"Total rounds: {rounds}")
    print(f"Total damage dealt by hero: {hero_damage}")
    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
