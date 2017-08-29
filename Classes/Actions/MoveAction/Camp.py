from Classes.Actions import MoveAction


class Camp(MoveAction):
    def __init__(self):
        super().__init__("Camp", "Stay put for a turn")

    def camp(self):
        pass
