from Enemy import *

enemy = Enemy("zombie",100,10)
print(f"type of enemy : {enemy.get_enemytype()}, health : {enemy.health}, attack : {enemy.attack}")

enemy.talk()

print()
print()

print(enemy.get_enemytype())

