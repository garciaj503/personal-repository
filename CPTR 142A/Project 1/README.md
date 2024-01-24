# CPTR 142: Project #1
## Problem Overview
For this project you will create a simulation of the "Left Center Right" (LCR) dice game.

> **LCR**, or **Left Center Right**, is a dice game for three or more players, published by George & Company LLC in 1992. It is entirely a game of chance. The players make no decisions of any kind, even as to wagering.
> 
> ### Gameplay
> 
> Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.
>
> If a player has fewer than three chips left, they are still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The player who does not receive chips after two passes is out of the game. The winner is the last player with chips left.

-- From [wikipedia.org](https://en.wikipedia.org/wiki/LCR_(dice_game)) (since deleted)

## Solution Specifications
Your solution should strive to meet the standards specified below as they form the basis on which it will be graded.

0. Your program will simulate the actions by all players in an entire game, from start to finish, and report the game's outcome to the console. 
    1. Ask the user for the number and names of the players, the number of chips all players get to start, and a seed for the random number generator `random.seed()`.
0. Your program must be divided into classes and functions which perform well-defined and logical sub-tasks for the problem. You may check with your professor, a tutor at the SDC, or another student about your choice of functions and the parameters and/or return types that they will require.
0. Define a Dice class with appropriate public function(s). Use `randint()` to simulate a dice roll with six outcomes, and convert the outcome to left, center, right, or dot. You can have multiple dice or use one dice multiple times; the result should be the same.
    1. Put each class definition (with its associated methods) in a separate file.
    1. Create a file with unit tests for your classes, verifying that their functionality is correct.
0. Create a file to simulate the game. Give each player a turn (zero to three rolls with appropriate transfers of chips) and move on to the next player if the game is not over. When the game ends, report which player won (by name) and how many turns it took to finish the game (a turn is when a player roles or passes).

## Hints

The following suggestions should save you some time and frustration.

* Make sure that each of your functions really encapsulates one particular well-defined task.  If your function is more than 10-15 lines long, think carefully about if it makes sense to break it up into separate subfunctions.
* Use descriptive function and variable names.  A function name like ``roll_dice`` is far more descriptive than ``rd`` and similarly for variables.
* For each function, include a comment that explains the input and output of the function and the task that it is responsible for completing.
* Think carefully about your code before you write it.  It is worth programming a little slower in order to make sure that the code you write is clear, simple, and easy to read and modify.
* Start writing your functions one-by-one and test them as you write them.  Make sure that each function behaves correctly before moving on to the next function.  This will potentially save you a huge amount of time and frustration when debugging.
* The expected output is quite simple, just a player's name and the number of turns that player took to win. You aren't required to report each roll or its result, though some output (perhaps to a file) might be helpful for debugging. 
* The use of a seed allows us to have repeatable "pseudo-random" sequences. Check back for sample results. 

## Code Review

See the Code Review Rubric document for expectations.