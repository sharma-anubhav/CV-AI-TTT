# Computer Vision - Artificial Intelligence Enabled TicTacToe

Hi! This project aims at simulating the classic game of **TicTacToe** using the feed from the webcam. The game follows the standard rules of X/O, where the player uses his finger to point to the section of the grid where he wishes to make his move. The user is given a 5 seconds window after each move by the computer to make his desired move.


# Uniqueness

Most object tracking algorithms suffer from one major drawback which is the amount of CPU/GPU processing required. Hence we often see low frame rates when run on local machines.
This implementation of the classic game is extremely lightweight as it does not use any object tracking pre-trained models and other ML-Algorithms that have the tendency to make the operations heavy. Instead to keep it relatively fast as we process each section of the grid seperately to extract contours from each grid square and to check if the finger was present inside that section/square. This contour extraction doesnt require any seperate dependancy and is very efficient and gets the job done perfectly. <br>All other projects use heavy object tracking algorithms for this purpose, whereas this approach employs simple yet efficient basic concepts which makes the requirements way more less and helps it become more flixble to work on lightweight machines without installing heavy dependancies.<br>
**This is a unique rendition of TicTacToe.**

## Minimax Algorithm

Minimax is a decision rule used in artificial intelligence, game theory, decision theory, etc. Minimax is useful because it leverages the capability of computers evaluating an exponentially growing series of possible scenarios. **Here the AI moves are simulated using this algorithm.**

## Libraries Required
Whats brilliant is that this requires just 2 libraries
- Opencv
- numpy

## Constraints

Since it is a webcam based game, optimal lighting is required.<br>
The background should be **Solid Color** only.

## Project Working

Opencv is used to process the webcam feed frame by frame and display a grid onto each frame. This is followed by extracting the image from each square of that grid and computing contours in order to identify if the finger is present inside that particular square or not. This is done for each square sequentially and then the users move is updated into the game state.<br>
If the n(contours)>0 in a particular square, then the finger is assumed to be present inside that particular grid.<br>
Minimax algorithm is used to compute the AI/Computer move and is also updated into the game state. After the AI move, the user is given a 5 seconds window to place his finger inside the desired position in the grid and the above procedure is repeated untill someone wins. The thresholds for the contour extraction were set via experimetation to suit the required purposes.
<br>
<br>
The flask project can be downloaded and run on a local host.
Also .exe and .dmg files for the application are provided so that the application directly runs without the need for installing any dependancies.

![enter image description here](https://github.com/sharma-anubhav/CV-AI-TTT/blob/master/flowChart.png?raw=true)

## Project Sample
![enter image description here](https://github.com/sharma-anubhav/CV-AI-TTT/blob/master/sample.png?raw=true)
