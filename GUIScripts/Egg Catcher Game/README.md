# Egg Catcher Game

## Aim:

-To create a Egg catcher game using python tkinter(GUI).

## Purpose:

- To enable user to play an egg catcher game using simple python GUI scripts.

## Description:

- This project is to build a Egg catcher game using python tkinter
- For this game, we will need to import Python modules one for creating GUI and for generating random numbers and also cycles.
- For GUI we will use **"tkinter module"**..

## About this Game:

- When we Run this game
- First the user will see the catcher for catching eggs.
- Text that displays the score,initially the score will be zero.
- Text for displaying the number of lives left,initially it would be 3.
- User can move the catcher to catch the eggs
- Everytime when an egg is catched the score increases by 10, and everytime when a egg falls lives get reduced 
- The speed of the eggs and number of eggs increases by time
- When the lives become 0, the game is quit and final score will be displayed

## Procedure: 
```python
from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font
```
- After importing modules, we will create a window.
- set tha attributes for canvas and create it.
- set the attributes for catcher and eggs and create it using function.
- We then create functions for moving,creating,checking score,checking lives and so on...

## Compilation Steps:

- Install python.
- Import the neccessary modules and run the program.

## Sample Output:
![Image](https://github.com/coding-geek21/Awesome_Python_Scripts/blob/main/GUIScripts/Egg%20Catcher%20Game/Images/game_over.jpg)


![Image](https://github.com/coding-geek21/Awesome_Python_Scripts/blob/main/GUIScripts/Egg%20Catcher%20Game/Images/egg_catcher_game.jpg)

## Author:

[@coding-geek21](https://github.com/coding-geek21)
