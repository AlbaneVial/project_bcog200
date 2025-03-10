# Prisoner's Dilemma Simulation  

## Project Description  
This project aims to implement an interactive simulation of the Prisoner's Dilemma, inspired by *The Evolution of Trust*. The program will simulate multiple player strategies interacting over a series of matches to observe the evolution of cooperation and betrayal. A visual interface will represent the players and their behaviors throughout the game.  

At the start, *n* players participate, and each player competes against every other player in *n* matches. A confrontation between two players is called a *round*. At the end of each round, players receive a score that changes based on their interactions. Once all players have faced each other, the *m* worst-performing players are replaced by copies of the best-performing player type. The game continues until only one type of player remains or the user presses the stop button.  

## Main Features  

1. **Game System**: Simulates matches between different player strategies with a scoring system based on cooperation or betrayal. The user can customize:  
   - The reward system (points for cooperation, betrayal, etc.).  
   - The number of matches per round (each player plays *n* matches against every other player per round).  

2. **Player Strategies**:  
   - **Tit-for-Tat**: Starts by cooperating, then mimics the opponent’s last move.  
   - **Cheater**: Always betrays.  
   - **Grudger**: Cooperates, but if betrayed once, will betray forever.  
   - **Cooperator**: Always cooperates.  

3. **Graphical Interface**:  
   - Players are visualized as colored bubbles:  
     - 🟦 **Tit-for-Tat** (Blue)  
     - 🟥 **Cheater** (Red)  
     - 🟨 **Grudger** (Yellow)  
     - 🟩 **Cooperator** (Green)  
   - The user can adjust:  
     - The number of each type of player.  
     - The reward system.  
     - The number of matches per round.  

## Code Architecture  

### 1. Class `Player`  
- **Attributes**: `strategy`, `score` (per round), `color`  
- **Methods**: `play` (chooses a strategy based on history and player type)  

### 2. Function `round`  
- **Input**: `player1`, `player2`, `history1`, `history2`  
- **Output**: Scores after the round  

### 3. Class `Canvas`  
- **Attributes**: Displays and updates the canvas each round  
- **Methods**: `create_canvas`, `update_canvas`  

### 4. Function `enter_number`  
- Asks for the number of each player type, the number of matches per round, and the rewards  

## Development Progress  

I have started coding the project. However, several mechanisms are still missing, such as:  
- The removal and replacement of players at the end of each round.  
- The display of the canvas.  

> **Note:** I am working on this project alone.  

## Resources  
- [The Evolution of Trust](https://ncase.me/trust/)  
- [Wikipedia - Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)  
- [The Evolution of Cooperation](https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation)  
