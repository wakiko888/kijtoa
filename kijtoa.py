import random
import time 
#Import on top 


def attack(damage, health):
    health += -damage
    return health

Hero_Hp = 100
Golbin_attack = random.randint(1, 15)
Hero_Hp = attack(Golbin_attack, Hero_Hp)
if Golbin_attack == 1:
    print("Le Goblin attaque pour 1 miserable dégât")
else:
    print("Le Golblin attque pour ", Golbin_attack, "dégâts")

print(Hero_Hp)
