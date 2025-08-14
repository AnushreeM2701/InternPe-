def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def check_draw(board):
    return all(spot in ['X', 'O'] for spot in board)


def play_tic_tac_toe():
    board = ['-' for _ in range(9)]
    current_player = 'X'
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        move = int(move) - 1

        if board[move] in ['X', 'O']:
            print("This spot is already taken. Please choose another one.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw! Neither player wins.")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_tic_tac_toe()
