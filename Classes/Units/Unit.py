from Classes.Equipment import Equipment
# Base class for all units in the game.


class Unit:
    def __init__(self, name, unit_type, strength, agility, intelligence, charisma, level=0, iron_flesh=0, power_strike=0,
                 one_hand=0):
        # identifying information
        self.name = name
        self.total_health = 0  # initialized here
        self.experience = 0  # not used yet
        self.current_health = self.total_health
        self.unit_type = unit_type
        self.level = level

        # what the users equipment is.
        self.equipment = Equipment.Equipment()  # default = no equipment

        # attributes
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.charisma = charisma

        # secondary skills
        self.iron_flesh = iron_flesh
        self.power_strike = power_strike
        # more to come, they just don't matter right now.

        # proficiencies
        self.one_hand = one_hand
        # more to come, they just don't matter right now.

        # do post-skill value calculations
        self.calculate_health()  # determine health based off stats.

    def calculate_health(self):
        self.total_health = self.strength * 4 + self.iron_flesh
        self.current_health = self.total_health

    def add_stats(self):
        pass
        # need to find a good way to edit certain stats...

    # pretty print stats
    def print_stats(self):
        print("Name: " + self.name)
        print("Class: " + self.unit_type)
        print("Health: " + str(self.current_health) + " / " + str(self.total_health))
        print("level: " + str(self.level))
        print("Str: " + str(self.strength))
        print("Agi: " + str(self.agility))
        print("Int: " + str(self.intelligence))
        print("Cha: " + str(self.charisma))
        print("more stats go here...")

    def print_equipment(self):
        self.equipment.print_equipment()

    def __str__(self):
        return self.unit_type + ": " + self.name + " (" + str(self.level) + ")"
