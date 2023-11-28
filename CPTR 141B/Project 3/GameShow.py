import random
doors = ['1', '2', '3']
doors1 = doors.copy()

#Define all the functions that I will use
def game_seed(user_seed):
    return random.seed(user_seed)

def menu():
    print("""Menu:
  1) Play a live game
  2) Simulate multiple games
  3) Quit""")

def LiveGame():
    print("""
There are three doors, each contains a prize
behind one door there is $10,000 hidden,
behind the other two there is dishwasher detergent.
Which door will you choose: 1, 2, or 3?          
""")

def SimulatedGames():
    return -1

def OtherDoorFrom(UserDoor, PrizeDoor):
    if UserDoor != PrizeDoor:
        doors1.remove(UserDoor)
        doors1.remove(PrizeDoor)
    else:
        doors1.remove(UserDoor)
    left_door = ""
    for string in doors1:
        left_door += string
    return left_door
    

def EndGame():
    return -1







def main():
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
        
    if user_choice == '1':        
        prizeDoor = random.choice(doors)
        
        #Calling function LiveGame which returns the overview of the game
        LiveGame()
        
        door_choice = input("Your choice: ")
        
        #Checking if the user entered a valid choice
        while door_choice not in ('123'):
            print("Please enter a valid door number")
            print()
            door_choice = input("Your choice: ")
        print()
                
        left_door = OtherDoorFrom(door_choice, prizeDoor)
        
        #Giving the user the chance to switch door by revealing one of them
        print(f"""Before I show you what is behind door {door_choice},
I'd like to show you that behind door {left_door} is laundry detergent,
now you have the chance to switch                 
""")
               
    elif user_choice == '2':
        print(SimulatedGames())
    
    else:
        EndGame()
                    
main()