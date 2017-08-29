from Classes.Actions import Action


class South(Action.MoveAction):
    def __init__(self):
        super().__init__("South", "Move down 1 space")
