import time
import random
import playerClass as pC
import monsterClass as mC

# fight handler to see who is fighting and give the correct output based on that
def fight_handler(the_one_who_attack, monster, player):
    if the_one_who_attack == "Player":
        type_of_attack = input("Choose your attack ! (défault = attack) ")
        if type_of_attack == "attack":
            player.attack()
            monster.take_damage(player.attack(), player)
            monster.check_status()
        elif type(type_of_attack) == pC.Ability:
            damage = player.use_ability(type_of_attack)
            monster.take_damage(damage, player)
            monster.check_status()
        else:
            print("wrong input")
    else:
        monster.damage_manager(player)
        player.check_status()

# change the side of the fight
def side_changer(player, monster):
        while(not player.check_status or not monster.ckeck_status()):
            random_result = random.random()
            if random_result > 0.5:
                fight_handler("Player", monster, player)
            else:
                fight_handler("Monster", monster, player)

# event 1 the dark cave :

def event_manager_1(choice, player):
    if choice == 'Right':
        print("You continue on your way and everything seems calm, maybe even too calm? ")
        time.sleep(2)
        blake_snake = mC.Monster("black snake", 1)
        print(f"an {blake_snake.name} has just arrived! Running away is not an option !")
        print("You decide to attack !")
        side_changer(player, blake_snake)
        
    else:
        pass