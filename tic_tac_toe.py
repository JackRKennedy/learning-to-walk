# tic tac toe

# writing a simple program to play tic tac toe
# two options of playing, one against the computer and one against another player
# will research way of implementing a minimax algorithm to make the computer unbeatable

import random

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def choose_x_or_o():
    good_input = False
    while not good_input:
        x_or_o = input("Do you want to play with X or O?").upper()
        if x_or_o in ["X", "O"]:
            good_input = True
        else:
            print("Please enter a valid response")

    if x_or_o == "X":
        user_symbol = "X"
        computer_symbol = "O"
    else:
        user_symbol = "O"
        computer_symbol = "X"
    return user_symbol, computer_symbol


def check_pick(pick):
    return pick in range(1, 10) and pick not in ["X", "O"]


def check_winner(computer_symbol, user_symbol, board):

    computer_won = False
    user_won = False
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] == computer_symbol:
            computer_won = True
        elif row[0] == row[1] == row[2] == user_symbol:
            user_won = True

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == computer_symbol:
            computer_won = True
        elif board[0][col] == board[1][col] == board[2][col] == user_symbol:
            user_won = True

    # check diagonals
    if (
        board[0][0] == board[1][1] == board[2][2] == computer_symbol
        or board[0][2] == board[1][1] == board[2][0] == computer_symbol
    ):
        computer_won = True
    elif (
        board[0][0] == board[1][1] == board[2][2] == user_symbol
        or board[0][2] == board[1][1] == board[2][0] == user_symbol
    ):
        user_won = True

    if computer_won:
        return "Unfortunately the computer won, you're pathetic"
    elif user_won:
        return "Congratulations! You won!"
    else:
        return False


def check_tie(board):
    # Check for a tie
    if all(isinstance(cell, str) for row in board for cell in row):
        return True
    return False


def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")


# ask user if they want to play with X or O


def play_game_against_computer():
    user_symbol, computer_symbol = choose_x_or_o()

    while not (check_winner(computer_symbol, user_symbol, board) or check_tie(board)):
        print_board(board)

        # User's turn
        user_pick = int(
            input("\nPlease pick a number from the board to place your symbol: ")
        )
        if 1 <= user_pick <= 9 and isinstance(
            board[(user_pick - 1) // 3][(user_pick - 1) % 3], int
        ):
            board[(user_pick - 1) // 3][(user_pick - 1) % 3] = user_symbol
        else:
            print(
                "\nPlease enter a valid number from the board that has not been picked"
            )
            continue

        if check_winner(computer_symbol, user_symbol, board):
            print_board(board)
            print("Congratulations! You won!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie! You're both losers")
            break

        # Computer's turn
        available_positions = [
            i + 1 for i in range(9) if isinstance(board[i // 3][i % 3], int)
        ]
        computer_pick = random.choice(available_positions)
        board[(computer_pick - 1) // 3][(computer_pick - 1) % 3] = computer_symbol

        if check_winner(computer_symbol, user_symbol, board):
            print_board(board)
            print("Unfortunately the computer won, you're pathetic")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie! You're both losers")
            break


play_game_against_computer()
