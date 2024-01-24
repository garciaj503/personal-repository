#Importing classes and modules
import random
import classes

seed = input("Please enter a seed: ")

random.seed(seed)

num_players = input("Please enter the number of players: ")

#Checking for a valid  numeric input
while not num_players.isnumeric():
    print("Please enter a valid number.")
    print()
    num_players = input("Try again: ")

num_players = int(num_players)

#Checking if user entered at least 3 players
while num_players < 3:
    print("Please enter 3 or more players")
    print()
    num_players = input("Plase enter the number of players: ")
    while not num_players.isnumeric():
        print("Please enter a valid number.")
        print()
        num_players = input("Try again: ")
    num_players = int(num_players)

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
while not num_tokens.isnumeric():
    print("Please enter a valid amount of tokens")
    print()
    num_tokens = input("Enter the number of tokens each player gets to start with (no less than 3): ")

num_tokens = int(num_tokens)

#Checking if user input is less than 3, then ask again for a number greater than or equal to 3
if num_tokens < 3:
    while num_tokens < 3:
        print("The amount of tokens has to be greater than or equal to 3.")
        print()
        num_tokens = input("Try Again: ")
        while not num_tokens.isnumeric():
            print("Please enter a valid amount of tokens")
            print()
            num_tokens = input("Enter the number of tokens each player gets to start with (no less than 3): ")
        num_tokens = int(num_tokens)

player_classes = [classes.Player(i, num_tokens) for i in player_names]

while any(player.tokens for player in player_classes):

    for index, object1 in enumerate(player_classes):
        sides_list = object1.roll_dice()
        object1.turns += 1

        if object1.tokens == 0:
            object1.turns_skipped += 1
            if object1.turns_skipped == 2:
                del player_classes[index]
            continue
        for side in sides_list:
            if side == "L":
                object1.tokens -= 1
                player_classes[index - 1].tokens += 1
            elif side == "R":
                index_last_player = len(player_classes) - 1
                object1.tokens -= 1
                if index == index_last_player:
                    player_classes[0].tokens += 1
                else:
                    player_classes[index + 1].tokens += 1
            elif side == "C":
                object1.tokens -= 1

    if len(player_classes) == 1:
        break

print(f"The winner is {player_classes[0].player_name} and it took {player_classes[0].turns} turns to win!")