import random

doors = ['1', '2', '3']
doors1 = doors.copy() #I am using this list to return the door that does not contain the prize and user
                    #choice later in another function defined later
                    
#Define all the functions that I will use
random.seed(input("Enter a seed: ")) #This feels kinda uselesss

def menu(): #Overview of the program
    print("""Menu:
  1) Play a live game
  2) Simulate multiple games
  3) Exit""")

def LiveGame(): #Overview of the simulation
    print("""
There are three doors, each contains a prize
behind one door there is $10,000 hidden,
behind the other two there is dishwasher detergent.
Which door will you choose: 1, 2, or 3?          
""")

def SimulatedGames():
    simulations = input('How many times should the game be simulated? ')
    
    #Checking if user entered a valid choice
    while simulations not in ('0123456789'):
        print("Please enter a valid number of simulations")
        print()
        simulations = input('How many times should the game be simulated? ')
    return simulations

def OtherDoorFrom(doorA, doorB, total_doors):
    total_doors = [int(x) for x in total_doors]
    remaining_doors = [door for door in range(1, total_doors + 1) if door != doorA and door != doorB]
    return str(remaining_doors[0])

def SwitchDoorFrom(doorA, doorB, total_doors):
    total_doors = [int(x) for x in total_doors]
    remaining_doors = [door for door in range(1, total_doors + 1) if door != doorA and door != doorB]
    return str(remaining_doors[0])

    
def EndGame():
    pass

def main():
    #Calling the menu function, but menu does not return anything, it just prints the menu to the user
    while True:
        menu()
        #Getting user choice based on the menu above
        user_choice = input("Please select what you would like to do: ")
        
        #Checking if the user entered a valid choice
        while user_choice not in ("123"):
            print("Hey bro, it is not that hard, just select 1, 2, or 3: ")
            print()
            menu()
            user_choice = input("Your choice: ")

        if user_choice == '1':
            #Run the Live Game
            # random.seed()        
            prizeDoor = random.choice(doors)
            
            #Calling function LiveGame which returns the overview of the game
            LiveGame()
            
            door_choice = input("Your choice: (1, 2, or 3): ")
            
            #Checking if the user entered a valid choice
            while door_choice not in ('123'):
                print()
                door_choice = input("C'mon bro, choose a door, 1, 2, or 3? ")
                
            print()
            
            #Giving the user the chance to switch door by revealing one of them
            print(f"""Ok let's calm down a bit. I want to tell you that behind door {OtherDoorFrom(door_choice, prizeDoor, doors)},
I have hidden laundry detergent, and you chose door {door_choice}.
Your choice might be right and win $10,000, but who knows what could happen. 
So, I will give you the chance to switch from door {door_choice} to door {SwitchDoorFrom(door_choice, prizeDoor, doors)}
Do you accept the deal?        
""")
            switch_choice = input("Enter 'y' if you do, otherwise enter 'n': ").lower()
            
            #Checking if user entered a valid choice
            while switch_choice not in ('yn'):
                print()
                switch_choice = input(("Bro it is not that deep. Just say 'y' if you want to switch doors, otherwise, say 'n'. ")).lower()
            
            #If the user decided to switch his door choice
            if switch_choice == 'y':
                new_choice = SwitchDoorFrom(door_choice, prizeDoor) #Assigning the new user choice
                if new_choice == prizeDoor:
                    print("You were wise by switching doors. You just won $10,000. Congratulations!")
                    print()
                else:
                    print(f"Well, that's too bad. The prize was behind door {prizeDoor}")
                    print()
            
            #If the user did not decide to switch his door choice
            elif switch_choice == 'n':
                if user_choice == prizeDoor: #User choice stays the same since he did not want to switch
                    print("You were wise by not switching doors. You just won $10,000. Congratulations!")
                    print()
                else:
                    print(f"Well, that's too bad. The prize was behind {prizeDoor}")
                    print()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        elif user_choice == '2':
            random.seed()
            switch_options = 'yn'
            print()
            simulations = SimulatedGames()
            for i in range(int(simulations)):
                prizeDoor = random.choice(doors) #Prize is randomly hidden
                userDoor = random.choice(doors) #User choice is randomly selected
                DoorToReveal = OtherDoorFrom(userDoor, prizeDoor)
                DoorToSwitch = SwitchDoorFrom(userDoor, prizeDoor)
                SwitchChoice = random.choice(switch_options)
                if SwitchChoice == 'y':
                    userDoor = DoorToSwitch
                    if userDoor == prizeDoor:
                        print('User switched and won')
                    else:
                        print('User switched and lost')
                elif SwitchChoice == 'n':
                    if userDoor == prizeDoor:
                        print("User did not switch and won")
                    else:
                        print("User did not switch and lost")
                        
            print(f'{simulations} done. Results will display at the end of the game')
                
                
            
        elif user_choice == '3':
            EndGame()
            break
        
                    
main()

#I will work on getting the SimulatedGames() function working and adding variables
#to keep track of if the user decided to switch between doors or not, and the win rate

#FOR SIMULATEDGAMES()FUNCTION: I need to use a foor loop to iterate over the amount of times the user wants to iterate over the
#game