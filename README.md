# Prisoner's Dilemma Simulation  

## Project Description  
This project aims to implement an interactive simulation of the Prisoner's Dilemma, inspired by "The Evolution of Trust." The program will simulate multiple player strategies interacting over a series of matches to observe the evolution of cooperation and betrayal. A visual interface will be generated to represent the players and their behaviors throughout the game.

 Au début n joueurs, chaque joueurs joue avec tout les joueurs n matchs chacun. Une confrontation avec un joueurs s'appelle une round. A la fin de cette round chaque joueur à un score qui varie donc à chaque round. Une fois que tout les joueurs se sont tous confronté les m pire joueurs son remplacé par le type de joueurs avec le meilleur score. La partie continue jusqu'à qu'il y est plus qu'un type de joueurs ou que l'utilisateur appui sur le boutton stop.
## Main Features  
1. **Game System**: Simulation of matches between different player strategies, with a scoring system based on interactions (cooperation or betrayal). The user will be able to customize:  
   - The reward system (points for cooperation, betrayal, etc.).  
   - The number of matches per round (each player plays *n* matches against every other player per round).  
2. **Player Strategies**:  
   - **Tit-for-Tat**: Starts by cooperating, then mimics the opponent’s last move.  
   - **Cheater**: Always betrays.  
   - **Grudger**: Cooperates, but if the opponent betrays once, it will betray forever.  
   - **Cooperator**: Always cooperates.  
3. **Graphical Interface**: Visualization of players as colored bubbles (blue for Tit-for-Tat, red for Cheater, yellow for Grudger, green for Cooperator). The user can adjust the number of each type of player, the  reward system  and the number of match per round.  


## Code Architecture

### 1. Class Player  
- **Attributes**: `strategy`, `score` (per round), `color`  
- **Methods**: `play` (chooses a strategy based on history and player type)  

### 2. Function round  
- **Input**: `player1`, `player2`, `history1`, `history2`  
- **Output**: Scores after the match  

### 3. Class Canvas  
- **Attributes**: Displays and updates the canvas each round  
- **Methods**: `create_canvas`, `update_canvas`  

### 4. Function enter_number  
- Asks for the number of each player type, the number of matches per round, and the rewards  

> **Note:** I am working on this project alone.

## Resources  
- [The Evolution of Trust](https://ncase.me/trust/)
- [Wikipedia - Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)  
- [The Evolution of Cooperation](https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation)  
