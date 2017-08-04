class Fight:
    def __init__(self, main_character, enemy_character):
        self.main_character = main_character
        self.enemy_character = enemy_character
        self.fight_over = False

    # for displaying the graphics
    def fight_screen(self):
        print("--------------------")
        print(self.main_character.name)
        print("hp: " + str(self.main_character.health))
        print("         vs         ")
        print("               " + self.enemy_character.name)
        print("               hp: " + str(self.enemy_character.health))
        print("--------------------")
