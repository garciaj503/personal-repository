import random

#Define alll the functions that I will use

def game_seed(user_seed):
    return -1

def menu():
    print("""Menu:
  1) Play a live game
  2) Simulate multiple games
  3) Quit""")

def LiveGame():
    return -1

def SimulatedGames():
    return -1

def OtherDoorFrom():
    return -1

def EndGame():
    return -1


def main():
    #FIXME
    user_seed = input("Please enter a seed to start the game: ")
    game_seed(user_seed)
    
    print()
    
    #Calling the menu function, but menu does not return anything, it just prints the menu to the user
    menu()
        
    #Getting user's choice based on the menu above
    user_choice = input("Enter an option: ")
    
    #Checking if the user entered a valid choice
    while user_choice not in ("123"):
        print("Please enter a valid choice")
        print()
        menu()
        user_choice = input("Enter an option: ")
                
main()