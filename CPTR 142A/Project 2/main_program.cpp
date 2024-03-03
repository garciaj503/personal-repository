/* This is the main program
functions are inherited from headers.h file which contains
the headers of all the functions defined in functions.cpp
*/

#include "functions.h"
#include <cctype>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

int main() {
  char userChoice;
  int seed;

  // Getting seed number from user input
  do {
    std::cout << "Enter a seed number: ";
    if (!(std::cin >> seed)) {
      std::cout << "Invalid input. Please enter an integer." << std::endl;
      std::cin.clear(); // clear the error state
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    } else {
      break;
    }
  } while (true);

  std::srand(seed);

  std::cout << std::endl;

  while (true) {
    userChoice = menu();

    if (userChoice == 1) {
      LiveGame();
    }

    else if (userChoice == 2) {
      simulatedGame();
    }

    else {
      endGame();
      break;
    }
  }

  return 0;
}