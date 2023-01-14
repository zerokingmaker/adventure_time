class Hero():
    def __init__(self, name, race, gender, specialisation):
        self.name = name
        self.race = race
        self.gender = gender
        self.specialisation = specialisation
        self.level = 1
        self.inventory = {}

        # stat attribute based on specialisation
        if self.specialisation == 'Warior':
            pass


class Item():
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


class Monster():
    def __init__(self, name, level):
        self.name = name
        self.level = level