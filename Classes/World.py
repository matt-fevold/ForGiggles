class World:

    def __init__(self,  width, height):
        self.world = []
        self.width = width
        self.height = height
        self.create_world(width, height)
        self.default_world()

    def create_world(self, width, height):
        # create width
        for i in range(width):
            self.world.append([])

        # create height
        for i in range(len(self.world)):
            for j in range(height):
                self.world[i].append([""])

    def default_world(self):    # add world_objects
        for col in range(len(self.world)):
            for row in range(len(self.world[col])):
                default = WorldObject("_", col, row, 0)
                self.add_object(default, col, row)

    # if depth is provided they want just a single object on tile, otherwise return whole tile
    def get_tile(self, col, row, depth=None):
        if depth is not None:
            return self.world[col][row][depth]
        else:
            return self.world[col][row]

    def print_world(self):
        for col in range(len(self.world)):
            for row in range(len(self.world[col])):

                print(self.get_tile(col, row, -1), end=" ")
            print()

    def print_world_all_objects(self):
        for col in range(len(self.world)):
            for row in range(len(self.world[col])):
                for depth in range(len(self.get_tile(col, row))):
                    print(self.get_tile(col, row, depth), end="")
                print(end=" ")
            print()

    def add_object(self, world_object, col, row, depth=None):
        if depth is None:  # if no depth specified, add to top of that tile, you typically will not be using depth

            self.world[col][row].append(world_object)
            world_object.set_col(col)
            world_object.set_row(row)

            # set depth of the object - only to use initializing since you can overwrite objects
            world_object.set_depth(len(self.world[col][row]) - 1)
        else:
            self.world[col][row][depth] = world_object
            world_object.setdepth(depth)

    def remove_object(self, world_object):
        self.world[world_object.col][world_object.row].remove(world_object)

    # will move object to top level of new spot.
    def move_object(self, world_object, row, col):

        # pop from old spot
        self.remove_object(world_object)

        # add to new spot
        self.world[col][row].append(world_object)

        # update object values
        world_object.change_spot(col, row, len(self.world[col][row]) - 1)


# for objects in the world, that way I can get super granular later
class WorldObject:
    def __init__(self, symbol, col,  row, depth=None):
        self.symbol = symbol
        self.col = col
        self.row = row
        self.depth = depth

    def __str__(self):
        return self.symbol

    def set_col(self, col):
        self.col = col

    def set_row(self, row):
        self.row = row

    def set_depth(self, depth):
        self.depth = depth

    def change_spot(self, col, row, depth):
        self.set_col(col)
        self.set_row(row)
        self.set_depth(depth)

# following should not be used, only not deleted since there is some logic I might want to use when rebuilding this.
def print_local_map(self, current_x, current_y, line_of_sight):
        local_map = []

        # create local map with nothing but darkness aka ~
        for i in range(line_of_sight * 2 + 3):
            local_map.append(["~"])

        for i in range(len(local_map)):
            for j in range(line_of_sight * 2 + 2):
                local_map[i].append(["~"])

        # add in top half NEEDS WORK :(
        for i in range(1, line_of_sight + 1):
            for j in range(2 * (i - 1) + 1):
                local_map[i][j + line_of_sight + 1 - j] = self.world[current_y - i][current_x - line_of_sight + 3 - j]

        # add in middle
        for i in range(1, line_of_sight + 1):
            pass

        # add in bottom
        for i in range(line_of_sight + 1):
            pass

        for i in range(len(local_map)):
            for j in range(len(local_map[i])):

                print(local_map[i][j][-1], end=" ")
            print()



