#include <iostream>
#include <vector>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cctype>


//Template of doors to be used
std::vector<int> doors {1, 2, 3};

//Variables to keep track of win/loss ratio
int not_switch_games = 0;
int switch_games = 0;
int not_switch_wins = 0;
int switch_wins = 0;


//Function to check the user choice. Has to be 1, 2, or 3.
int choiceChecking (std::string userChoice) {
  int return_Value;
  std::cout << std::endl;
  while (userChoice.at(0) != '1' && userChoice.at(0) != '2' && userChoice.at(0) != '3') {
    std::cout << "Hey bro, it is not that hard, just select 1, 2, or 3: ";
    std::cin >> userChoice;
  }
  return_Value = userChoice.at(0) - '0';
  return return_Value;
}


//Function to check the user switch choice. The user can enter 'yes' or 'no, the first letter will be taken into account.
char swtichChoiceChecking (std::string switchChoice) {
  std::cout << std::endl;
  while (tolower(switchChoice.at(0)) != 'y' && tolower(switchChoice.at(0)) != 'n') {
    std::cout << "I did not understant that. Please enter 'y' for yes or 'n' for no: ";
    std::cin >> switchChoice;
  }
  return tolower(switchChoice.at(0));
}


//Function to return a door that does not have the prize and is not the user's selection
int OtherDoorFrom(int doorA, int doorB){
  std::vector<int> copyDoors = doors;

  if (doorA != doorB) {
    for (int i = 0; i < copyDoors.size(); ++i) {
      if (copyDoors.at(i) == doorA || copyDoors.at(i) == doorB) {
        copyDoors.erase(copyDoors.begin() + i);
        --i;
      }
    }
  } else {
      for (int i = 0; i < copyDoors.size(); ++i) {
        if (copyDoors.at(i) == doorA) {
          copyDoors.erase(copyDoors.begin() + i);
          break;
        }
      }
  }
  return copyDoors.front();
}

//Function to return a door to which the user can switch to
int SwitchDoorTo(int doorA, int doorB) {
  std::vector<int> copyDoors = doors;
  
  if (doorA != doorB) {
    for (int i = 0; i < copyDoors.size(); ++i) {
      if (copyDoors.at(i) == doorA) {
        copyDoors.erase(copyDoors.begin() + i);
        return doorB;
      }
    }
    
} else {
    for (int i = 0; i < copyDoors.size(); ++i) {
      if (copyDoors.at(i) == doorA) {
        copyDoors.erase(copyDoors.begin() + i);
        return copyDoors.back();
    }
        }
    }
    return 0;
}


//Displays menu and returns option chosen by user
int menu() {
  //fixed means that the value has been checked for correct input

  std::string get_User_Option;
  int fixed_User_Option;

  std::cout << "Menu:" << std::endl;
  std::cout << "  1) Play a live game" << std::endl;
  std::cout << "  2) Simulate multiple games" << std::endl;
  std::cout << "  3) Exit" << std::endl;
  std::cout << "Please select what you would like to do: ";
  std::cin >> get_User_Option;

  fixed_User_Option = choiceChecking(get_User_Option);

  return fixed_User_Option;
}


//Function that runs the live game
void LiveGame() {
  //fixed means that the value has been checked for correct input

  std::string get_User_Door;
  int fixed_User_Door;
  std::string switch_Choice;
  char fixed_Switch_Choice;
  int prize_Door;
  int new_User_Door;

  std::cout << std::endl;
  std::cout << "There are three doors, each contains a prize" << std::endl;
  std::cout << "behind one door there is a Macbook Pro with an M3 chip,"
            << std::endl;
  std::cout << "behind the other two you will find the cases for a Macbook Pro."
            << std::endl;
  std::cout << "Which door will you choose: 1, 2, or 3?" << std::endl;
  std::cout << "Your choice: (1, 2 or 3): ";
  std::cin >> get_User_Door;

  fixed_User_Door = choiceChecking(get_User_Door);

  //Hiding prize
  prize_Door = (rand() % 3) + 1;

  std::cout << std::endl;
  std::cout << "Ok let's calm down a bit. I want to tell you that behind door " << OtherDoorFrom(fixed_User_Door, prize_Door) << std::endl;
  std::cout << "there's one of the two cases for a Macbook, and you chose " << fixed_User_Door << "." << std::endl;
  std::cout << "Your choice might be right and you could win the latest Macbook pro, but who knows what could happen." << std::endl;
  std::cout << "So, I will give you the chance to switch from door " << fixed_User_Door << " to door " << SwitchDoorTo(fixed_User_Door, prize_Door) << std::endl;
  std::cout << "Do you accept the deal? (y/n) ";
  std::cin >> switch_Choice;

  fixed_Switch_Choice = swtichChoiceChecking(switch_Choice);

  //User decided to switch
  if (fixed_Switch_Choice == 'y') {
    switch_games += 1;
    new_User_Door = SwitchDoorTo(fixed_User_Door, prize_Door);

    if (new_User_Door == prize_Door) {
      switch_wins += 1;
      std::cout << "You were wise by switching doors. You just won a Macbook Pro! Congratulations!" << std::endl;

    } else {
      std::cout << "Well, you won the case, you just need the Macbook now. Good luck next time!" << std::endl;
    }

  //User decided not to switch
  } else if (fixed_Switch_Choice == 'n') {
      not_switch_games += 1;

      if (new_User_Door == prize_Door) {
        not_switch_wins += 1;
        std::cout << "You were wise by not switching doors. You just won a Macbook Pro! Congratulations!" << std::endl;

      } else {
        std::cout << "Well, you won the case, you just need the Macbook now. Good luck next time!" << std::endl;
      }

  }
  return;
}


//Function that simulates the entire game
void simulatedGame() {
  char switch_Options[] = "yn";
  std::string simulations;
  int fixed_Simulations;
  int prize_Door;
  int user_Door;
  int new_User_Door;
  int door_To_Switch;
  char switch_Choice;

  prize_Door = (rand() % 3) + 1;

  std::cout << "Welcome to the simulated version of the game." << std::endl;
  std::cout << "Here, the machine will do everything for you." << std::endl;

  std::cout << "How many times would you wish to simulate the game? ";
  std::cin >> simulations;


  while (true) {
    bool validInput = true;
    for (int i = 0; i < simulations.size(); ++i) {
      if (!isdigit(simulations.at(i))) {
        validInput = false;
        break;
      }
    }

    if (validInput) {
      break;
  } else {
      std::cout << "Please enter a valid number: ";
      std::cin >> simulations;
    }
  }

  fixed_Simulations = std::stoi(simulations);

  for (int i = 0; i < fixed_Simulations; ++i) {
    user_Door = (rand() % 3) + 1;
    door_To_Switch = SwitchDoorTo(user_Door, prize_Door);
    switch_Choice = switch_Options[(rand() % 2)];

    if (switch_Choice == 'y') {
      switch_games += 1;
      new_User_Door = door_To_Switch;

      if (new_User_Door == prize_Door) {
        switch_wins += 1;
      }

    } else if (switch_Choice == 'n') {
      not_switch_games += 1;
      if (user_Door == prize_Door) {
        not_switch_wins += 1;
      }
    } 
  }

  std::cout << std::endl;
  std::cout << simulations << " simulations done. Results will display at the end of the game." << std::endl << std::endl;
  return;    
}


//Function to return the win rate based how many games the user played
double win_Rate(int x, int y) {
  double return_Value;
  if (y == 0) {
    return_Value = 0;
    return return_Value;
  } else {
        return_Value = (static_cast<double>(x)/y) * 100;
        return return_Value;
      }
  return 0;
}


//Function to display statistics when the user decides to stop playing
void endGame() {
  std::string line(54, '-');
  int total_Games;
  int total_Wins;
  double switch_Win_Rate;
  double not_switch_Win_Rate;
  double total_Win_Rate;

  //Computing final results
  total_Games = switch_games + not_switch_games;
  total_Wins = switch_wins + not_switch_wins;
  switch_Win_Rate = win_Rate(switch_wins, switch_games);
  not_switch_Win_Rate = win_Rate(not_switch_wins, not_switch_games);
  total_Win_Rate = win_Rate(total_Wins, total_Games);

  //Table with statistics
  std::cout << std::left << std::setw(14) << "Strategy" << std::setw(14) << "Games" << std::setw(14) << "Wins" << std::setw(14) << "Win Rate" << std::endl;
  std::cout << line << std::endl;
  std::cout << std::fixed << std::setprecision(2) << std::setw(15) << "Switch" << switch_games << std::setw(13) << "" << switch_wins << std::setw(13) << ""  << switch_Win_Rate << "%" << std::endl;
  std::cout << line << std::endl;
  std::cout << std::fixed << std::setprecision(2) << std::setw(15) << "Not Switch" << not_switch_games << std::setw(13) << "" << not_switch_wins << std::setw(13) << ""  << not_switch_Win_Rate << "%" << std::endl;
  std::cout << line << std::endl;
  std::cout << std::fixed << std::setprecision(2) << std::setw(15) << "Total" << total_Games << std::setw(13) << "" << total_Wins << std::setw(13) << ""  << total_Win_Rate << "%" << std::endl;
  return;
}

