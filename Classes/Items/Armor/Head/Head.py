from Classes.Items.Armor import Armor


class Head(Armor.Armor):
    def __init__(self, name, armor_value):
        super().__init__(name, "Head", armor_value)

    def __str__(self):
        return super().__str__()
