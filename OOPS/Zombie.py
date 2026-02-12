from Enemy import *


class Zombie(Enemy):
    def __init__(self,health,attack):
        super().__init__(enemytype='Zombie',
                         health=health,
                         attack=attack)

    def talk(self):
        print((f"this is the zomboe that is going to eat you got it!@"))

    def eat(self):
        print(f"and has a health and it is going to kill you like anything")
    def spraad(self):
        print("Zombie spread the disease")