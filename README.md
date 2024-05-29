# Angis2048

Hello and welcome to my game of 2048!
This game is my version of the classic 2048, with the same playgame as the classic game but
a different look.
Please enjoy the game!

I set up the game code as follows:
The main game loop can be found from line 158 to 215.
The event code can is part of this main game loop from line 183 to 208. This event code describes
what shall happen if the player hits different buttons (direction, enter,
or close keys on the keyboard).

The game code starts with loading the necessary modules (pygame and random) and the initialization
of pygame.
After this code, I defined the initial set-up of the game. Most of those parameter, to change the
design of the game, are stored in a second Python sheet for a better visibility.
The necessary, defined functions which are used in my game are following. There are four functions
that are needed to have the make the board/game appear on the screen. The first one is the
draw_board function (line 22 - 28). The second is the new pieces function (line 30 - 45), and the
third one is the draw pieces function (line 47 - 66). The fourth function is needed in case the
game is finished because there are no more moves possible (game over event) (line 68 - 74).
The core function of the game is the take turn actions. This function describes what will happen
to the different pieces on the board, if an event key is hit (direction to move is indicated). This
function start in line 76 and runs to 155.

