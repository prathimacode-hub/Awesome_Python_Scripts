# Chess Game
### This repo contains program for a Chess Game in python.

#### In this game, the whole board can be controlled using simple algebraic commands, 
For example:
>>>e4 e7
This will move the pawn present on the e4 position to the e7 position. The program will evaluate constantly, whether its a valid move or not.

CONVENTIONS: Positions are row-column based, both are numbers from the bottom left. This corresponds to the alpha-number system in traditional chess while being computationally useful. They are specified as tuples

Game class contains the following members and methods:
> Two arrays of pieces for each player.
> 8x8 piece array with references to these pieces.
> A parse function, which turns the input from the user into a list of two tuples denoting start and end points.
> A checkmateExists function which checks if either players are in checkmate.
> A checkExists function which checks if either players are in check.
> A main loop, which takes input, runs it through the parser, asks the piece if the move is valid, and moves the piece if it is. If the move conflicts with another piece, that piece is removed. ischeck(mate) is run, and if there is a checkmate, the game prints a message as to who wins.

General Chess Rules
White is always first to move and players take turns alternately moving one piece at a time. A piece may be moved to another position or may capture an opponent´s piece, replacing on its square. With the exception of the knight, a piece may not move over or through any of the other pieces. When a king is threatened with capture (but can protect himself or escape), it´s called check. If a king is in check, then the player must make a move that eliminates the threat of capture and cannot leave the king in check. Checkmate happens when a king is placed in check and there is no legal/valid move to escape. Checkmate ends the game and the side whose king was checkmated looses.

#### Setup instructions
1. Install 3.x (recommended).

2. Download this repository as zip and extract.

4. Open cmd prompt and adjust the directory to 'Chess Game' folder.

5. Type this command to run the code

chess_game.py

Have fun!!

## Output
<img align="center" alt="output" src="Images/img.jpg"/>

Creator: [Sahil Singh](https://github.com/sahilsingh2402)
