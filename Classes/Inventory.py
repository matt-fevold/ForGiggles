class Inventory:
    def __init__(self):
        self.inventory_list = []  # empty list to start with

    def view_inventory(self):
        print("Inventory:" + "\n-----------")
        for i in range(len(self.inventory_list)):
            print("(" + str(i) + ")" + self.inventory_list[i])
        print("----------")

    def view_inventory_item(self, index):
        if index <= len(self.inventory_list):
            return self.inventory_list[index]
        else:
            print("Not a valid input")
            return None

    def add_to_inventory(self, item):
        self.inventory_list.append(item)

    # return true if the item is there and successfully removed.
    def remove_from_inventory(self, item):
        if self.inventory_list.__contains__(item):
            self.inventory_list.remove(item)
            return True
        else:
            return False
