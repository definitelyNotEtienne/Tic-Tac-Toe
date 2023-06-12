### Notes regarding the game
- The game window and everything else can be resized to your preferences by only changing the WIDTH dimension. 
- When the game is launched, it will be in Player vs Unbeatable AI mode unless the gamemode is changed by the Player.
- Press 'R' to restart the game
- Press 'G' to activate Player vs Player mode
- Press '0' to activate Player vs Random AI mode
- Press '1' to re-activate Player vs Unbeatable AI mode if other modes were chosen 
- The AI modes are Player 2 in the game

### Comparison between the Random AI and the Minimax Algorithm AI
#### The result is from left to right, 0 to 8 taken spots in ms

#### Random algorithm AI:
[0.006967, 0.005355, 0.005382, 0.00544, 0.005453, 0.005396, 0.005314, 0.00533, 0.00525]

It remains approximately the same because the algorithm takes random cells.

#### Minimax algorithm AI:
[6865.05018, 623.315921, 81.040446, 10.005745, 4.475388, 0.487959, 0.065395, 0.009381, 0.007484]

The Minimax algorithm takes lesser time because it needed lesser models to predict the best step out of all the possible steps to take by the algorithm.

