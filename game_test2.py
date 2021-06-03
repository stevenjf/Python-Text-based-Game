from math import fabs
import random
import time
from random import randrange
from time import monotonic_ns, sleep
import sys 

def typewriter(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)


class player:
    def __init__(self, pname, phealth, ability1, ability2, ability3):
        self.name = pname
        self.health = phealth
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3

    def get_name(self):
        return self.name
    def get_hp(self):
        return self.health
    def get_ability1(self):
        return self.ability1
    def get_ability2(self):
        return self.ability2
    def get_ability3(self):
        return self.ability3

    def set_health(self, new_health):
        self.health = new_health


class monster:
    def __init__(self, mname, mhealth, mability1):
        self.name = mname
        self.health = mhealth
        self.ability1 = mability1
        
    def get_name(self):
        return self.name
    def get_hp(self):
        return self.health
    def get_ability1(self):
        return self.ability1

    def set_health(self, new_health):
        self.health = new_health


# colours 
red = "\33[91m"
bred = "\33[41m" + "\033[91m"
rend = "\33[0m"
brend = "\33[0m" + "\033[0m"
green = "\33[92m"
bgreen = "\33[102m" + "\33[92m"
gend = "\33[0m"
bgend = "\33[0m" + "\33[0m"
purple = "\33[35m"
pend = "\33[0m"

#health bar count
health_dashes = 20


#Health bar player
def do_health(background_colour, background_colour_end):
    global max_health, health_dashes, hp
    dash_convert = int(max_health / health_dashes)
    current_dashes = int(player.get_hp() / dash_convert)
    remaining_health = health_dashes - current_dashes
    health_display = "-" * current_dashes
    remaining_display = " " * remaining_health

    return "|" + background_colour + health_display + background_colour_end + remaining_display + "|"


#animated health bar player
def health_bar():
    print(purple + "     __  __           ____  __  \n    / / / /__  ____ _/ / /_/ /_ \n", "  / /_/ / _ \/ __ `/ / __/ __ \   " + rend, f"{do_health(bred, brend)}\n", purple + " / __  /  __/ /_/ / / /_/ / / /", f"             {player.get_hp()}\n", "/_/ /_/\___/\__,_/_/\__/_/ /_/ " + rend)
    print("")


#Health bar monster
def do_enemy_health(background_colour, background_colour_end):
    global max_health, health_dashes, hp_rogue, hp_monster, max_health_monster
    dash_convert = int(max_health_monster / health_dashes)
    current_dashes = int(monster.get_hp() / dash_convert)
    remaining_health = health_dashes - current_dashes
    health_display = "-" * current_dashes
    remaining_display = " " * remaining_health

    return "|" + background_colour + health_display + background_colour_end + remaining_display + "|"
    
#animeted health bar monster
def enemy_health_bar():
    print(red + "     __  __           ____  __  \n    / / / /__  ____ _/ / /_/ /_ \n", "  / /_/ / _ \/ __ `/ / __/ __ \   " + rend, f"{do_enemy_health(bred, brend)}\n", red + " / __  /  __/ /_/ / / /_/ / / /", f"             {monster.get_hp()}\n", "/_/ /_/\___/\__,_/_/\__/_/ /_/ " + rend)
    print("")



class_chosen = ""
Class = ("Rogue","Magician","Reaper")
option = 0
charecter = ""
# active = False

print("Welcome to Text Quest!")
print('''
Text Quest is a python text based RPG adventure game with different 
outcomes, choices and battles to be made each playthrough.

Can you make it to the end??
''')
Character_Name = input("Enter Your Name: ").capitalize()
print(Character_Name, "Please Choose Your Class \n")

def choose_class():
    global class_chosen
    print("1:",Class[0],"- Special Ability\n")
    time.sleep(0.5)
    print("2:",Class[1],"- Special Ability\n")
    time.sleep(0.5)
    print("3:",Class[2],"- Special Ability\n")
    time.sleep(0.5)
    option = int(input("Enter the number of your selected class: "))
    
    if option == 1:
        class_chosen = "Rogue"
        return player(Character_Name, 200 , 20 , 40 , 60)
        
    elif option == 2:
        class_chosen = "Magician"
        return player(Character_Name, 150 , 30 , 50, 90)
    elif option == 3:
        class_chosen = "Reaper"
        return player(Character_Name, 200 , 20 , 40 , 60)

player = choose_class()
monster = monster("sephiroth", 200, 30 )
# bahamut = monster("bahamut", 200, 40)
# sephiroth = monster("sephiroth", 300, 40)
max_health = player.get_hp()
max_health_monster = monster.get_hp()
abilities = []
if class_chosen == "Rogue":
    abilities = ["back_stab", "life_drain", "assasination"]
elif class_chosen == "Magician":
    abilities = ["fireball", "icy_plains", "meteor_shower"]
elif class_chosen == "Reaper":
        abilities = ["stab", "phase", "Mini-gun"]



active = True
# def temple_guardian():

def enetring_jungle():
    global active
    while active:
        # temple_guardian = "A","R"
        print("Loading...")
        time.sleep(0.5)
        print ("You are entering the wilderness of the dark jungle")         
        time.sleep(1)
        print("After hours of being lost in the Jungle, you stumble upon a Temple. The enterance looks clear & you go in... Oh no! You have alerted the Temple Guardian!")
        temple_guardian = input("Temple Guardian has found you & its his job to stop you... Do you Attack or Run? a/r :")
        while temple_guardian != "a" and temple_guardian != "r":
            print("Invalid selection!\n")
            temple_guardian = input("Temple Guardian has found you & its his job to stop you... Do you Attack or Run? a/r :")
        if temple_guardian == "a":
                print("You have Died... Game Over!")
                print("Try again...")
                choose_location()
                active = False
                time.sleep(1)
                break
        elif temple_guardian == "R" or temple_guardian == "r":
                print("You choose to run!... Smart choice...but in your haste, you managed to set off a trap, & now the floor beneath you begins to collapse!")
                time.sleep(0.5)
                temple_choice = "J","F"
                temple_choice = input("Time to make a split second decision. Do you use your Parkour skills & jump to the ledge or fall through the floor? j/f")
                if temple_choice.lower() == "j":
                    print("The jump has lead you to a doorway & you enter. You are met by Bahamut!!")
                    time.sleep(0.5)
                    active = False
                else:
                    print("Fell through the floor & landed in The Tomb of The Dead Corpses! You see a light at the end")
                    time.sleep(0.5)  
                    print("The light leads you to a portal & with no other way out, you go through the portal")
                    active = False

location = "J","D"

def player_hit():
    global hp_rogue, poison, rogue_abilities, monotonic_ns, abilities

    rand_num = random.randint(1, 5)
    if rand_num in [1, 2, 3,]:
        typewriter(f"your choice is\n 1 = {abilities[0]}\n 2 = {abilities[1]}\n 3 = {abilities[2]}\n ")
        var = input()
        if var == "1":
            print (var)
            monster.set_health(monster.get_hp() - player.get_ability1())
        elif var == "2":
            monster.set_health(monster.get_hp() - player.get_ability2())
        else:
            monster.set_health(monster.get_hp()- player.get_ability3())
    else:
        typewriter("you attacked but missed \n")

# player_hit()

def enemy_hit():
    global hp_rogue, poison, rogue_abilities, monotonic_ns
    rand_num = random.randint(1, 5)
    if rand_num in [1, 2,]:
        typewriter("the monster has attacked you \n")
        player.set_health(player.get_hp() - monster.get_ability1())
    else:
        typewriter("the monster attacked but missed \n")

def first_fight():
    while monster.get_hp() >= 0 or player.get_hp() >= 0:
     
        player_hit()
        print(monster.get_hp())
        enemy_health_bar()
        if monster.get_hp() <= 0:
            print("you have killed the monster")
            break 
        enemy_hit()
        health_bar()
        if player.get_hp() <= 0:
            print("you have died")
            break

monster_option = ""
         
def enemy_gen():
    if monster_option == 1:
        return monster("Monster", 200 , 20)
    elif monster_option == 2:
        return monster("Bahamut", 200 , 30 ,)
    elif monster_option == 3:
        return monster("Sephiroth", 300 , 40 )



def la_fight():
    print("Loading...")
    time.sleep(0.5)
    print("You are entering inner city LA, where darkness has taken over the bright lights and monsters patrol the once lively city")
    time.sleep(1)
    print("While searching for a safe route to area 51 a mutant blocks your path")
    downtown_mutant = input("The mutant has found you & is ready to strike... Do you Attack or Run? a/r :")
    if downtown_mutant.lower() == "a":
        print("You have Died... Game Over!")
        print("Try again...")
        choose_location()
    elif downtown_mutant == "R" or downtown_mutant == "r":
        print("You begin to run!... As you are getting away, you meet a shadow figure it wants you to follow.")
        time.sleep(0.5)
        print("You do to see where it will lead you, now that you have created some distance between you and the mutant")
        time.sleep(0.5)
        print("This leads shadow to a battle and it needs your help!")
        monster_option = 1
        monster1 = enemy_gen()
        first_fight()
        post_shadow_fight()


def choose_location():
    location = input("Would you like to start at Jungle or Downtown LA? j/d : ")
    if location.lower() in ["J","j"]:
        enetring_jungle()
    elif location.lower() in ["D","d"]:
        la_fight()
    else:
        print("You only have two ways to turn, choose one of the following")
        choose_location()

def post_shadow_fight():
    print("SHADOW\n Thank you for your help, I couldn't have done it without you!")

choose_location()

