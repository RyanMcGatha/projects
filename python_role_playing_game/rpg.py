"""
In this simple RPG game, the Hero fights the Goblin. He has the options to:

1. fight Goblin
2. do nothing - in which case the Goblin will attack him anyway
3. flee

"""

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("%s does %d damage to the %s." % (self.__class__.__name__, self.power, enemy.__class__.__name__))
        if enemy.health <= 0:
            print("The %s is dead." % enemy.__class__.__name__)

    def print_status(self):
        print("%s has %d health and %d power." % (self.__class__.__name__, self.health, self.power))

    def alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

def main():
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()

        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()

        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():
            goblin.attack(hero)

main()




