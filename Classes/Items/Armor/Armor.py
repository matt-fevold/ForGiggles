from Classes.Items import Item


class Armor(Item.Item):
    def __init__(self, name, armor_type, armor_value):
        super().__init__(name)
        self.armor_type = armor_type
        self.armor_value = armor_value

    def __str__(self):
        return super().__str__() + "\nArmor Type: " + self.armor_type + "\nArmor Value: " + str(self.armor_value)