#A game with three doors.
#Behind one door there's $10,000 dollars. Behind the other two there's diswasher detergent.
import random

def playGame(times, seed=None):
    random.seed(seed)

    numStayed = 0
    numSwitched = 0

    for _ in range(times):
        doors = [False, False, True]
        random.shuffle(doors)

        chosenDoor = random.choice([0, 1, 2])
        otherDoor = otherDoorFrom(chosenDoor, doors.index(True))

        # Host reveals the consolation prize behind one of the remaining doors
        revealedDoor = random.choice([i for i in range(3) if i != chosenDoor and i != otherDoor])

        if doors[chosenDoor]:
            numStayed += 1
        else:
            numSwitched += 1

    winRateStayed = numStayed / times
    winRateSwitched = numSwitched / times

    return winRateStayed, winRateSwitched

def otherDoorFrom(doorA, doorB):
    for i in range(3):
        if i != doorA and i != doorB:
            return i

seed = input("Enter a seed for the random number generator (leave blank for a random seed): ")
if seed == "":
    seed = random.randint(0, 1000000)

numTimes = int(input("Enter the number of times you want to play the game: "))
winRateStayed, winRateSwitched = playGame(numTimes, seed)

print(f"Win Rate for Stayed: {winRateStayed:.2f}")
print(f"Win Rate for Switched: {winRateSwitched:.2f}")