from Classes.Items.Armor import *


class Equipment:
    def __init__(self, head=None, torso=None, legs=None, feet=None, hands=None, weapon=None, shield=None):
        self.head = head  # object that is a head piece
        self.torso = torso  # object that is a torso piece
        self.legs = legs  # ect..
        self.feet = feet
        self.hands = hands
        self.weapon = weapon
        self.shield = shield

    def print_equipment(self):
        print("Head: " + self.head.name)
        print("Torso: ")  # TODO this section
        print("Legs: ")
        print("Feet: ")
        print("Hands: ")
        print("Weapon: ")
        print("Shield: ")

    def equip_head(self, head_item):
        if head_item.armor_type not in ["Head"]:
            return False
        else:
            self.head = head_item
            return True

    def unequip_head(self):
        if self.head is not None:
            self.head = None
            return True
        else:
            print("No item to remove from head")
            return False

    # TODO need to equip/unequip for each item or find a better way to do this.
