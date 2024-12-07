import numpy as np # Import the numpy library and give it the alias 'np'. NumPy is used for numerical operations, especially for handling arrays (like the Tic-Tac-Toe board).
import random  # Imports the random module to allow random decisions
from copy import deepcopy # Import the 'deepcopy' function from the 'copy' module. It's used to create a deep copy of an object (like the board) so that changes to one copy don't affect the other.

# Constants for Tic-Tac-Toe
ROWS, COLS = 3, 3  # Define the size of the Tic-Tac-Toe board (3x3)
EMPTY = 0  # Value representing an empty cell on the board
PLAYER_X = 1  # Represents the human player (Player X)
PLAYER_O = 2  # Represents the Q-Learning agent (Player O)

# Q-Learning Parameters
ALPHA = 0.1  # Learning rate, how much new information influences the Q-values
GAMMA = 0.9  # Discount factor, how much future rewards are valued
EPSILON = 0.5  # Exploration rate, how often the agent chooses random moves
NUM_EPISODES = 10000  # Number of episodes for training the Q-learning agent

# Q-Table Initialization (holds Q-values for state-action pairs)
q_table = {}

# Function to convert board state into a unique key for the Q-table
def state_to_key(board):
    # Convert the board into a string to use it as a unique key
    return str(board.reshape(-1))

# Function to get available moves (cells that are still empty)
def get_available_moves(board):
    # Return a list of tuples for the empty cells on the board
    return [(r, c) for r in range(ROWS) for c in range(COLS) if board[r, c] == EMPTY]

# Function to choose an action based on epsilon-greedy strategy
def q_learning_action(board, epsilon=EPSILON):
    # Convert the board to a unique key to reference in the Q-table
    state_key = state_to_key(board)
    
    # Exploration: if random number is less than epsilon, choose a random move
    if random.random() < epsilon or state_key not in q_table:
        return random.choice(get_available_moves(board))  # Random move (exploration)
    
    # Exploitation: choose the action (move) with the highest Q-value
    q_values = q_table[state_key]  # Get the Q-values for the current state
    return max(q_values, key=q_values.get)  # Select the action with the max Q-value

# Function to update the Q-table after performing an action
def update_q_table(old_state, action, reward, next_state):
    # Convert the old and new states to unique keys for referencing in the Q-table
    old_key = state_to_key(old_state)
    new_key = state_to_key(next_state)
    
    # Initialize the Q-values for the old and new states if they don't exist in the table
    if old_key not in q_table:
        q_table[old_key] = {a: 0 for a in get_available_moves(old_state)}
    if new_key not in q_table:
        q_table[new_key] = {a: 0 for a in get_available_moves(next_state)}
    
    # Q-Learning Update Rule: Adjust the Q-value for the old state-action pair
    q_table[old_key][action] += ALPHA * (
        reward + GAMMA * max(q_table[new_key].values(), default=0) - q_table[old_key][action]
    )

# Function to initialize a new empty board for a game
def initialize_board():
    # Create and return a 3x3 board initialized with zeros (empty cells)
    return np.zeros((ROWS, COLS), dtype=int)

# Function to check if there is a winner in the current state of the board
def check_winner(board):
    # Check for a winner along rows, columns, and diagonals
    for i in range(ROWS):
        if all(board[i, :] == PLAYER_X):  # Player X wins if any row is filled with 'X'
            return PLAYER_X
        if all(board[i, :] == PLAYER_O):  # Player O wins if any row is filled with 'O'
            return PLAYER_O
    for i in range(COLS):
        if all(board[:, i] == PLAYER_X):  # Player X wins if any column is filled with 'X'
            return PLAYER_X
        if all(board[:, i] == PLAYER_O):  # Player O wins if any column is filled with 'O'
            return PLAYER_O
    # Check diagonals for a winner
    if all(board.diagonal() == PLAYER_X) or all(np.fliplr(board).diagonal() == PLAYER_X):
        return PLAYER_X
    if all(board.diagonal() == PLAYER_O) or all(np.fliplr(board).diagonal() == PLAYER_O):
        return PLAYER_O
    
    return None  # Return None if there is no winner yet

# Function to check if the game has ended in a draw (no empty cells and no winner)
def is_draw(board):
    # A draw occurs when there are no available moves and no winner
    return not get_available_moves(board) and check_winner(board) is None

# Function to train the Q-Learning agent by running multiple episodes
def train_q_learning():
    # Run through a predefined number of episodes (games)
    for _ in range(NUM_EPISODES):
        board = initialize_board()  # Start a new game with an empty board
        prev_state = deepcopy(board)  # Save the initial state of the board
        while True:
            # The agent selects a move based on the Q-learning policy
            q_move = q_learning_action(board)
            board[q_move] = PLAYER_O  # Apply the selected move (agent plays 'O')
            
            # Check if the agent has won
            if check_winner(board) == PLAYER_O:
                update_q_table(prev_state, q_move, 1, board)  # Reward the agent for winning
                break
            elif is_draw(board):
                update_q_table(prev_state, q_move, 0, board)  # Reward the agent for a draw
                break
            
            # Save the current state for the next iteration
            prev_state = deepcopy(board)

# Function to print the current state of the board
def print_board(board):
    # Print each row of the board, displaying 'X', 'O', or '_' for empty cells
    for row in board:
        print(' '.join(['_' if cell == EMPTY else 'X' if cell == PLAYER_X else 'O' for cell in row]))
    print()

# Function for the human player to make a move
def human_move(board):
    while True:
        try:
            # Prompt the human player to enter a row and column number
            row, col = map(int, input("Enter row and column separated by space (1 3): ").split())
            row, col = row - 1, col - 1  # Convert from 1-based to 0-based indexing
            if (row, col) in get_available_moves(board):  # Ensure the move is valid
                return row, col
        except ValueError:
            pass  # If the input is invalid, try again
        print("Invalid input, try again. Enter as 'row col'.")

# Alpha-Beta Pruning heuristic to evaluate the best move for the Alpha-Beta agent
def heuristic_alpha_beta(board, depth, alpha, beta, maximizing):
    # Base case: check for winner or draw
    if check_winner(board) == PLAYER_X:
        return -10  # Player X wins
    if check_winner(board) == PLAYER_O:
        return 10  # Player O wins
    if is_draw(board):
        return 0  # Draw
    
    if maximizing:  # If it's Player O's turn (maximize the score)
        max_eval = -float('inf')
        for move in get_available_moves(board):  # Try each available move
            board[move] = PLAYER_O  # Apply move for Player O
            eval = heuristic_alpha_beta(board, depth - 1, alpha, beta, False)  # Evaluate the move
            board[move] = EMPTY  # Undo the move
            max_eval = max(max_eval, eval)  # Update the best value
            alpha = max(alpha, eval)  # Update the alpha value (prune if necessary)
            if beta <= alpha:  # alpha beta pruning: cut off branches where beta <= alpha
                break
        return max_eval
    else:  # If it's Player X's turn (minimize the score)
        min_eval = float('inf')
        for move in get_available_moves(board):  # Try each available move
            board[move] = PLAYER_X  # Apply move for Player X
            eval = heuristic_alpha_beta(board, depth - 1, alpha, beta, True)  # Evaluate the move
            board[move] = EMPTY  # Undo the move
            min_eval = min(min_eval, eval)  # Update the best value
            beta = min(beta, eval)  # Update the beta value (prune if necessary)
            if beta <= alpha:  # Alpha  beta pruning: cut off branches where beta <= alpha
                break
        return min_eval

# Function to choose the best move for the Alpha-Beta agent using the heuristic function
def alpha_beta_action(board):
    best_val = -float('inf')  # Start with an impossible low value
    best_move = None  # Variable to store the best move found
    for move in get_available_moves(board):  # Try each available move
        board[move] = PLAYER_O  # Apply the move for Player O
        move_val = heuristic_alpha_beta(board, 3, -float('inf'), float('inf'), False)  # Evaluate the move
        board[move] = EMPTY  # Undo the move
        if move_val > best_val:  # If this move is better than the current best, update it
            best_val = move_val
            best_move = move
    return best_move  # Return the best move found

# Main game loop to control the flow of the game
def play_game(mode):
    board = initialize_board()  # Initialize an empty board
    print_board(board)  # Print the empty board
    while True:
        if mode == 1:  # Q-Learning vs Human
            move = human_move(board)  # Get the human player's move
            board[move] = PLAYER_X  # Apply the human move
            if check_winner(board):
                print_board(board)
                print("Human wins!")  # Check for winner
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")  # Check for draw
                break
            q_move = q_learning_action(board, epsilon=0)  # Q-learning agent's move
            board[q_move] = PLAYER_O  # Apply the agent's move
            if check_winner(board):
                print_board(board)
                print("Q-Learning Agent wins!")
                break
        elif mode == 2:  # Q-Learning vs Alpha-Beta
            q_move = q_learning_action(board, epsilon=0)  # Q-learning agent's move
            board[q_move] = PLAYER_X  # Apply the Q-learning agent's move
            if check_winner(board):
                print_board(board)
                print("Q-Learning Agent wins!")  # Check for winner
                break
            ab_move = alpha_beta_action(board)  # Alpha-Beta agent's move
            board[ab_move] = PLAYER_O  # Apply the Alpha-Beta move
            if check_winner(board):
                print_board(board)
                print("Alpha-Beta Agent wins!")
                break
        print_board(board)  # Print the current state of the board

# Main entry point of the program
if __name__ == "__main__":
    train_q_learning()  # Train the Q-learning agent before starting the game
    while True:
        print("\nChoose mode:")  # Menu to select the game mode
        print("1: Q-Learning vs Human")
        print("2: Q-Learning vs Alpha-Beta")
        print("3: Exit")
        mode = int(input("Enter mode: "))  # Get user input for game mode
        if mode == 3:
            print("Goodbye!")
            break  # Exit the game
        elif mode in [1, 2]:
            play_game(mode)  # Start the game with the selected mode
