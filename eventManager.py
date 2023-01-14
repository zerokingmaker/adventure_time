import time
import random
import playerClass as pC
import monsterClass as mC
from sys import exit

# general purpose fonction

# fight handler to see who is fighting and give the correct output based on that
def fight_handler(the_one_who_attack, monster, player):
    if the_one_who_attack == "Player":
        type_of_attack = input("Choose your attack ! (défault = attack) ")
        if type_of_attack == "attack":
            monster.take_damage(player.attack(), player)
            monster.check_status()
        elif type_of_attack == "fireball":
            fireball = pC.Ability("fireball", 10, "throws a fireball", 5, 'Mage')
            damage = player.use_ability(fireball)
            monster.take_damage(damage, player)
            monster.check_status()
        else:
            print("wrong input")
    else:
        monster.damage_manager(player)
        player.check_status()

# change the side of the fight
def side_changer(player, monster):
        while(player.isAlive and monster.isAlive):
            random_result = random.random()
            print(player.isAlive)
            if random_result > 0.5:
                fight_handler("Player", monster, player)
                check_gameover(player)
            else:
                fight_handler("Monster", monster, player)
                check_gameover(player)


# check if the game is over
def check_gameover(player):
    if not player.isAlive:
        print("And so your journey ends...")
        reset_stats(player)
        exit()

# reset player stats at the end of the game
def reset_stats(player):
    if player.specialisation == "Mage":
        player = pC.Mage(player.name)
    else:
        player = pC.Warior(player.name)

# end of general purpose fonctions

# event 1 the dark cave :

def event_manager_1(choice, player):
    if choice == 'Right':
        print("You continue on your way and everything seems calm, maybe even too calm? ")
        time.sleep(2)
        blake_snake = mC.Monster("black snake", 1)
        print(f"an {blake_snake.name} has just arrived! Running away is not an option !")
        print("You decide to attack !")
        fight_handler("Player", blake_snake, player)
        side_changer(player, blake_snake)
        check_gameover(player)
        print("It was an uphill battle but you managed to triumph !")
        pick_item = input("The enemy dropped an object, do you want to pick it up? Y/N ")
        if pick_item == "Y":
            potion = pC.Item("potion", "Gives you 20 hp back")
            player.get_item(potion)
            player.use_item(potion)
            player.stats['hp'] += 20
        else:
            print("Alright. You can leave it here")
        print("We thus continue our way further")
        
    else:
        print("Hum you seem to hear some noise in the distance, you decide to keep going even more in the darkness")
        time.sleep(2)
        print("a door stands in front of you... What could it be hiding? You decide to open it and ....")
        time.sleep(2)
        print("It was a trap! The cellar collapses and you suffocate. This is a gameover.")
        player.isAlive = False
        check_gameover()