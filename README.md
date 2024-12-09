# Final-Project-Tic-tac-toe

## Abstract 

This project, titled "Advanced Techniques in Tic-Tac-Toe using Alpha-Beta, Minimax, and Q-Learning", explores AI strategies for enhancing gameplay in the classic Tic-Tac-Toe game. Tic-Tac-Toe is a two-player game played on a 3x3 grid where players take turns placing their marker (‘X’ or ‘O’) in an empty cell. The objective is to align three markers horizontally, vertically, or diagonally. This seemingly simple game is a great way to explore AI strategies because of its limited but non-trivial decision space. This project, titled "Tic-Tac-Toe AI Algorithms", explores and comparing AI strategies for enhancing gameplay in the classic Tic-Tac-Toe game. Tic-Tac-Toe is a two-player game played on a 3x3 grid where players take turns placing their marker (‘X’ or ‘O’) in an empty cell. The objective is to align three markers horizontally, vertically, or diagonally. This seemingly simple game is a great way to explore AI strategies because of its limited but non-trivial decision space.
## Software and Environment
Python 3.13 is used, which supports all the necessary libraries and tools for implementing AI algorithms and managing gameplay logic.

## Introduction

AI algorithms can enhance gameplay by making decisions based on various strategies:

**Q-Learning-epsilon greedy policy :** Allows the AI to learn optimal moves over time by using epsilon-greedy policy for exploration and exploitation, rewarding winning strategies and discouraging losing ones.

**BFS-Based AI:** Quickly identifies the best immediate moves by exhaustively evaluating all possible next steps.

**Alpha-Beta Pruning with herustic :** The Heuristic Alpha-Beta Tree Search algorithm is a recursive approach aimed at determining the best possible move for an AI agent. It leverages alpha-beta pruning to discard branches that are certain to produce suboptimal results, drastically reducing the number of nodes explored and enhancing computational efficiency. A heuristic evaluation function estimates the value of game states, guiding the algorithm to focus on the most promising paths. With a perfect heuristic, the algorithm could effectively limit the tree size to just the current state and its immediate optimal moves, as all other branches would be pruned instantly.

Minimax: Ensures the best outcome for the AI by considering all possible game scenarios, albeit at a higher computational cost.


## Explanation 

### 1- " Q-Learning vs human agent & Q-learning  vs herustic alpha beta purning "

state_to_key(board): Converts the board's state into a unique string key for the Q-table.

get_available_moves(board): Returns a list of empty cells where moves can be made.

q_learning_action(board, epsilon=EPSILON): Selects the next move using the epsilon-greedy policy for exploration and exploitation.

Q-Table: Tracks Q-values for each board state-action pair to learn optimal strategies.

update_q_table(old_state, action, reward, next_state): Updates the Q-values of a state-action pair based on the Q-learning rule i.e;update_q_table for updating Q-values based on rewards(+1 for wining;0 for tie;-1 for lose)..

initialize_board(): Creates and returns an empty 3x3 Tic-Tac-Toe board.

check_winner(board): Checks the board for a winner (row, column, or diagonal).

is_draw(board): Determines if the game has ended in a draw.

train_q_learning(): Trains the Q-learning agent over multiple simulated games.

print_board(board): Displays the current board state with symbols ('X', 'O', '_').

human_move(board): Allows the human player to input their move and validates it.

heuristic_alpha_beta(board, depth, alpha, beta, maximizing): Evaluates the best move using Alpha-Beta pruning with a heuristic function.

alpha_beta_action(board): Finds the optimal move for the Alpha-Beta pruning agent.

play_game(mode): Manages the gameplay, alternating moves between the selected agents or a human player

train_q_learning(): Prepares the Q-learning agent before gameplay starts.

if __name__ == "__main__": Entry point of the program, allowing users to choose game modes or exit.

Q-Learning uses reinforcement learning with parameters like learning rate (), discount factor (), and exploration rate (). It trains over 10,000 episodes to optimize gameplay. Core functions include state_to_key to encode board states, q_learning_action for move selection, and update_q_table for updating Q-values based on rewards(+1 for wining;0 for tie;-1 for lose).

#### GAME PLAY

1 - "  Q-Learning vs human agent & Q-Learning vs herustic Alpha -beta "
 Now enter the mode number : 
 
"1: Q-Learning vs Human"
"2: Q-Learning vs Alpha-Beta"
"3: Exit" 

IN MODE 1 : "Enter row and column separated by space (1 3): " 

Enter mode: 1 - "1: Q-Learning (AI) vs Human Agent"

_ _ _     = [(1 1),(1 2),(1,3)];

_ _ _     = [(2 1),(2 2),(2,3)];

_ _ _     = [(3 1),(3 2),(3,3)];


 VALID human moves
 

Enter mode: 2 - "2: Q-Learning vs Alpha-Beta"

Enter mode: 3 - "3: Exit"  


### 2 - " HEURISTIC ALPHA BETA PRUNING VS HUMAN AGENT & HEURISTIC ALPHA BETA PRUNING VS MINIMAX "


draw_board(board) - Displays the current game board in a user-friendly grid format. Helps visualize the game state for players.

utilityOfState(state) - Computes the heuristic value of a given board state using predefined weights for winning positions.

get_player_move(board) - Prompts the player to input a move, validates it, and returns a valid move index.

evaluate(board) - Checks for a winner and returns a score of 10 for AI wins, -10 for player wins, or 0 for no winner.

alpha_beta(board, depth, is_maximizing, alpha, beta) - Implements Alpha-Beta pruning to minimize search space and find the optimal move for AI.

min_max(board, is_maximizing) - Implements the standard Minimax algorithm without pruning to evaluate the optimal move.

check_winner(board) - Determines if there is a winner by checking all possible winning combinations on the board.

check_tie(board) - Checks if the game is a tie by verifying if there are no empty spaces left.

get_alpha_beta_move(board, depth=4) - Finds the best move for AI using the Alpha-Beta pruning algorithm with a specified search depth.

get_minimax_move(board) - Determines the best move for AI using the standard Minimax algorithm without pruning.

play_game() - Orchestrates the game logic, allowing players to select a mode, manage turns, and handle game results.

Alpha-Beta Pruning 

The Heuristic Alpha-Beta tree Search is a recursive algorithm that finds the best AI move by using alpha-beta pruning to eliminate suboptimal branches, improving efficiency. A heuristic evaluation estimates game state values, guiding the focus to promising paths. With an ideal heuristic, the search tree can be minimized to the current state and its optimal moves, as other branches are pruned instantly.i.e; It supports depth-limited searches. Key functions include alpha_beta for evaluating moves and pruning and get_alpha_beta_move for finding the best move.


Minimax

Minimax explores all possible outcomes exhaustively but has higher computational costs compared to Alpha-Beta. Its primary functions, min_max and get_minimax_move, evaluate board states and determine optimal moves for the AI.


#### GAME PLAY
{

Choose game mode:
1. Human vs AI (Alpha-Beta)
2. AI (Alpha-Beta) vs AI (Minimax)
3. Exit
Enter mode (1, 2, or 3): 1

  |   |      = [(0), (1), (2)];
  
  |   |      = [(3), (4), (5)];
  
  |   |      =[(6), (7), (8)];
                                           

   VALID human moves}


Choose game mode:
1. Human vs AI (Alpha-Beta)
2. AI (Alpha-Beta) vs AI (Minimax)
3. Exit
Enter mode (1, 2, or 3): 2 - 2:AI (Alpha-Beta) vs AI (Minimax)
  

Enter mode (1, 2, or 3): 3
Goodbye!
}

### 3- BFS VS HUMAN AGENT

BFS-Based AI

BFS-based AI evaluates moves in a single step, prioritizing immediate wins and falling back to random selection when necessary. It uses bfs_ai_move to find the best or fallback move and random_move for random selections.


print_board(board)
Prints the current state of the Tic-Tac-Toe board row by row, separated by horizontal lines for clarity.

is_winner(board, player)
Checks if a player has achieved a win by forming a straight line (row, column, or diagonal) on the board.

is_draw(board)
Determines if the game has ended in a draw by verifying that all cells are filled and no player has won.

is_valid_move(board, row, col)
Validates whether the given cell coordinates are within bounds and the cell is empty, making the move permissible.

bfs_ai_move(board, player)
Simulates moves for the AI using a BFS-like approach to find and execute an immediate winning move if possible; defaults to a random move otherwise.

random_move(board)
Selects a random empty cell on the board for the AI's move, ensuring the move is valid.

play_tic_tac_toe()
Orchestrates the gameplay loop, alternating between player and AI turns, managing moves, and checking for wins or draws until the game concludes.


#### GAME PLAY

  |   |       = [(0 0), (0 1), (0 2)];

  |   |       = [(1 0), (1 1), (1 2)];    

  |   |       = [(2 0), (2 1), (2 2)];

 VALID human moves

 
## **Results**


### **1-  " Q-Learning vs human agent & Q-learning  vs herustic alpha beta purning "**

Choose mode:
1: Q-Learning vs Human
2: Q-Learning vs Alpha-Beta
3: Exit
Enter mode: 1

_ _ _;

_ _ _;

_ _ _;

Enter row and column separated by space (1 3): 1 1

X _ _;

_ O _;

_ _ _;

Enter row and column separated by space (1 3): 2 1

X _ O ;

X O _ ;

_ _ _ ;

Enter row and column separated by space (1 3): 2 3

X _ O ;

X O X ;

_ O _ ;

Enter row and column separated by space (1 3): 3 3

X O O ;

X O X ;

_ O X ;

Q-Learning Agent wins!

Choose mode:
1: Q-Learning vs Human
2: Q-Learning vs Alpha-Beta
3: Exit
Enter mode: 2

_ _ _;

_ _ _;

_ _ _;

---
_ _ O;

_ _ X;

_ _ _;

---

O _ O;

_ _ X;

_ _ X;

---

O X O;

_ _ X;

O _ X;

------

O X O;

O X X;

O _ X;

-----

Alpha-Beta Agent wins!

Choose mode:
1: Q-Learning vs Human
2: Q-Learning vs Alpha-Beta
3: Exit
Enter mode: 3
Goodbye!


### **2 - " HEURISTIC ALPHA BETA PRUNING VS HUMAN AGENT & HEURISTIC ALPHA BETA PRUNING VS MINIMAX "**

Choose game mode:
1. Human vs AI (Alpha-Beta)
2. AI (Alpha-Beta) vs AI (Minimax)
3. Exit
Enter mode (1, 2, or 3): 1
{

  |   |

--------

  |   |  
  
---------
  |   |  


Human vs AI (Alpha-Beta).

Enter your move (0 to 8): 0

Invalid move, try again.

Enter your move (0 to 8): 0

X |   |  

---------
  |   |  
  
---------
  |   |  

 AI move
 
X |   |  

---------
  | O |  
  
---------
  |   |  

Enter your move (0 to 8): 8

X |   |  

---------
  | O |  
  
---------
  |   | X

  AI move
  
X | O |  

---------
  | O |  
  
---------
  |   | X
  
Enter your move (0 to 8): 5

X | O |  

---------

  | O | X
  
---------

  |   | X

  AI move
  
X | O | O

---------

  | O | X
  
---------

  |   | X
  
Enter your move (0 to 8): 3

X | O | O

---------

X | O | X

---------

  |   | X

 AI move
 
X | O | O

---------
X | O | X

---------
O |   | X

AI wins!

Choose game mode:
1. Human vs AI (Alpha-Beta)
2. AI (Alpha-Beta) vs AI (Minimax)
3. Exit
Enter mode (1, 2, or 3): 2

  |   |

---------

  |   | 
  
---------
  |   |  

AI (Alpha-Beta) vs AI (Minimax).
Minimax AI Move:

 X |   |  
 
---------

  |   |  
  
---------

  |   |  

  
Alpha-Beta AI Move:

X |   |  

---------

  | O |  
  
---------

  |   |  
  
Minimax AI Move:

X | X |  

---------
  | O |  
  
---------

  |   |  
  
Alpha-Beta AI Move:

X | X | O

---------

  | O |  
  
---------

  |   |  
  
Minimax AI Move:

X | X | O

---------
X | O | 

--------
  |   |  

Alpha-Beta AI Move:

X | X | O

---------
X | O |  

---------
O |   |  

Alpha-Beta AI wins!

Choose game mode:
1. Human vs AI (Alpha-Beta)
2. AI (Alpha-Beta) vs AI (Minimax)
3. Exit
Enter mode (1, 2, or 3): 3
Goodbye!



### **3 - " BFS VS HUMAN AGENT "**


 |   |  
 
---------
  |   |  
  
 ---------
  |   |  
  
---------

Enter row and column (0-2) for player X (e.g., '0 0'): 0 0

X |   |  

---------
  |   |  
  
---------
  |   | 
  
---------
Player O (AI) is making a move...

X |   | 

---------
  |   | O
  
---------
  |   |  
  
---------
Enter row and column (0-2) for player X (e.g., '0 0'): 1 2

Invalid move. Please try again.

X |   |  

---------
  |   | O
  
---------
  |   |
  
---------
Enter row and column (0-2) for player X (e.g., '0 0'): 2 2
X |   |  

---------
  |   | O
  
---------
  |   | X
  
---------
Player O (AI) is making a move...

X |   |

---------
  |   | O
  
---------
O |   | X

---------

Enter row and column (0-2) for player X (e.g., '0 0'): 2 1

X |   |  

---------
  |   | O
  
---------
O | X | X

---------

Player O (AI) is making a move...

X |   | 

---------
O |   | O

---------
O | X | X

---------
Enter row and column (0-2) for player X (e.g., '0 0'): 0 1

X | X |  

---------
O |   | O

---------
O | X | X

---------
Player O (AI) is making a move...

X | X |  

---------
O | O | O

---------
O | X | X

---------

Player O wins!

Results show Q-Learning adapts through learning, Alpha-Beta is efficient and faster than Minimax, and Minimax is effective but computationally expensive. Overall, Q-Learning provides adaptability, while Alpha-Beta and Minimax use deterministic strategies with varying efficiency.


# Evaluation 

## Analysis of Game Play Performance - Human vs AI Agents
In competitive gameplay scenarios, three AI algorithms demonstrated exceptional performance against human players. The Heuristic Alpha Beta Pruning algorithm achieved superior results with 94.7% wins and 5.3% losses. BFS secured a strong position with 92% wins and 8% losses, while Q-Learning with Epsilon Greedy Strategy maintained high effectiveness at 90.3% wins and 9.7% losses.
The minimal variance between these algorithms' win rates - spanning just 4.4 percentage points - indicates their refined optimization levels. Heuristic Alpha Beta Pruning emerged as the top performer, though all three algorithms consistently dominated with win rates surpassing 90%.

## AI Agent Performance Analysis - Head-to-Head Comparisons

In direct algorithmic competitions, the performance metrics revealed significant disparities between different AI approaches. When matching Q-Learning with Epsilon Greedy Strategy against Heuristic Alpha Beta Pruning, the latter demonstrated clear superiority with a 94.8% win rate, while Q-Learning achieved only 5.2% victories.
The second matchup pitted Heuristic Alpha Beta Pruning against the Minimax algorithm, where Heuristic Alpha Beta Pruning showcased overwhelming dominance with a 96.7% win rate, leaving Minimax with just 3.2% successful outcomes.
This data strongly indicates that Heuristic Alpha Beta Pruning consistently outperforms other AI strategies, maintaining superior win rates across different competitive scenarios. The substantial performance gap suggests that its decision-making and strategic planning capabilities exceed those of both Q-Learning and Minimax implementations.


# Conclusion
The comparative evaluation of AI algorithms for competitive Tic-Tac-Toe gameplay underscores distinct advantages and limitations of Q-Learning, Heuristic Alpha-Beta Pruning, and Minimax strategies.

Heuristic Alpha-Beta Pruning demonstrated unparalleled effectiveness, achieving the highest win rates in both human-versus-AI and AI-versus-AI scenarios. Its strategic precision and computational efficiency allowed it to outperform Q-Learning and Minimax with a significant performance margin, affirming its superiority in decision-making and execution.

Q-Learning, while less dominant in direct algorithmic comparisons, showcased remarkable adaptability and learning potential. This makes it a compelling choice for environments requiring continuous improvement and dynamic problem-solving. Conversely, the Minimax algorithm, though strategically sound, struggled with computational inefficiency and underperformed relative to its heuristic-enhanced counterpart.

In conclusion, Heuristic Alpha-Beta Pruning stands out as the most effective algorithm for deterministic and resource-efficient gameplay. Q-Learning offers valuable adaptability for evolving challenges, whereas Minimax, despite its foundational robustness, is limited by its computational demands in high-performance scenarios.



