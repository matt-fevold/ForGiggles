# intended to be used by Characters (aka leaders) on the main world screen
class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class MoveAction(Action):
    def __init__(self, direction, description):
        super().__init__(direction, description)


class MenuAction(Action):
    def __init__(self, name, description):
        super().__init__(name, description)

