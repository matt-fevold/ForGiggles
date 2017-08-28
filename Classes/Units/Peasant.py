import names

from Classes.Units import Unit
from Classes.Items.Armor.Head import LeatherHat

class Peasant(Unit.Unit):
    def __init__(self):
        super().__init__(names.get_full_name(), "Peasant", 2, 3, 4, 5)
        self.equipment.head = LeatherHat.LeatherHat()

    def print_stats(self):
        super().print_stats()
