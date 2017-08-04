class World:

    def __init__(self, width, height):
        self.world = []
        self.width = width
        self.height = height
        self.random_world(width, height)

    def random_world(self, width, height):
        # create width
        for i in range(width):
            self.world.append([])

        # create height
        for i in range(width):
            for j in range(height):
                self.world[i].append([])

        # add world_objects
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                grass = WorldObject("_", i, j, 0)
                self.add_object(grass)

    def print_world(self):
        for i in range(self.width):
            for j in range(self.height):

                print(self.world[i][j][-1], end=" ")
            print()

    def print_world_all_objects(self):
        for i in range(self.width):
            for j in range(self.height):
                for k in range(len(self.world[i][j])):
                    print(self.world[i][j][k], end="")
                print(end=" ")
            print()

    def add_object(self, world_object, depth=None):
        if depth is None:  # if no depth specified, add to top of that tile
            self.world[world_object.x_coord][world_object.y_coord].append(world_object)
            world_object.depth = len(self.world[world_object.x_coord][world_object.y_coord]) - 1
        else:
            self.world[world_object.x_coord][world_object.y_coord][depth] = world_object
            world_object.depth = depth

    def remove_object(self, world_object):
        self.world[world_object.x_coord][world_object.y_coord].remove(world_object)

    # will move object to top level of new spot.
    def move_object(self, world_object, new_y, new_x):

        # pop from old spot
        self.remove_object(world_object)

        # add to new spot
        self.world[new_x][new_y].append(world_object)

        # update object values
        world_object.y_coord = new_y
        world_object.x_coord = new_x
        world_object.depth = len(self.world[new_x][new_y]) - 1


# for objects in the world, that way I can get super granular later
class WorldObject:
    def __init__(self, symbol, y_coord,  x_coord, depth=None):
        self.symbol = symbol
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.depth = depth

    def __str__(self):
        return self.symbol





