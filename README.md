# ANGIS 2048 Game
Welcome to my version of the classic game 2048! This adaptation retains the original gameplay mechanics but offers a different visual style for a fresh gaming experience. There is a high score tracking integrated. So you can compete with other players! Check out the current highest score /high_scores. 

## How to Play
Simply run the game and enjoy!

## Code Structure
### Main Game Loop
The main game loop starts at line 158 and ends at line 215 in main.py.

### Event Handling
Event handling is integrated into the main game loop from line 183 to 208. This section defines how the game responds to player input such as directional keys, enter, and close keys.

### Initialization
The game starts by loading necessary modules (Pygame and random) and initializing Pygame for graphics handling.

### Game Setup
Initial game setup and configuration parameters are defined in config.py for easy customization.


## Defined Functions
### Several key functions are implemented:
- draw_board: Draws the game board (lines 22-28)
- new_pieces: Generates new game pieces (lines 30-45)
- draw_pieces: Renders game pieces on the board (lines 47-66)
- game_over: Handles the end-game scenario when no more moves are possible (lines 68-74)
- take_turn: Core function that processes player actions and updates the game state (lines 76-155)

## Enjoy the Game!
Feel free to explore the code, tweak the settings in config.py, and have fun playing 2048 with a new visual twist!
