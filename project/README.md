# Tic Tac Toe game
#### Video Demo:  https://youtu.be/4FFyeg8Lnpc
#### Description:
This project is a working model of the Tic Tac Toe game in Python. The game allows a player and machine to take turns marking spaces on a 3x3 grid, aiming to get three of their symbols (either 'X' for user or 'O' for machine) in a row, column, or diagonal.

### Files:
- **project.py**: This file contains the main code for the Tic Tac Toe game. It includes functions for displaying the game board, determining the starting player, handling user and machine moves, checking for a winner, and running the game loop.

- **test_project.py**: This file contains unit tests for the functions in `project.py`. It checks the three main function user_move, machine_move and check_winner.

### Design Choices:
- **User Interface**: The game interface is kept simple, with the game board displayed in the console. Players are prompted to enter their moves by selecting a number corresponding to the position on the board which is constantly displayed with updated marks so that the user can see each move made by them and the machine and the free space.

- **Player Representation**: Players are represented by 'X' and 'O' symbols is used by machine, and the board is represented by a list of strings where each element corresponds to a position on the grid.

- **Randomized Starting Player**: The starting player is chosen randomly at the beginning of each game to ensure fairness.

- **Machine Move Logic**: The machine move logic is implemented to make the game challenging for the player. It tries to block the player from winning while also aiming to win itself. If no immediate winning or blocking move is available, it prioritizes side positions first then diagnol and finally  if none available marks in random free spot.

### Project Goals:
The primary goal of this project is to design and implement the Tic Tac Toe game in Python. Ensuring that the user can play without any hitches.

### Future Improvements:
- **Improved AI**: Enhance the machine move logic to create a more challenging opponent for the player, possibly implementing a more sophisticated algorithm using machine learning.
- **GUI Implementation**: Develop a graphical user interface (GUI) for the game to enhance the user experience and make it more visually appealing.
