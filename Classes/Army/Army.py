class Army:
    def __init__(self, leader):
        self.List_Of_Units = []  # no units in blank army
        self.leader = leader

    def print_army(self):
        print("Army: ")
        for i in range(len(self.List_Of_Units)):
            print(self.List_Of_Units[i])

    def add_unit(self, unit):
        self.List_Of_Units.append(unit)

    def remove_unit(self, unit):
        self.List_Of_Units.remove(unit)
