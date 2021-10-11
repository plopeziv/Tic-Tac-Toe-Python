#Tic-Tac-Toe
This application runs a user vs computer Tic-Tac-Toe command line game. To play simply follow the command prompts and submit a response by typing on the keyboard followed by the enter button. At the end of each game, an option will be given to play again. If the user does not wish to play again, a simple "n" response will exit the game. 

#Installation
GameClass.py will run on any machine with python 3.0 or greater. To run the entire game and test suite pytest, pytest-watch, and numpy should all be installed as dependencies.

#Running the Game
While in the src directory, enter the initiation command below

```python
python3 GameClass.py


#Testing
To use the pytest testing suite use the ptw command inside the Tic-Tac-Toe-Python directory. Currenly, a directory bug exists that will not allow the tests run at startup. To circumnavigate this bug, comment out _test.py files before running. After pytest's first run, the _test.py files can be restored. Tests will then run normally until the next ptw session. 

#Contributors
The initial Tic-Tac-Toe program was created by Pedro Lopez under the guidance and oversight of Dave Torre & Matt Readout. 