import random  # Importing the random module to enable random AI moves.

def print_board(board):
    # Function to print the game board.
    for row in board:  # Loop through each row in the board.
        print(" | ".join(row))  # Join the cells in the row with '|' separator and print.
        print("-" * 9)  # Print a separator between rows for better readability.

def is_winner(board, player):
    # Function to check if a player has won the game.
    for row in board:  # Check each row.
        if all(cell == player for cell in row):  # If all cells in the row match the player, they win.
            return True
    for col in range(3):  # Check each column.
        if all(board[row][col] == player for row in range(3)):  # If all cells in the column match the player, they win.
            return True
    # Check the diagonals.
    if all(board[i][i] == player for i in range(3)):  # Top-left to bottom-right diagonal.
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Top-right to bottom-left diagonal.
        return True
    return False  # Return False if no win condition is met.

def is_draw(board):
    # Function to check if the game is a draw (board is full and no winner).
    return all(cell != " " for row in board for cell in row)  # If there are no empty cells, it's a draw.

def is_valid_move(board, row, col):
    # Function to check if the given move (row, col) is valid.
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "  # Valid if within bounds and the cell is empty.

def bfs_ai_move(board, player):
    # Function to calculate the best move for the AI using a BFS-like approach.
    for row in range(3):  # Iterate over the board rows.
        for col in range(3):  # Iterate over the board columns.
            if board[row][col] == " ":  # Check if the cell is empty.
                new_board = [r[:] for r in board]  # Create a copy of the board.
                new_board[row][col] = player  # Make the move for the AI player.
                if is_winner(new_board, player):  # Check if this move results in a win.
                    return row, col  # If the AI wins, return the row and column.
    return random_move(board)  # If no immediate winning move is found, make a random move.

def random_move(board):
    # Function to make a random move on the board.
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]  # List all empty cells.
    return random.choice(empty_cells) if empty_cells else None  # Choose a random empty cell.

def play_tic_tac_toe():
    # Main function to play the Tic-Tac-Toe game.
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize an empty 3x3 board.
    players = ["X", "O"]  # Define the two players (X and O).
    current_player = players[0]  # Start with player X.

    while True:
        print_board(board)  # Print the current state of the board.

        if current_player == "X":  # If it's player X's turn.
            try:
                # Request the row and column input in one line, separated by a space.
                row, col = map(int, input(f"Enter row and column (0-2) for player X (e.g., '0 0'): ").split())
            except ValueError:
                # Handle invalid input (non-integer or incorrect format).
                print("Invalid input. Please enter two integers between 0 and 2, separated by a space.")
                continue  # Ask for input again if there's an error.
        else:
            # If it's player O's turn (AI).
            print("Player O (AI) is making a move...")  # Notify that the AI is playing.
            ai_move = bfs_ai_move(board, current_player)  # Get the AI's move using BFS.
            row, col = ai_move if ai_move else (0, 0)  # Use the AI's move, default to (0, 0) if no move found.

        if is_valid_move(board, row, col):  # Check if the move is valid.
            board[row][col] = current_player  # Make the move on the board.

            if is_winner(board, current_player):  # Check if the current player won.
                print_board(board)  # Print the final board.
                print(f"Player {current_player} wins!")  # Announce the winner.
                break  # End the game if there's a winner.

            if is_draw(board):  # Check if the game is a draw.
                print_board(board)  # Print the final board.
                print("It's a draw!")  # Announce the draw.
                break  # End the game if it's a draw.

            current_player = players[1] if current_player == players[0] else players[0]  # Switch to the other player.
        else:
            # Handle invalid move (e.g., the chosen cell is not empty or out of bounds).
            print("Invalid move. Please try again.")

if __name__ == "__main__":
    play_tic_tac_toe()  # Start the game when the script is run.
