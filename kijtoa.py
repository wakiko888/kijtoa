import random
import time 



#Import on top
def dmg_calc(strength,weapon_mutipl):
    formual = (strength/10) + weapon_mutipl
    if formual < 1:
        formual =  1
    damage = random.randint(1,10) * formual
    return damage

def attack_order(speed_hero, speed_monster):
    if speed_hero > speed_monster:
        order = 0
    elif speed_monster > speed_hero:
        order = 1
    elif speed_hero ==speed_monster:
        order = random.randint(0,1)
    return order

    
def class_choosing():
    print("So... What class are you choosing?\n")
    print("1. Warrior")
    print("2. Rogue")
    choice = input("Your choice:\n ")
    if choice == "1":
        return Warrior()
    elif choice == "2":
        return Rogue() 

def Warrior():
    Warrior = True
    print("You've became a Warrior. Ourah !")
    return "Warrior"

def Rogue():
    Rogue = True
    print("You've became a Rogue. Ourah !")
    return "Rogue"

def attack(damage, health):
    health += -damage
    return health

#Fonction on top

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
        else:
            self.stat = Stat(50,1,1,1)


#Class on top
#Game and test

player_name = input("what's you're character name ?\n")
player_class = class_choosing()
player= Character(player_name,player_class)
Goblin = Character("philipe","Rogue")
Goblin_attack = dmg_calc(Goblin.stat.strength, 0)

while 1==1:
    if player.stat.health <=0:
        print("Game over....")
        
    


player.stat.health = 0


attack(Goblin_attack, player.stat.health)
if Goblin_attack == 1 :
    print("Le Goblin attaque" ,player.name ,  " pour 1 miserable dégât")
else:
    print("Le Goblin attaque ", player.name, "pour ", Goblin_attack, "dégâts")
time.sleep(1)
print("You're current health is ", player.stat.health)