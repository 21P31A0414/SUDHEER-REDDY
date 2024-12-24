import random

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(all(cell != " " for cell in row) for row in board)

def get_available_moves(board):
    """Returns a list of available moves (empty cells)."""
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                moves.append((row, col))
    return moves

def minimax(board, depth, maximizing_player):
    """Minimax algorithm with no alpha-beta pruning."""
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = "O"
            eval = minimax(board, depth + 1, False)
            board[row][col] = " "  # Undo the move
            max_eval = max(max_eval, eval)
        return max_eval
    else:  # Minimizing player
        min_eval = float('inf')
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = "X"
            eval = minimax(board, depth + 1, True)
            board[row][col] = " "  # Undo the move
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    """Gets the best move for the AI using Minimax."""
    best_move = None
    best_eval = -float('inf')
    for move in get_available_moves(board):
        row, col = move
        board[row][col] = "O"
        eval = minimax(board, 0, False)
        board[row][col] = " "  # Undo the move
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def main():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for human, False for AI

    while True:
        print_board(board)

        if player_turn:
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                        board[row][col] = "X"
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter numbers.")

            if check_winner(board, "X"):
                print_board(board)
                print("You win!")
                break
        else:
            print("AI is thinking...")
            best_move = get_best_move(board)
            board[best_move[0]][best_move[1]] = "O"
            print(f"AI plays at row {best_move[0]}, column {best_move[1]}")
            if check_winner(board, "O"):
                print_board(board)
                print("AI wins!")
                break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player_turn = not player_turn

if __name__ == "__main__":
    main()
