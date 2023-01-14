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
elif player_specialisation == "Warior":
    new_player = pC.Warior(player_name)
else:
    raise eM.wrongspecialisationError(player_specialisation)


print(f"Welcome {new_player.name} to this new world !")
print("You will have to overcome many trials along your adventure. It will be a series of choices... Good luck !")

choice1 = input("You arrive in a dark cave and you seem to see two paths. Which one do you take? Right or left")

# choice 1 manager :
if choice1 == 'Right':
    pass
else:
    pass
