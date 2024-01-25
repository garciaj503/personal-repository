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

class Player:
    def __init__(self, player_name, tokens):
        self.player_name = player_name
        self.tokens = tokens
        self.dice = Dice()
        self.turns = 0
        self.turns_skipped = 0

    def display_info(self):
        return f"The name of the player is {self.player_name} and has {self.tokens} tokens"

    def roll_dice(self):
        dice_outcome = []
        #Rolling the dice based on the number of tokens the player has
        if self.tokens > 3:
            for i in range(3):
                dice_outcome.append(self.dice.get_side())
            return dice_outcome
        elif self.tokens <= 3:
            for i in range(self.tokens):
                dice_outcome.append(self.dice.get_side())
            return dice_outcome

#FUNCTIONS
def numeric_num_players_checking(num_players):
    """
    This function checks if the number of players that the user entered is a numeric value.
    If not, ask again for a numeric value
    """
    while not num_players.isnumeric():
        print("Please enter a valid number.")
        print()
        num_players = input("Try again: ")
    return int(num_players)

def num_players_checking(num_players):
    """
    This function checks if the amount of players is less than three.
    If true, it will ask the user for a number greater than or equal to 3.
    It also calls the previous function to double-check the value 
    entered by the user.
    """
    while num_players < 3:
        print("Please enter 3 or more players")
        print()
        num_players = input("Please enter the number of players: ")
        #Checking again that the input is a number
        numeric_num_players_checking(num_players)
        num_players = int(num_players)
    return int(num_players)

def numeric_token_checking(num_tokens):
    """
    This function checks if the number of tokens entered by the user 
    is a numeric value. If not, ask again for a numeric value.
    """
    while not num_tokens.isnumeric():
        print("Please enter a valid amount of tokens")
        print()
        num_tokens = input("Enter the number of tokens each player gets to start with (no less than 3): ")
    return int(num_tokens)

def num_token_checking(num_tokens):
    """
    This function checks if the number of tokens entered by the user
    is less than three. If true, it will ask the user to enter a number
    greater than or equal to 3. It also calls the previous function
    to double-check the value entered by the user.
    """
    while num_tokens < 3:
        print("The amount of tokens has to be greater than or equal to 3.")
        print()
        num_tokens = input("Try Again: ")
        #Checks again if value entered by the user if a number
        numeric_token_checking(num_tokens)
        num_tokens = int(num_tokens)
    return int(num_tokens)