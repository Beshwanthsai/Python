class Enemy:

    def __init__(self,enemytype,health,attack):
        self.__enemytype = enemytype
        self.health = health
        self.attack = attack

    def get_enemytype(self):
        return self.__enemytype

    def talk(self):
        print(f"{self.__enemytype} and has a health of {self.health} health and is talking to you")

    def eat(self):
        print(f"{self.__enemytype} and has a health and it is going to kill you")

    def special_attack(self):
        print("Enemy has no special attack!")