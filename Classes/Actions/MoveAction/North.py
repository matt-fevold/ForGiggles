from Classes.Actions import Action


class North(Action.MoveAction):
    def __init__(self):
        super().__init__("North", "Move up 1 space")
