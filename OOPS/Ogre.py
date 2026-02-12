
from Enemy import *

class Ogre(Enemy):
    def __init__(self,health,attack):
        super().__init__(enemytype="Ogre",
                         health=health,
                         attack=attack)
