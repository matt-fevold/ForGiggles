from Classes.Actions import MenuAction


class ViewInventory(MenuAction):
    def __init__(self, inventory):
        super().__init__("View Inventory", "Look at your possessions")
        self.inventory = inventory

    def view_inventory(self):
        pass


class EditInventory(MenuAction):
    pass


