# AI Checkers

## Overview

Our first step in creating the AI checkers was to establish a standard checkers game, complete with the necessary rules and a graphical user interface (GUI).

### 1. Piece Object

We began by defining a `Piece` object to represent each individual piece on the checkers board. Each piece contains attributes such as its associated row and column, color (red or white), and whether it has been crowned as a king.

### 2. Board Object

Next, we developed a `Board` object to manage the state of the checkers board. The board is represented internally using a NumPy array, facilitating efficient manipulation and evaluation of the game state. This object also tracks the number of red and white pieces remaining after each move, as well as which player's turn it is.

### 3. Game Object

The final step involved creating a `Game` object responsible for coordinating the gameplay. This object keeps track of the turns, players, and valid moves throughout the course of the game. It maintains a record of each move made, facilitates the transition between players' turns, and ultimately determines the winner based on the state of the board array.
