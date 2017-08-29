from Classes.Actions import MenuAction
from Classes import Character
# for actions that modify self


class ViewSelf(MenuAction):
    def __init__(self, character):
        super().__init__("View Self", "Inspect your character")
        self.character = character

    def view_self(self):
        self.character.print_self()


# for editing attributes(level up?) still not super sure what to do here
class EditSelf(MenuAction):
    pass
