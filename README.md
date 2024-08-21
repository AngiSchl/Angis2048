# ANGIS 2048 Game :tada:
Welcome to my version of the classic game 2048! :wave: This adaptation retains the original gameplay mechanics but offers a slightlz different visual style for a fresh gaming experience. There is a high score tracking integrated. So you can compete with other players! Check out the current highest score (./high_score.txt). So go ahead and aim for the stars :sparkles: :trophy:

## How to Play
Simply run the game and enjoy! :smile: The game ends if the field is fully populated - try to reach a new Highscore! 

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
- **draw_board**: Draws the game board (lines 22-28)
- **new_pieces**: Generates new game pieces (lines 30-45)
- **draw_pieces**: Renders game pieces on the board (lines 47-66)
- **game_over**: Handles the end-game scenario when no more moves are possible (lines 68-74)
- **take_turn**: Core function that processes player actions and updates the game state (lines 76-155)

## Enjoy the Game! 
Feel free to explore the code, and have fun playing 2048!
