class Enemy:

    def __init__(self,enemytype,health=90,attack=2):
        self.__enemytype = enemytype
        self.health = health
        self.attack = attack

    def get_enemytype(self):
        return self.__enemytype

    def talk(self):
        print("I am an enemy, I will kill you")

