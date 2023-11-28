import random

doors = ['1', '2', '3']
doors1 = doors.copy() #I am using this list to return the door that does not contain the prize and user
                    #choice later in another function defined later
                    
#Define all the functions that I will use
random.seed(input("Enter a seed: "))

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
    global doors1 #Making doors1 global to be able to modify it
    if doorA != doorB: #If parameters are not equal, I remove both parameters from the list
        doors1.remove(doorA)
        doors1.remove(doorB)
    else: #If they are equal, I only remove one parameter and it will automatically remove the second
        #parameter from list
        doors1.remove(doorA)
    return doors1[0] #Returning the first value of doors1, if the if statement ran, it will be the first
#one anywayd, if the else statement ran, it will return the first value of the list of two values

def SwitchDoorFrom(doorA, doorB):
    global doors1 #Making doors1 global to be able to modify it
    if doorA != doorB:
        return doorB
    else:
        return doors1[-1]
    
def EndGame():
    return -1


def main():
    #Calling the menu function, but menu does not return anything, it just prints the menu to the user
    while True:
        menu()
            
        #Getting user choice based on the menu above
        user_choice = input("Enter an option: ")

        #Checking if the user entered a valid choice
        while user_choice not in ("123"):
            print("Please enter a valid choice")
            print()
            menu()
            user_choice = input("Enter an option: ")
            
        #Run the Live Game
        if user_choice == '1':
            random.seed()        
            prizeDoor = random.choice(doors)
            
            #Calling function LiveGame which returns the overview of the game
            LiveGame()
            
            door_choice = input("Your choice: ")
            
            #Checking if the user entered a valid choice
            while door_choice not in ('123'):
                print("Please enter a valid door number")
                print()
                door_choice = input("Your choice: (1, 2, or 3): ")
            print()
            
            #Giving the user the chance to switch door by revealing one of them
            print(f"""Before I show you what is behind door {door_choice},
    I'd like to show you that behind door {OtherDoorFrom(door_choice, prizeDoor)} is laundry detergent,
    now you have the chance to switch. 
    Would you like to switch from door {door_choice} to door {SwitchDoorFrom(door_choice, prizeDoor)}?        
    """)
            stick_choice = input("Enter 'y' if you decide to switch, otherwise enter 'n': ").lower()
            
            #Checking if user entered a valid choice
            while stick_choice not in ('yn'):
                print("I did not understand that. Please try again.")
                print()
                stick_choice = input("Enter 'y' if you decide to switch, otherwise enter 'n': ").lower()
            
            #If the user decided to switch his door choice
            if stick_choice == 'y':
                new_choice = SwitchDoorFrom(door_choice, prizeDoor) #Assigning the new user choice
                if new_choice == prizeDoor:
                    print("Ganaste puta")
                else:
                    print("Perdiste zorra")
            
            #If the user did not decide to switch his door choice
            elif stick_choice == 'n':
                if user_choice == prizeDoor: #User choice stays the same since he did not want to switch
                    print("Ganaste puta")
                else:
                    print("Perdiste zorra")
                
                
                
        elif user_choice == '2':
            SimulatedGames()
        
        else:
            EndGame()
            
        if user_choice == '3':
            break
        
                    
main()

#TOMORROW: I need to make the messages to the user nicer and better looking.

#I will work on getting the SimulatedGames() function working and adding variables
#to keep track of if the user decided to switch between doors or not and the win rate