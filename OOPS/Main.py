from Enemy import *
from Zombie import *
from Ogre import *

zombie = Zombie(100,10)

print(zombie.get_enemytype())

print(zombie.talk())
print(zombie.eat())
print(zombie.spraad())

ogre = Ogre(1,100)
print(ogre.get_enemytype())