#Importing classes and modules
import random
import classes

print("Welcome to the LCR game!")
seed = input("Please enter a seed to start the game: ")

random.seed(seed)

num_players = input("Please enter the number of players: ")

#Checking for a valid  numeric input
num_players = classes.numeric_num_players_checking(num_players)

#Checking if user entered at least 3 players
num_players = classes.num_players_checking(num_players)

print()

#List to store player names
player_names = []

#Asking user for player names
for i in range(num_players):
    name = input(f"Please enter the name of player {i + 1}: ")
    #Checking for valid names
    while not name.isalpha():
        print("Please enter a valid name")
        print()
        name = input(f"Please enter the name of player {i + 1}: ")
    player_names.append(name)

print()

num_tokens = input("Enter the number of tokens each player gets to start with (no less than 3): ")

#Checking for a valid  numeric input
num_tokens = classes.numeric_token_checking(num_tokens)

#Checking if user entered at least 3 tokens
num_tokens = classes.num_token_checking(num_tokens)

player_classes = [classes.Player(i, num_tokens) for i in player_names]

#Simulating the game
while any(player.tokens for player in player_classes):
    for index, object1 in enumerate(player_classes):
        sides_list = object1.roll_dice()
        object1.turns += 1

        #If the player has 0 tokens, then their turn is skipped
        if object1.tokens == 0:
            object1.turns_skipped += 1
            #Player out of the game if they haven't played for two rounds
            if object1.turns_skipped == 2:
                del player_classes[index]
            continue

        #Checking for each outcome of the dice and performing the required process
        for side in sides_list:
            if side == "L":
                object1.tokens -= 1
                player_classes[index - 1].tokens += 1
            elif side == "R":
                object1.tokens -= 1
                player_classes[(index + 1) % len(player_classes)].tokens += 1
            elif side == "C":
                object1.tokens -= 1

    if len(player_classes) == 1:
        break

print(f"The winner is {player_classes[0].player_name} and it took {player_classes[0].turns} turns to win!")