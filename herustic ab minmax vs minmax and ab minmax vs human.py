import random  # Imports the random module to allow random decisions (like deciding who goes first).
import numpy as np  # Imports numpy for handling arrays efficiently.
from copy import copy  # Imports copy for creating shallow copies of objects.

# Function to display the game board
def draw_board(board):
    print(board[0], "|", board[1], "|", board[2])  # Prints the first row of the board.
    print("---------")  # Prints a separator between rows.
    print(board[3], "|", board[4], "|", board[5])  # Prints the second row.
    print("---------")  # Separator between rows.
    print(board[6], "|", board[7], "|", board[8])  # Prints the third row.

# Initialize the heuristic table to evaluate board positions for each winning position
rows, cols = 3, 3  # Tic-Tac-Toe board has 3 rows and 3 columns.
heuristicTable = np.zeros((rows + 1, cols + 1))  # Initializes a heuristic table of size (4,4) for storing evaluation values.

# Calculate the number of winning positions (rows, columns, and diagonals)
numberOfWinningPositions = rows + cols + 2  # 3 rows, 3 columns, and 2 diagonals.

# Populate the heuristic table with values for each position
for index in range(0, rows + 1):
    heuristicTable[index, 0] = 10 ** index  # Positive value for X's (player).
    heuristicTable[0, index] = -10 ** index  # Negative value for O's (AI).

# Define the array of winning positions (index combinations that result in a win)
winningArray = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                         [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                         [0, 4, 8], [2, 4, 6]])

# Function to calculate the utility (score) of a given board state based on the heuristic table
def utilityOfState(state):
    stateCopy = copy(state)  # Make a copy of the board to avoid modifying the original.
    heuristic = 0  # Initialize heuristic score.

    # Evaluate each winning position
    for i in range(0, numberOfWinningPositions):
        maxp = 0  # Counter for AI's pieces ('O')
        minp = 0  # Counter for player's pieces ('X')
        for j in range(0, rows):
            if stateCopy[winningArray[i, j]] == 2:  # 'O' is AI.
                maxp += 1
            elif stateCopy[winningArray[i, j]] == 1:  # 'X' is player.
                minp += 1
        heuristic += heuristicTable[maxp][minp]  # Add the heuristic value for the combination.

    return heuristic  # Return the calculated heuristic value.

# Function to get a valid move from the player
def get_player_move(board):
    valid_move = False  # Initially, no valid move.
    while not valid_move:  # Keep asking until a valid move is given.
        move = input("Enter your move (0 to 8): ")  # Prompt the player for a move.
        if move.isdigit() and int(move) in range(9) and board[int(move)] == " ":  # Check if the move is valid.
            valid_move = True  # Mark the move as valid.
        else:
            print("Invalid move, try again.")  # Print an error message for invalid move.
    return int(move)  # Return the valid move as an integer.

# Heuristic Evaluation Function
def evaluate(board):
    winner = check_winner(board)  # Check if there is a winner.
    if winner == "O":  # AI wins.
        return 10
    elif winner == "X":  # Player wins.
        return -10
    return 0  # No winner or a tie.

# Alpha-Beta Pruning with Heuristic (Minimax algorithm with optimization)
def alpha_beta(board, depth, is_maximizing, alpha, beta):
    if depth == 0 or check_winner(board) or check_tie(board):  # Base case: stop if max depth is reached or game over.
        return utilityOfState(np.array([1 if x == "X" else 2 if x == "O" else 0 for x in board]))  # Return the utility of the board.

    if is_maximizing:  # If it is AI's turn to maximize the score.
        max_eval = -float("inf")  # Start with a very low evaluation.
        for i in range(9):
            if board[i] == " ":  # If the cell is empty.
                board[i] = "O"  # AI places its piece.
                eval = alpha_beta(board, depth - 1, False, alpha, beta)  # Recursively call alpha-beta for the opponent.
                board[i] = " "  # Undo the move.
                max_eval = max(max_eval, eval)  # Get the maximum evaluation.
                alpha = max(alpha, eval)  # Update alpha.
                if beta <= alpha:  # Prune the search tree if alpha is greater than or equal to beta.
                    break
        return max_eval  # Return the best evaluation found for AI's turn.
    else:  # If it is player's turn to minimize the score.
        min_eval = float("inf")  # Start with a very high evaluation.
        for i in range(9):
            if board[i] == " ":  # If the cell is empty.
                board[i] = "X"  # Player places its piece.
                eval = alpha_beta(board, depth - 1, True, alpha, beta)  # Recursively call alpha-beta for the AI.
                board[i] = " "  # Undo the move.
                min_eval = min(min_eval, eval)  # Get the minimum evaluation.
                beta = min(beta, eval)  # Update beta.
                if beta <= alpha:  # Prune the search tree if beta is less than or equal to alpha.
                    break
        return min_eval  # Return the best evaluation found for player's turn.

# Minimax Algorithm (without pruning)
def min_max(board, is_maximizing):
    score = evaluate(board)  # Evaluate the current board state.
    if score != 0 or check_tie(board):  # If there is a winner or tie, return the score.
        return score

    if is_maximizing:  # If it's AI's turn to maximize the score.
        best_score = -float("inf")  # Start with a very low evaluation.
        for i in range(9):
            if board[i] == " ":  # If the cell is empty.
                board[i] = "O"  # AI places its piece.
                score = min_max(board, False)  # Recursively call Minimax for the opponent.
                board[i] = " "  # Undo the move.
                best_score = max(best_score, score)  # Get the maximum evaluation.
        return best_score  # Return the best evaluation for AI's turn.
    else:  # If it's player's turn to minimize the score.
        best_score = float("inf")  # Start with a very high evaluation.
        for i in range(9):
            if board[i] == " ":  # If the cell is empty.
                board[i] = "X"  # Player places its piece.
                score = min_max(board, True)  # Recursively call Minimax for the AI.
                board[i] = " "  # Undo the move.
                best_score = min(best_score, score)  # Get the minimum evaluation.
        return best_score  # Return the best evaluation for player's turn.

# Function to check if there is a winner
def check_winner(board):
    winning_positions = [  # Define all winning combinations.
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":  # Check if there are 3 same pieces in a winning position.
            return board[a]  # Return the winner (either 'X' or 'O').
    return None  # No winner yet.

# Function to check for a tie
def check_tie(board):
    return " " not in board  # A tie occurs if there are no empty spaces left on the board.

# AI Move Functions
def get_alpha_beta_move(board, depth=4):
    best_score = -float("inf")  # Initialize with the worst possible score.
    best_move = None  # Track the best move.
    for i in range(9):
        if board[i] == " ":  # If the cell is empty.
            board[i] = "O"  # AI places its piece.
            score = alpha_beta(board, depth - 1, False, -float("inf"), float("inf"))  # Use alpha-beta pruning.
            board[i] = " "  # Undo the move.
            if score > best_score:  # If the score is better, update the best move.
                best_score = score
                best_move = i
    return best_move  # Return the best move for AI.

def get_minimax_move(board):
    best_score = -float("inf")  # Initialize with the worst possible score.
    best_move = None  # Track the best move.
    for i in range(9):
        if board[i] == " ":  # If the cell is empty.
            board[i] = "O"  # AI places its piece.
            score = min_max(board, False)  # Use the Minimax algorithm.
            board[i] = " "  # Undo the move.
            if score > best_score:  # If the score is better, update the best move.
                best_score = score
                best_move = i
    return best_move  # Return the best move for AI.

# Main Game Function
def play_game():
    while True:
        print("\nChoose game mode:")  # Display the game mode options.
        print("1. Human vs AI (Alpha-Beta)")  # Option 1: Human vs AI with Alpha-Beta.
        print("2. AI (Alpha-Beta) vs AI (Minimax)")  # Option 2: AI vs AI using Alpha-Beta and Minimax.
        print("3. Exit")  # Option 3: Exit the game.
        mode = input("Enter mode (1, 2, or 3): ")  # Get user's choice of mode.

        if mode == "3":  # If user selects Exit.
            print("Goodbye!")  # Display exit message.
            break

        board = [" " for _ in range(9)]  # Initialize the empty board.
        draw_board(board)  # Draw the initial board.
        player_turn = random.choice([True, False])  # Randomly decide who goes first.

        if mode == "1":  # Human vs AI (Alpha-Beta).
            print("\nHuman vs AI (Alpha-Beta).")
            while True:
                if player_turn:
                    move = get_player_move(board)  # Get the human player's move.
                    board[move] = "X"  # Place player's piece.
                else:
                    move = get_alpha_beta_move(board)  # Get AI's move using Alpha-Beta.
                    board[move] = "O"  # Place AI's piece.

                draw_board(board)  # Draw the updated board.
                if check_winner(board):  # Check if there is a winner.
                    print("You win!" if player_turn else "AI wins!")  # Print the result.
                    break
                elif check_tie(board):  # Check if the game is a tie.
                    print("It's a tie!")  # Print a tie message.
                    break
                player_turn = not player_turn  # Switch turns.

        elif mode == "2":  # AI (Alpha-Beta) vs AI (Minimax).
            print("\nAI (Alpha-Beta) vs AI (Minimax).")
            while True:
                if player_turn:
                    move = get_alpha_beta_move(board)  # Get move for AI with Alpha-Beta.
                    board[move] = "O"
                    print("Alpha-Beta AI Move:")
                else:
                    move = get_minimax_move(board)  # Get move for AI with Minimax.
                    board[move] = "X"
                    print("Minimax AI Move:")

                draw_board(board)  # Draw the updated board.
                if check_winner(board):  # Check if there is a winner.
                    print("Alpha-Beta AI wins!" if player_turn else "Minimax AI wins!")  # Print the result.
                    break
                elif check_tie(board):  # Check if the game is a tie.
                    print("It's a tie!")  # Print a tie message.
                    break
                player_turn = not player_turn  # Switch turns.

        else:
            print("Invalid mode. Please select again.")  # Handle invalid mode selection.

# Start the game by calling play_game() if this script is run directly.
if __name__ == "__main__":
    play_game()  # Start the main game loop.
