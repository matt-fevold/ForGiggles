from Classes.Actions import Action


class West(Action.MoveAction):
    def __init__(self):
        super().__init__("West", "Move west 1 space")
