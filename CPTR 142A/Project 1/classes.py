import random

class Dice:
    def get_side(self):
        random_side = random.randint(1, 6)
        if random_side in [1, 2, 3]:
            return "."
        elif random_side == 4:
            return "L"
        elif random_side == 5:
            return "R"
        elif random_side == 6:
            return "C"

class Player(Dice):
    def __init__(self, player_name, tokens):
        self.player_name = player_name
        self.tokens = tokens
        self.turns = 0
        self.turns_skipped = 0

    def roll_dice(self):
        dice_outcome = []
        if self.tokens > 3:
            for i in range(3):
                dice_outcome.append(Dice.get_side(self))
            return dice_outcome
        elif self.tokens <= 3:
            for i in range(self.tokens):
                dice_outcome.append(Dice.get_side(self))
            return dice_outcome

def num_checking(value):
    pass

def valod_players(value):
    pass
