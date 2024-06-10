import random

def display_board(board):
    print("Tic Tac Toe")
    print("------------")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        print("---------")

def player_starts():
    return random.randint(1, 2)

def machine_move(board):
    # machine move logic
    if '5' in board:
        board[4] = 'O'
    else:
        for i in range(1, 10):
            if board[i - 1] not in ['X', 'O']:
                board[i - 1] = 'O'
                if check_winner(board) == 'Machine':
                    return
                board[i - 1] = i

        for i in range(1, 10):
            if board[i - 1] not in ['X', 'O']:
                board[i - 1] = 'X'
                if check_winner(board) == 'User':
                    board[i - 1] = 'O'
                    return
                board[i - 1] = i

        side_pos = [2, 4, 6, 8]
        for pos in side_pos:
            if board[pos - 1] not in ['X', 'O']:
                board[pos - 1] = 'O'
                return

        diagonal_pos = [1, 3, 7, 9]
        for pos in diagonal_pos:
            if board[pos - 1] not in ['X', 'O']:
                board[pos - 1] = 'O'
                return

        while True:
            random_spot = random.randint(0, 8)
            if board[random_spot] not in ['X', 'O']:
                board[random_spot] = 'O'
                return

def user_move(board):
    #user move.
    while True:
            try:
                position = int(input("Enter a number (1-9): "))
                if position < 1 or position > 9:
                    print("Please enter a value within 1-9.")
                    continue
                if board[position - 1] in ['X', 'O']:
                    print("That position is already marked choose another.")
                    continue
                board[position - 1] = 'X'
                break
            except ValueError:
                print("Please enter a valid integer.")

def check_winner(board):
    #check row
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == 'X':
            return "User"
        elif board[i] == board[i+1] == board[i+2] == 'O':
            return "Machine"

    #check column
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == 'X':
            return "User"
        elif board[i] == board[i+3] == board[i+6] == 'O':
            return "Machine"

    #check diagonal
    if board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
        return "User"
    elif board[0] == board[4] == board[8] == 'O' or board[2] == board[4] == board[6] == 'O':
        return "Machine"

    #if no winner found return none
    return None


def main():
    # display the board
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(board)

    # who starts first
    player = player_starts()
    if player == 1:
        print("Machine starts first")
    else:
        print("User starts first")

    # game loop
    while True:
        # check if there is a winner
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break

        # machine turn
        if player == 1:
            machine_move(board)
            display_board(board)
            player = 2
        # user turn
        else:
            user_move(board)
            display_board(board)
            player = 1

        # check for draw
        if all(cell in ['X','O'] for cell in board):
            winner = check_winner(board)
            if winner:
                print(f"{winner} wins!")
                break
            else:
                print("It is a draw")
                break

if __name__ == "__main__":
    main()
