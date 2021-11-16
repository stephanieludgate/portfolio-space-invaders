# Space Invaders
Python program (using pygame) to play Space Invaders
<img width="760" alt="game play" src="https://user-images.githubusercontent.com/58275084/142034150-d0d2649e-0a33-4511-82ae-1f1028274347.png">

### Start Game
Game starts and six 'enemies' are spawned (random locations).  They travel across the x-axis, and when they reach the edge of the screen, they change direction and drop down the y-axis.  The goal of the game is to 'kill' the enemies before they reach the spaceship.  The spaceship at the bottom of the screen moves across the x-axis, controlled by the left and right arrows.  To shoot at the enemies, press the spacebar.\
<img width="760" alt="shooting bullet" src="https://user-images.githubusercontent.com/58275084/142036723-51385f2a-1175-482b-ba91-1a418a0ed3bb.png">

### Game Features
When an enemy is killed, it is re-spawned, again in a random position.  To make the game more difficult, the enemies' speed increases after 20pts, and again after 50pts.  If an enemy reaches the spaceship's x-axis, the game ends.
<img width="760" alt="game over" src="https://user-images.githubusercontent.com/58275084/142034181-81dfe963-ee97-4e0c-b374-01028d8bdf24.png">

### Opportunities for Improvement
Some improvements that could be made:
1. Add instructions for the player, before the game starts
2. Allow the user to 'Play Again' after the game ends
3. Add more enemies as the score increases
