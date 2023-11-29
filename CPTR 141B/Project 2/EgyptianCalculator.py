"""
Project II:  An implementation of the so-called "Russian Peasant" or "Ancient
             Egyptian" method for multiplication.

File Name:   multiplier.py
Name:        Jaime Garcia
Course:      CPTR 141
Code Review:
"""

#Welcome to the calculator
print("Welcome to the Ancient Egyptian Calculator!")
user_choice = input("Would you like to see how it works? (yes/no) ")
print()

while user_choice[0] != 'y':
    if user_choice[0] == 'n':
        break
    user_choice = input("I did not understand that. Could you try again? ")
    print()

while user_choice[0] == 'y':
    #Asking the user for inputs
    A = input("Enter integer A: ")
    B = input("Enter integer B: ")

    # Creating lists to store the values of A and B
    A_values = []
    B_values = []

    #Checking if user inputs are negative values, using flags to keep track of negative values
    negativeA = False
    negativeB = False

    if A[0] == '-':
        A = A[1:]
        negativeA = True

    if B[0] == '-':
        B = B[1:]
        negativeB = True
        
    # Perform validation for inputs
    while not (A.isdigit() and B.isdigit()):
        print("Please enter valid integers")
        print()        
        A = input("Enter integer A: ")
        B = input("Enter integer B: ")

        #Checking if user inputs are negative values, using flags to keep track of negative values
        negativeA = False
        negativeB = False
        
        if A[0] == '-':
            A = A[1:]
            negativeA = True

        if B[0] == '-':
            B = B[1:]
            negativeB = True

    A = int(A)
    B = int(B)

    if negativeA == True:
        A *= -1
    A_values.append(A)

    if negativeB == True:
        B_values.append(-B)
    else:
        B_values.append(B)


    # Create a variable to store the result
    result = 0
    
    # Create a loop to get all the values of A and B
    print()  #Newline to separate
    print("A   B          Comments") #Header of the table
    while B >= 1:
        if B % 2 != 0:
            result += A
        if B == 1:
            break
        A *= 2
        B //= 2
        if negativeB == True:
            B_values.append(-B)
        else:
            B_values.append(B)
        A_values.append(A)

    if negativeB == True:
        B *= -1
        result *= -1

    #This is my comment section
    for c, d in zip(A_values, B_values):
        print("_______________________________________________________")
        if d % 2 != 0:
            print(f"{c}  {d} ---- Since {d} is odd, we will add {c} to our answer.")
        else:
            print(f"{c}  {d} ---- Since {d} is even, we will ignore {c}.")

    print()
    print(f"The result of {A_values[0]} x {B_values[0]} is {result}")
    
    user_choice = input("Would you like to try again? ")
    print()    
    
print('See you soon!')