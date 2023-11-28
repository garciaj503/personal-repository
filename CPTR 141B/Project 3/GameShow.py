import random
doors = ['1', '2', '3']
doors1 = doors.copy() #I am using this list to return the door that does not contain the prize and user
                    #choice later in another function defined later

#Define all the functions that I will use
def game_seed(user_seed):
    return (random.seed(user_seed))

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

def OtherDoorFrom(doorA, doorB):
    #Need to remove PrizeDoor and UserDoor from the list
    global doors1
    if doorA != doorB:
        doors1.remove(doorA)
        doors1.remove(doorB)
        
    else:
        doors1.remove(doorB)
    
    random_door = random.choice(doors1)
    return random_door
        
    
    

    
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
                
        print(prizeDoor)
        print(door_choice)
        
        #Giving the user the chance to switch door by revealing one of them
        print(f"""Before I show you what is behind door {door_choice},
I'd like to show you that behind door {OtherDoorFrom(door_choice, prizeDoor)} is laundry detergent,
now you have the chance to switch. Would you like to switch from door {door_choice} to door {doors1[0]}?           
""")
               
    elif user_choice == '2':
        SimulatedGames()
    
    else:
        EndGame()
                    
main()