# Scalable TicTacToe 
Modified from CS50AI TicTacToe submission.  
  
First I've created a `scale` (change it in tictactoe.py) variable that allows both the visual playing field and the 'logical/AI' size to scale. Some functions had to be modified to be responsive to the scale (some loops were hardcoded to the regular size of 3).
  
A normal 3x3 game of TicTacToe has 255168 possible moves. The depth of the tree is 9! (362880), but this does not take into account the amount of games that finish without a full board. However, if we scale our board to 4x4, the depth raises up to 16! (2,0922 E^13) and 5x5 gives us a depth of 25! (1,5511 E^25). Our initial Minimax function checks all possible moves before deciding on the best one, but with trees of this size, this becomes very slow.
  
I've [Implemented depth-limited Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#:~:text=Alpha%E2%80%93beta%20pruning%20is%20a,Connect%204%2C%20etc) in order to make the AI more efficient. If a path is worse than the current best, there is no need to explore that deeper. In addition, there is now a depth-limit.  
  
The AI works well, but with slightly bigger board sizes (lets take 5x5 from now on), the depth becomes a problem. For example, whilst deciding a move in the early game, the AI already has 127 million moves to consider. In the early game, the strategy and depth is not as important as in the later stages of the game (where it is useful to 'predict' the opponents moves).
  
To optimize this problem, I have implemented a depth limit function that scales based on the size of the available moves pool. The minimum depth is 2. For larger boards, the AI doesn't really have a strategy until the endgame, but it will block you from making the winning move. To try and give the AI a bit more strategy, I tried to change the scaling in steps, so the depth is increased once there are fewer steps left.

## How To Play
1. download files
2. `python -m venv venv`
3. `. venv/Scripts/activate`
4. `pip install -r requirements.txt`
5. `python runner.py`
6. (optionally) Change scale in the tictactoe.py file 