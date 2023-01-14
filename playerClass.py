class Hero():
    def __init__(self, name, specialisation):
        self.name = name
        self.level = 1
        self.isAlive = True
        self.stats = {}
        self.specialisation = specialisation
        self.abilities = {}
        self.inventory = {}

    # ability manager
    def use_ability(self, ability):
        if ability.name not in self.abilities:
            return print("You don't have this ability !")

        if self.specialisation == "Mage":
            if self.stats['mana'] < ability.mana_cost:
                print("You don't have enought mana")
            else:
                self.stats['mana'] -= ability.mana_cost
                if ability.damage > 0:
                    damage_output = ability.damage * self.stats['magic']
                    print(f"You used {ability.name}")
                    print(f'You did {damage_output} damages')
                    return damage_output
                else:
                    print(ability.effect)
        else:
            if ability.damage > 0:
                damage_output = ability.damage * self.status['magic']
                print(ability.effect)
                print(f'You did {damage_output} damages')
                return damage_output
            else:
                print(ability.effect)

    def learn_ability(self, ability):
        if ability in self.abilities:
            print("You have already learned this ability")
        elif type(ability) == Ability:  # to check if it's from the Ability class
            if ability.class_requirement != self.specialisation:
                return print("You cannot learn this ability")
            else:
                self.abilities.update({ability.name : ability.effect})
                print(f"You learned {ability.name}")
        else:
            print("This ability doesn't exist !")

    # basic attack manager
    def attack(self):
        print('You used your normal attack')
        return self.stats['attack'] 

    # item manager
    def use_item(self, item):
        if item.name not in self.inventory:
            return print("You don't have this item")
        else:
            self.inventory[item.name] -= 1
            print(f'You used {item.name}')
            return item.effect

    def get_item(self, item):
        if type(item) == Item:
            print(f'added {item.name} to the inventory')
            if item not in self.inventory:
                self.inventory[item.name] = 0
            else:
                self.inventory[item.name] += 1
        else:
            print("This item doesn't exist")


    # check if the player is alive
    def check_status(self):
        if self.stats['hp'] <= 0:
            self.isAlive = False
        else:
            self.isAlive = True
        
    
    # print a summary of the player
    def __repr__(self):
        current_hp = self.stats['hp']
        current_inventory = len(self.inventory.keys())
        return f'Player {self.name} have currently {current_hp} hp. You have in your inventory {current_inventory} items'
    

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name,'Mage')
        self.stats = {
                'hp' : self.level * 6,
                'attack' : self.level * 2,
                'defense' : self.level * 2,
                'magic' : self.level * 13,
                'mana' : 200
        }


class Warior(Hero):
    def __init__(self, name):
        super().__init__(name, 'Warior')
        self.stats = {
                'hp' : self.level * 10,
                'attack' : self.level * 6,
                'defense' : self.level * 4,
                'magic' : self.level * 0
        }

class Ability():
    def __init__(self, name, mana_cost, effect, damage, class_requirement):
        self.name = name
        self.mana_cost = mana_cost
        self.effect = effect
        self.damage = damage
        self.class_requirement = class_requirement

    
    # print a summary of the ability
    def __repr__(self):
        return f'{self.name} has the effect : {self.effect}'



class Item():
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    # print a summary of the item
    def __repr__(self):
        return f'{self.name} has the effect : {self.effect}'



