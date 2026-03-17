import random
import time 

#Import on top
def class_choosing():
    print("What class are you choosing?")
    print("1. Warrior")
    print("2. Rogue")

    choice = input("Your choice: ")

    if choice == "1":
        Warrior()
    elif choice == "2":
        Rogue() 

def Warrior():
    Warrior = True
    print("You've became a Warrior. Ourah !")
    return Warrior 

def Rogue():
    Rogue = True
    print("You've became a Rogue. Ourah !")
    return Rogue 

player_name = input("what's you're name ?")
player_class = class_choosing()


class Stat:
    def __init__(self, health, strength, defense, speed):
        self.health = health 
        self.strength = strength
        self.defense = defense
        self.speed = speed

class Character:
    def __init__(self,name,classe ):
        self.name = name
        self.classe = classe
        if self.classe == "Warrior":
            self.stat = Stat(100,5,5,5)
        elif self.classe == "Rogue":
            self.stat = Stat(75,3,5,7)



player= Character(player_name,player_class)
print(player.name)


#J'ai pas encore fait de systeme ou les stats influent sur l'attack et la vie. Je suis fatigué

def attack(damage, health):
    health += -damage
    return health

Hero_Hp = 100
Golbin_attack = random.randint(1, 15)
Hero_Hp = attack(Golbin_attack, Hero_Hp)
if Golbin_attack == 1 :
    print("Le Goblin attaque" ,player.name ,  " pour 1 miserable dégât")
else:
    print("Le Golblin attaque ", player.name, "pour ", Golbin_attack, "dégâts")

time.sleep(1)

print("You're current health is ", Hero_Hp)