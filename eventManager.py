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
        check_gameover(player)


# event 2 the forest :

def event_manager_2(choice, player):
    if choice == "1":
        print("You tell yourself that you have been lucky enough to have survived until now and decide to continue your journey. That's pretty wise.")
        print("You continue on your way and everything is normal, no monsters, no witches, no traps, everything is fine")
        print("No I'm just kidding.")
        choice_intern = input("A few steps away from you is a shady man walking towards you. You have two choices: \n 1 - Attack in anticipation \n 2-  wait for him to come to you, maybe he seems nice to you  \n ")
        if choice_intern == "1":
            print("You launch the first attack")
            demon_lord = mC.Monster("demon lord", 99)
            fight_handler("Player", demon_lord, player)
            side_changer(player, demon_lord)
            check_gameover(player)
        else:
            print("What do you expect? I already told you he was shady. Before you could even figure it out, he grabbed you and shoved a blade into you")
            player.isAlive = False
            check_gameover(player)
    elif choice == "2":
        print("You decide to follow the noise")
        print("The forest although threatening seems to welcome you with open arms")
        print("The noise intensifies, you must not be very far... That's where you find a group of villagers who are about to take a boat. It was the noise of the engine ")
        print("They explain that they are trying to escape a demon that has taken over this forest")
        print("They will join the neighboring village which is more prepared militarily for this kind of incident")
        choice_intern_2 = input("Would you like to join them? Y/N ")
        if choice_intern_2 == "Y":
            print("You decide to follow them")
            print("The atmosphere is nice on the boat. The villagers tell you about their daily life. Some start to make jokes and others prepare some good food")
            print("But you see a shadow coming towards you")
            print("Without really understanding why, the crew members start to fall one after the other. You quickly find yourself alone in front of the demon. He followed the boat to this point. Your only hope? To defeat it")
            print("You launch the first attack")
            demon_lord = mC.Monster("demon lord", 99)
            fight_handler("Player", demon_lord, player)
            side_changer(player, demon_lord)
            check_gameover(player)
        else:
            print("You decide that it would be better to continue your journey alone. This story seems too weird for you and you are not interested in traveling by boat")
            print("You continue your way and arrive at the end of the forest. You see a sign indicating the direction of a manor and you decide to go there")
            print("What will be waiting for you there ? More info in the next chapter !")
    else:
        print("wrong input")


# event 3 : the manor

def event_manager_3(choice, player):
    if choice == '1':
        player.stats = {
                'hp' : 1000,
                'attack' : 500,
                'defense' : 400,
                'magic' : 500,
                'mana' : 500
        }
        print("You have reached level 85. You seem wiser ")
        print("You go back on your steps and go to the central room. You see blood everywhere but mostly in the direction of the room on the left")
        choice_intern = input("Are you going to :  \n 1- take a closer look at this  \n 2- leave the mansion \n")
        if choice_intern == "1":
            print("You decide to take a closer look and you see a room full of dead bodies. Maybe the villagers' story was true after all.")
            print("You find a silver sword on one of the corpses and decide to take it with you")
            silver_sword = pC.Item("silver sword", "Sword made to kill demons")
            player.get_item(silver_sword)
            print("You see your attack being increased greatly")
            player.stats['attack'] += 50
            print("You hear the door open behind you. The demon has returned. Only you can stop him. The fight begins")
            demon_lord = mC.Monster("demon lord", 99)
            fight_handler("Player", demon_lord, player)
            side_changer(player, demon_lord)
            check_gameover(player)
            print("You come out triumphant from this painful fight but you saved this forest from this demon. You can be proud of yourself, you are a real hero")
        else:
            print("Barely arrived at the exit of the manor you feel a presence hiding behind you. You don't have time to react and you feel an attack pierce you. This is your end")
            player.isAlive = False
            check_gameover(player)
    else:
        player.stats['defense'] += 300
        print("You feel more resilient")
        print("You go back on your steps and go to the central room. You see blood everywhere but mostly in the direction of the room on the left")
        choice_intern = input("Are you going to :  \n 1- take a closer look at this  \n 2- leave the mansion \n")
        if choice_intern == "1":
            print("You decide to take a closer look and you see a room full of dead bodies. Maybe the villagers' story was true after all.")
            print("You find a silver sword on one of the corpses and decide to take it with you")
            silver_sword = pC.Item("silver sword", "Sword made to kill demons")
            player.get_item(silver_sword)
            print("You see your attack being increased greatly")
            player.stats['attack'] += 50
            print("You hear the door open behind you. The demon has returned. Only you can stop him. The fight begins")
            demon_lord = mC.Monster("demon lord", 99)
            fight_handler("Player", demon_lord, player)
            side_changer(player, demon_lord)
            check_gameover(player)
            print("You come out triumphant from this painful fight but you saved this forest from this demon. You can be proud of yourself, you are a real hero")
        else:
            print("Barely arrived at the exit of the manor you feel a presence hiding behind you. You don't have time to react and you feel an attack pierce you. This is your end")
            player.isAlive = False
            check_gameover(player)