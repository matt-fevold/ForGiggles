from Classes.Actions import Action


class East(Action.MoveAction):
    def __init__(self):
        super().__init__("East", "Move right 1 space")

    def move_east(self, character):
        pass
