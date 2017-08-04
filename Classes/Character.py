from Classes.World import WorldObject, World


class Character:
    def __init__(self, health, attack, symbol, x_coord, y_coord, world, name):
        self.health = health
        self.attack = attack
        self.world_object = WorldObject(symbol, x_coord, y_coord)
        self.world = world
        self.name = name



    def attack(self):
        return self.attack

    def take_damage(self, amount):
        self.health -= amount
        return amount

    def heal(self, amount):
        self.health += amount

    def walk(self, direction):
        # can be N, S, E, W
        if direction not in ["up", "down", "right", "left"]:
            return False
        elif direction in ["up"]:
            self.world.move_object(self.world_object, self.world_object.y_coord, self.world_object.x_coord - 1)
        elif direction in ["down"]:
            self.world.move_object(self.world_object, self.world_object.y_coord, self.world_object.x_coord + 1)
        elif direction in ["right"]:
            self.world.move_object(self.world_object, self.world_object.y_coord + 1, self.world_object.x_coord)
        elif direction in ["left"]:
            self.world.move_object(self.world_object, self.world_object.y_coord - 1, self.world_object.x_coord)

    def run(self, move):
        if move in ["up"]:
            self.walk("down")
        elif move in ["down"]:
            self.walk("up")
        elif move in ["right"]:
            self.walk("left")
        elif move in ["left"]:
            self.walk("right")
