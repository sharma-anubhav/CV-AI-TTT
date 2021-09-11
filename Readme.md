# Computer Vision - Artificial Intelligence Enabled TicTacToe

Hi! This project aims at simulating the classic game of **TicTacToe** using the feed from the webcam. The game follows the standard rules of X/O, where the player uses his finger to point to the section of the grid where he wishes to make his move. The user is given a 5 seconds window after each move by the computer.


# Uniqueness

This game is extremely lightweight as it does not use any object tracking pre-trained models and other ML-Algorithms that have the tendency to make the operations heavy. Instead to keep it relatively fast, we process the sections of the grid to extract contours from each grid square and to check if the finger was present inside that section/square.  

## Minimax Algorithm

Minimax is a decision rule used in artificial intelligence, game theory, decision theory, etc. Minimax is useful because it leverages the capability of computers evaluating an exponentially growing series of possible scenarios. **Here the AI moves are simulated using this algorithm.**

## Libraries Required
Whats brilliant is that this requires just 2 libraries
- Opencv
-  numpy

## Constraints

Since it is a webcam based game, optimal lighting is required.
The background should be **Solid Color** only.

## Project Working

The flask project can be downloaded and run on a local host.
Also .exe and .dmg files for the application are provided so that the application directly runs without the need for installing any dependancies.



## Project Sample
![enter image description here](https://github.com/sharma-anubhav/blog/blob/master/img/CV_AI.jpg?raw=true)
