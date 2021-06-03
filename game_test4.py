from math import fabs
import random
import time
from random import randrange
from time import monotonic_ns, sleep
import sys 

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

def typewriter(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.03)


def forgotten_land():
    global monster_option, monster1
    typewriter("Entering the Forgotten land...\n")
    time.sleep(0.5)
    typewriter("Ohh great! Look what we have disturbed on entry!!\n")
    time.sleep(0.5)
    monster1.set_health(300)
    monster_option = 3
    monster1 = enemy_gen() 
    first_fight()
    time.sleep(1)
    if monster1.get_hp() < 0:
        typewriter("Sephiroth fly's into the wall and hits the ground\n")
        time.sleep(1.5)
        typewriter("If you have enjoyed playing Text Quest\n - Give CodeNation a follow on instagram and twitter")
    elif player.get_hp() <= 0:
        typewriter("Try Again!!!")
        if class_chosen == "Rogue":
            player.set_health(250)
        elif class_chosen == "Magician":
            player.set_health(150)
        elif class_chosen == "Reaper":
            player.set_health(200)
            time.sleep(1)
        forgotten_land()
        

def portal():
    typewriter("you have been granted acsess to the portal\n")
    time.sleep(0.5)
    typewriter("you go through the portal\n")
    forgotten_land()



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
    typewriter("")


#Health bar monster
def do_enemy_health(background_colour, background_colour_end):
    global max_health, health_dashes, hp_rogue, hp_monster, max_health_monster
    dash_convert = int(max_health_monster / health_dashes)
    current_dashes = int(monster1.get_hp() / dash_convert)
    remaining_health = health_dashes - current_dashes
    health_display = "-" * current_dashes
    remaining_display = " " * remaining_health

    return "|" + background_colour + health_display + background_colour_end + remaining_display + "|"
    
#animeted health bar monster
def enemy_health_bar():
    print(red + "     __  __           ____  __  \n    / / / /__  ____ _/ / /_/ /_ \n", "  / /_/ / _ \/ __ `/ / __/ __ \   " + rend, f"{do_enemy_health(bred, brend)}\n", red + " / __  /  __/ /_/ / / /_/ / / /", f"             {monster1.get_hp()}\n", "/_/ /_/\___/\__,_/_/\__/_/ /_/ " + rend)
    typewriter("")



class_chosen = ""
Class = ("Rogue","Magician","Reaper")
option = 0
charecter = ""
# active = False
typewriter("Welcome to Text Quest!")
time.sleep(1.5)
typewriter('''
Text Quest is a python text based RPG adventure game with different 
outcomes, choices and battles to be made each playthrough.

Can you make it to the end??
''')
Character_Name = input("Chose Your Characters Name: ").capitalize()
time.sleep(1)
typewriter(f"{Character_Name} Please Choose Your Class \n")

def choose_class():
    global class_chosen
    typewriter(f"1: {Class[0]}")
    typewriter("- the Rogue is an assasin based class with regular attack power but high HP\n")
    time.sleep(0.5)
    typewriter(f"2: {Class[1]}")
    typewriter("- the Magician is a magic base class with High attack but low HP\n")
    time.sleep(0.5)
    typewriter(f"3: {Class[2]}")
    typewriter("- the Reaper is a Ranged attacker with the use of a Mini gun, this class a regular HP\n")
    time.sleep(0.5)
    option = int(input("Enter the number of your selected class: "))
    
    if option == 1:
        class_chosen = "Rogue"
        return player(Character_Name, 250 , 20 , 40 , 50)
    elif option == 2:
        class_chosen = "Magician"
        return player(Character_Name, 150 , 40 , 60, 90)
    elif option == 3:
        class_chosen = "Reaper"
        return player(Character_Name, 200 , 30 , 50 , 60)

monster_option = 3
         
def enemy_gen():
    global monster, monster1, monster_option
    if monster_option == 1:
        return monster("Mutant", 200 , 80)
    elif monster_option == 2:
        return monster("Bahamut", 200 , 40 ,)
    elif monster_option == 3:
        return monster("Sephiroth", 300 , 50 )


player = choose_class()
monster1 = enemy_gen()
# bahamut = monster("bahamut", 200, 40)
# sephiroth = monster("sephiroth", 300, 40)
max_health = player.get_hp()
max_health_monster = monster1.get_hp()
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
        typewriter("Loading...")
        time.sleep(0.5)
        typewriter("You are entering the wilderness of the dark jungle\n")         
        time.sleep(1)
        typewriter("After hours of being lost in the Jungle, you stumble upon a Temple.\n The enterance looks clear & you go in... Oh no! You have alerted the Temple Guardian!\n")
        temple_guardian = input("Temple Guardian has found you & its his job to stop you... Do you Attack or Run? a/r :")
        while temple_guardian != "a" and temple_guardian != "r":
            typewriter("Invalid selection!\n")
            temple_guardian = input("Temple Guardian has found you & its his job to stop you... Do you Attack or Run? a/r :")
        if temple_guardian == "a":
                typewriter("You have Died... Game Over!")
                time.sleep(0.5)
                typewriter("Try again...")
                time.sleep(0.5)
                choose_location()
                active = False
                time.sleep(1)
                break
        elif temple_guardian == "R" or temple_guardian == "r":
                typewriter("You choose to run!... Smart choice...but in your haste, you managed to set off a trap, & now the floor beneath you begins to collapse!")
                time.sleep(0.5)
                temple_choice = "J","F"
                temple_choice = input("Time to make a split second decision. Do you use your Parkour skills & jump to the ledge or fall through the floor? j/f")
                time.sleep(0.5)
                if temple_choice.lower() == "j":
                    typewriter("The jump has lead you to a doorway & you enter. You are met by Bahamut!!")
                    time.sleep(0.5)
                    active = False
                    random_riddle()
                else:
                    typewriter("Fell through the floor & landed in The Tomb of The Dead Corpses! You see a light at the end")
                    time.sleep(0.5)  
                    typewriter("The light leads you to a portal & with no other way out, you go through the portal")
                    forgotten_land()
                    active = False

location = "J","D"

def player_hit():
    global hp_rogue, poison, rogue_abilities, monotonic_ns, abilities

    rand_num = random.randint(1, 5)
    if rand_num in [1, 2, 3,]:
        typewriter(f"your choice is\n 1 = {abilities[0]}\n 2 = {abilities[1]}\n 3 = {abilities[2]}\n ")
        var = input()
        if var == "1":
            typewriter (var)
            monster1.set_health(monster1.get_hp() - player.get_ability1())
        elif var == "2":
            monster1.set_health(monster1.get_hp() - player.get_ability2())
        else:
            monster1.set_health(monster1.get_hp()- player.get_ability3())
    else:
        typewriter("you attacked but missed \n")

# player_hit()

def enemy_hit():
    global hp_rogue, poison, rogue_abilities, monotonic_ns
    rand_num = random.randint(1, 10)
    if rand_num in [1, 2, 3, 4, 5]:
        typewriter("the monster has attacked you \n")
        player.set_health(player.get_hp() - monster1.get_ability1())
    else:
        typewriter("the monster attacked but missed \n")

def first_fight():
    while monster1.get_hp() >= 0 or player.get_hp() >= 0:
     
        player_hit()
        typewriter(f"{monster1.get_hp()}")
        enemy_health_bar()
        if monster1.get_hp() <= 0:
            typewriter("you have killed the monster")
            break 
        enemy_hit()
        health_bar()
        if player.get_hp() <= 0:
            typewriter("you have died")
            break




def la_fight():
    global monster_option, monster1
    typewriter("Loading...")
    time.sleep(0.5)
    typewriter("You are entering inner city LA, where darkness has taken over the bright lights and monsters patrol the once lively city")
    time.sleep(1)
    typewriter("While searching for a safe route to area 51 a mutant blocks your path")
    downtown_mutant = input("The mutant has found you & is ready to strike... Do you Attack or Run? a/r :")
    if downtown_mutant.lower() == "a":
        typewriter("You have Died... Game Over!")
        time.sleep(0.5)
        typewriter("Try again...")
        time.sleep(0.5)
        choose_location()
    elif downtown_mutant == "R" or downtown_mutant == "r":
        typewriter("You begin to run!... As you are getting away, you meet a shadow figure it wants you to follow.")
        time.sleep(0.5)
        typewriter("You do to see where it will lead you, now that you have created some distance between you and the mutant")
        time.sleep(0.5)
        typewriter("This leads shadow to a battle and it needs your help!")
        time.sleep(0.5)
        monster_option = 1
        monster1 = enemy_gen()
        first_fight()
    if monster1.get_hp() < 0:
        post_shadow_fight()
    elif player.get_hp() <= 0:
        typewriter("Try Again!!!")
        if class_chosen == "Rogue":
            player.set_health(250)
        elif class_chosen == "Magician":
            player.set_health(150)
        elif class_chosen == "Reaper":
            player.set_health(200)
            time.sleep(3)
        choose_location()


def post_shadow_fight():
    typewriter("Thank you for your help, I couldn't have done it without you!")
    time.sleep(0.5)
    typewriter("The boss dropped this, it looks like a portal key... Lets jump through")
    time.sleep(0.5)
    forgotten_land()

def riddle_correct():
    typewriter("Bahamut has used the monsters biometrics to cut through the fabric of the jungle!")
    time.sleep(0.5)
    typewriter("This has accidently opened a worm hole that pulls you for a place far far away")
    time.sleep(0.5)
    forgotten_land()

def choose_location():
    global la_fight
    location = input("Would you like to start at Jungle or Downtown LA? j/d : ")
    if location.lower() in ["J","j"]:
        enetring_jungle()
    elif location.lower() in ["D","d"]:
        la_fight()
    else:
        typewriter("You only have two ways to turn, choose one of the following")
        choose_location()




def random_riddle():
    rand_num = random.randint(1, 3)
    if rand_num in [1]:
        riddle1()
    elif rand_num in [2]:
        riddle2()
    elif rand_num in [3]:
        riddle3()

def riddle1():
    global monster_option, monster1
    typewriter("To get past me you must answer this riddle...")
    time.sleep(0.5)
    typewriter("What is full of holes but still holds water?")
    time.sleep(0.5)
    typewriter('''
A.  A Coral Reef
B.  A Sponge
C.  The Earth
D.  An Old Backpack
        ''')
    answer = input("Your answer: ").lower()
    if answer == "b":
        typewriter(f"You answered: {answer}....")
        time.sleep(2.0)
        typewriter("Your right!")
        riddle_correct()
    else:
        typewriter("Incorrect! You shall face your doom!")
        time.sleep(0.1)
        monster_option = 2
        monster1 = enemy_gen()
        first_fight()
        if player.get_hp() <= 0:
            monster1.set_health(200) 
            random_riddle()
        elif monster1.get_hp() <= 0:
            portal()


def riddle2():
    global monster_option, monster1
    typewriter("To get past me you must answer this riddle...")
    time.sleep(0.5)
    typewriter("What month of the year has 28 days?")
    time.sleep(0.5)
    typewriter('''
A.  Febuary
B.  August
C.  None of them
D.  All of Them
        ''')
    answer = input("Your answer: ").lower()
    if answer == "d":
        typewriter(f"You answered: {answer}....")
        time.sleep(2.0)
        typewriter("Your right!")
        riddle_correct()
    else:
        typewriter("Incorrect! You shall face your doom!")
        time.sleep(0.1)
        monster_option = 2
        monster1 = enemy_gen()
        first_fight()
        if player.get_hp() <= 0:
            monster1.set_health(200)
            random_riddle()
        elif monster1.get_hp() <= 0:
            portal()




def riddle3():
    global monster_option, monster1
    typewriter("To get past me you must answer this riddle...")
    time.sleep(0.5)
    typewriter("What goes up but never comes down?")
    time.sleep(0.5)
    typewriter('''
A.  The Sun
B.  A Waterfall
C.  Your Age
D.  A Jumping Kangaroo
        ''')
    answer = input("Your answer: ").lower()
    if answer == "c":
        typewriter(f"You answered: {answer}....")
        time.sleep(2.0)
        typewriter("Your right!")
        riddle_correct()
    else:
        typewriter("Incorrect! You shall face your doom!")
        time.sleep(0.1)
        monster_option = 2
        monster1 = enemy_gen()
        first_fight()
        if player.get_hp() <= 0:
            monster1.set_health(200)
            time.sleep(0.5)
            random_riddle()
        elif monster1.get_hp() <= 0:
            time.sleep(0.5)
            portal()
            



choose_location()