from Classes.World import WorldObject, World
from Classes.Army import Army
from Classes import Inventory


# needs rework
class Character:
    def __init__(self, health, attack, symbol, col, row, world, name):
        self.health = health
        self.attack = attack
        self.world_object = WorldObject(symbol, col, row)
        self.world = world
        self.name = name
        self.army = Army.Army(self.name)
        self.action_list = []
        self.inventory = Inventory.Inventory()

    def print_self(self):
        print("Name: " + self.name)
        print("More Stuff can go here")

    def walk(self, direction):
        # can be N, S, E, W
        if direction not in ["up", "down", "right", "left"]:
            return False
        elif direction in ["up"]:
            self.world.move_object(self.world_object, self.world_object.row, self.world_object.col - 1)
        elif direction in ["down"]:
            self.world.move_object(self.world_object, self.world_object.row, self.world_object.col + 1)
        elif direction in ["right"]:
            self.world.move_object(self.world_object, self.world_object.col, self.world_object.row + 1)
        elif direction in ["left"]:
            self.world.move_object(self.world_object, self.world_object.col, self.world_object.row - 1)

    def run(self, move):
        if move in ["up"]:
            self.walk("down")
        elif move in ["down"]:
            self.walk("up")
        elif move in ["right"]:
            self.walk("left")
        elif move in ["left"]:
            self.walk("right")


