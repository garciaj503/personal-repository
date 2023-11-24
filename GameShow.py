import random

seed = random.seed(int(input("Please enter a seed to start playing: ")))
print()

doors = ['1', '2', '3']
prize = random.choice(doors)

def LiveGame():
    print()
    print("""Welcome to tonight's show! I'm so glad you have joined us
Tonight's game is the following:
There are three doors, and each of them is concealing a price.
Two of those have laundry detergent behind them, but one of them has $10,000.
Which door will you choose? 1, 2, or 3?
""")
    
    user_choice = input("Choose 1, 2, or 3: ")
    if user_choice == prize:
        print("Congratulations! You just won $10,000")
    else:
        for i in doors:
            if i != prize and i != user_choice:
                door_to_reveal =  i
        print(f"Before I show you what's behind door {user_choice},") 
        print(f"I would like to show that behind door {door_to_reveal} is laundry detergent.")
        print(f"It is not too late to change doors.") 
        print(f"Would you like to change from door {user_choice} to {i}?")
                
    





def SimulatedGames():
    return -1

def StatisticsTable():
    return -1

def main():
    print('''What would you like to do?
    1) Play a Live Game
    2) Simulate Game
    3) Quit
    ''')
    
    user_choice = input("Your choice: ")
    
    if user_choice == "1":
        LiveGame()
        
    elif user_choice == "2":
        SimulatedGames()
        
    else:
        StatisticsTable()

main()



    
 
