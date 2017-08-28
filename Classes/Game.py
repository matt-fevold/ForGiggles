class Game:
    def __init__(self, turn):
        self.game_turn_counter = 0
        self.current_turn = turn

    def next_turn(self, turn):
        self.game_turn_counter += 1
        self.current_turn = turn

    def get_turn_number(self):
        return self.game_turn_counter

    def get_turn(self):
        pass

