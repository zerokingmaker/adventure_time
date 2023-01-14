class Monster():
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.isAlive = True
        self.stats = {
                'hp' : self.level * 4,
                'attack' : self.level * 2,
                'defense' : self.level * 4,
        }
    

    # Manage how much damages the player takes
    def damage_manager(self, player):
        damage_output = self.stats['attack'] - player.self.stats['defense']
        player.self.stats['hp'] -= damage_output
        print(f'{player.name} took {damage_output} damages')
        return damage_output

    # check how monster takes damages
    def take_damage(self, damage, player):
        damage_taken = damage - self.stats['defense']
        self.stats['hp'] -= damage_taken
        print(f'{self.name} took {damage_taken} damages from {player.name}')

    # check if the monster is dead
    def check_status(self):
        if self.stats['hp'] <= 0:
            self.isAlive = False
        else:
            self.isAlive = True

    