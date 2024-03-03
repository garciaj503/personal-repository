"""
Project III:  A game show simulation

File Name:   gameShow.py
Name:        Jaime Garcia
Course:      CPTR 141
"""
import random

doors = ["1", "2", "3"]
doors1 = (
    doors.copy()
)  # I am using this list to return the door that does not contain the prize and user
# choice later in another function defined later

# Initializing variables to keep track of the win/loss ratio
not_switch_games = 0
switch_games = 0
not_switch_wins = 0
switch_wins = 0

random.seed(
    input("Enter a seed: ")
)  # This feels kinda useless but we'll leave it there


# Define all the functions that I will use
def menu():  # Overview of the program
    print(
        """Menu:
  1) Play a live game
  2) Simulate multiple games
  3) Exit"""
    )


def LiveGame():  # Overview of the simulation
    print(
        """
There are three doors, each contains a prize
behind one door there is a Macbook Pro with an M3 chip,
behind the other two you will find the cases for a Macbook Pro.
Which door will you choose: 1, 2, or 3?          
"""
    )


def SimulatedGames():
    print(
        """Welcome to the simulated version of the game.
Here, the machine will do everything for you"""
    )
    simulations = input("How many times would you wish to simulate this game? ")

    # Checking if user entered a valid choice
    while not simulations.isdigit():
        print("Please enter a valid number of simulations")
        print()
        simulations = input("How many times would you wish to simulate this game? ")
    return simulations


def OtherDoorFrom(doorA, doorB):
    doors2 = doors1[
        :
    ]  # Creating a copy of doors1 to create a new set of doors each time
    if (
        doorA != doorB
    ):  # If parameters are not equal, I remove both parameters from the list
        doors2.remove(doorA)
        doors2.remove(doorB)
    else:  # If they are equal, I remote either parameter, it does not matter which
        doors2.remove(doorA)
    return doors2[
        0
    ]  # Returning the first value of doors1, in one case the list will only have one value.


def SwitchDoorFrom(doorA, doorB):
    doors2 = doors1[
        :
    ]  # Creating a copy of doors1 to create a new set of doors each time
    if doorA != doorB:
        doors2.remove(doorA)
        return doorB
    else:
        doors2.remove(doorA)
        return doors2[-1]


def EndGame():
    def win_rate(x, y):
        if y == 0:
            return f"{0:.1f}%"
        else:
            if y > 0:
                return f"{(x / y)*100:.1f}%"

    total_games = switch_games + not_switch_games
    total_wins = switch_wins + not_switch_wins
    switch_win_rate = win_rate(switch_wins, switch_games)
    not_switch_win_rate = win_rate(not_switch_wins, not_switch_games)
    total_win_rate = win_rate(total_wins, total_games)
    print(f'{"Strategy":^16}|{"Games":^16}|{"Wins":^16}|{"Win Rate":^16}')
    print(f"{'-' * 64}")
    print(f'{"Switch":^16}|{switch_games:^16}|{switch_wins:^16}|{switch_win_rate:^16}')
    print(
        f'{"Do not switch":^16}|{not_switch_games:^16}|{not_switch_wins:^16}|{not_switch_win_rate:^16}'
    )
    print(f"{'-' * 64}")
    print(f'{"Total":^16}|{total_games:^16}|{total_wins:^16}|{total_win_rate:^16}')


def main():
    # Calling the menu function, but menu does not return anything, it just prints the menu to the user
    while True:
        menu()
        # Getting user choice based on the menu above
        user_choice = input("Please select what you would like to do: ")

        # Checking if the user entered a valid choice
        while user_choice not in ("123"):
            print("Hey bro, it is not that hard, just select 1, 2, or 3: ")
            print()
            menu()
            user_choice = input("Your choice: ")

        if user_choice == "1":
            # Run the Live Game
            random.seed()
            prizeDoor = random.choice(doors)

            # Calling function LiveGame which returns the overview of the game
            LiveGame()

            door_choice = input("Your choice: (1, 2, or 3): ")

            # Checking if the user entered a valid choice
            while door_choice not in ["1", "2", "3"]:
                print()
                door_choice = input("C'mon bro, just choose a door, 1, 2, or 3? ")

            print()

            # Giving the user the chance to switch door by revealing one of them
            print(
                f"""Ok let's calm down a bit. I want to tell you that behind door {OtherDoorFrom(door_choice, prizeDoor)},
there's one of the two cases for a Macbook, and you chose door {door_choice}.
Your choice might be right and win the latest Macbook Pro, but who knows what could happen. 
So, I will give you the chance to switch from door {door_choice} to door {SwitchDoorFrom(door_choice, prizeDoor)}
Do you accept the deal?        
"""
            )
            switch_choice = input("Enter 'y' if you do, otherwise enter 'n': ").lower()

            # Checking if user entered a valid choice
            while switch_choice not in ["y", "n"]:
                print()
                switch_choice = input(
                    (
                        "Bro it is not that deep. Just say 'y' if you want to switch doors, otherwise, say 'n'. "
                    )
                ).lower()

            # If the user decided to switch his door choice
            if switch_choice == "y":
                global switch_games
                global switch_wins
                switch_games += 1
                new_choice = SwitchDoorFrom(
                    door_choice, prizeDoor
                )  # Assigning the new user choice
                if new_choice == prizeDoor:
                    switch_wins += 1
                    print(
                        "You were wise by switching doors. You just won a Macbook Pro! Congratulations!"
                    )
                    print()
                else:
                    print(
                        "Well, you won the case, you just need the Macbook now. Good luck next time!"
                    )
                    print()

            # If the user did not decide to switch his door choice
            elif switch_choice == "n":
                global not_switch_games
                global not_switch_wins
                not_switch_games += 1
                if (
                    door_choice == prizeDoor
                ):  # User choice stays the same since he did not want to switch
                    not_switch_wins += 1
                    print(
                        "You were wise by switching doors. You just won a Macbook Pro! Congratulations!"
                    )
                    print()
                else:
                    print(
                        "Well, you won the case, you just need the Macbook now. Good luck next time!"
                    )
                    print()

        elif user_choice == "2":
            # Play the simulated games
            random.seed()
            switch_options = "yn"
            print()
            simulations = SimulatedGames()  # Calling the overview of Simulated Games
            for i in range(int(simulations)):
                prizeDoor = random.choice(doors)  # Prize is randomly hidden
                userDoor = random.choice(doors)  # User choice is randomly selected
                DoorToSwitch = SwitchDoorFrom(userDoor, prizeDoor)
                SwitchChoice = random.choice(
                    switch_options
                )  # User switch choice is randomly selected
                if SwitchChoice == "y":
                    switch_games += 1
                    userDoor = DoorToSwitch
                    if userDoor == prizeDoor:
                        switch_wins += 1

                elif SwitchChoice == "n":
                    not_switch_games += 1
                    if userDoor == prizeDoor:
                        not_switch_wins += 1

            print(
                f"{simulations} simulations done. Results will display at the end of the game"
            )
            print()

        elif user_choice == "3":  # User decides to stop playing
            EndGame()  # Displaying the stats
            print()
            print("Thanks for playing!")
            break


main()
