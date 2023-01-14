import monsterClass as mC
import playerClass as pC
import exceptionManager as eM
import eventManager as eMgr

print('Welcome to our new story: "adventure time".')
print("Before continuing, please create your character")
player_name = input("What is your name ? ")
player_specialisation = input("What will be your class ? Mage or Warior ? ")


# check player specialistion
if player_specialisation == "Mage":
    new_player = pC.Mage(player_name)
    fireball = pC.Ability("fireball", 10, "throws a fireball", 5, 'Mage')
    new_player.learn_ability(fireball)
elif player_specialisation == "Warior":
    new_player = pC.Warior(player_name)
else:
    raise eM.wrongspecialisationError(player_specialisation)


print(f"Welcome {new_player.name} to this new world !")
print("You will have to overcome many trials along your adventure. It will be a series of choices... Good luck !")

choice1 = input("You arrive in a dark cave and you seem to see two paths. Which one do you take? Right or left ")

#  the cave
eMgr.event_manager_1(choice1, new_player)

# the forest
print("Finally, you arrive at the end of the path. You see light at the end of the tunnel.  You decide to go out and you find yourself in a forest! ")
print("You start to explore the forest and you hear a noise in the distance. ")
choice2 = input("What are you doing? Are you going to:  \n 1- Continue on your way  \n 2- Are you going to follow the noise ? \n")

eMgr.event_manager_2(choice2, new_player)

# the manor
print("You finally arrive in front of the mansion. You knock on the door and it opens slowly. You call out to see if anyone is there but no one seems to answer.")
print("You tell yourself that after having come this far, it would be a shame to turn back and so you continue your exploration of the manor")
choice3 = input("You find in a room two relics: \n 1 - relic of wisdom \n 2- relic of endurance \n What will you take ? ")
eMgr.event_manager_3(choice3, new_player)