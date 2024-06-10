from project import user_move, machine_move, check_winner
from unittest.mock import patch


#test machine_move function
def test_machine_move():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    machine_move(board)
    assert board == ['1', '2', '3', '4', 'O', '6', '7', '8', '9']

#test check_winner function
def test_check_winner():
    board_user_win = ['X', 'X', 'X', '4', '5', '6', '7', '8', '9']
    assert check_winner(board_user_win) == 'User'

    board_machine_win = ['O', 'O', 'O', '4', '5', '6', '7', '8', '9']
    assert check_winner(board_machine_win) == 'Machine'

#test user move function
@patch('builtins.input', side_effect=['10'])
def test_user_move(mock_input):
    board = ['1', '2', '3', '4', 'X', '6', '7', '8', '9']
    try:
        user_move(board)
    except ValueError:
        assert True
    except StopIteration:
        pass
    else:
        assert False
