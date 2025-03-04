# Prisoner's Dilemma Simulation  

## Project Description  
This project aims to implement an interactive simulation of the Prisoner's Dilemma, inspired by "The Evolution of Trust." The program will simulate multiple player strategies interacting over a series of matches to observe the evolution of cooperation and betrayal. A visual interface will be generated to represent the players and their behaviors throughout the game.  

## Main Features  
1. **Game System**: Simulation of matches between different player strategies, with a scoring system based on interactions (cooperation or betrayal). The user will be able to customize:  
   - The reward system (points for cooperation, betrayal, etc.).  
   - The number of matches per round (each player plays *n* matches against every other player per round).  
2. **Player Strategies**:  
   - **Tit-for-Tat**: Starts by cooperating, then mimics the opponent’s last move.  
   - **Cheater**: Always betrays.  
   - **Grudger**: Cooperates, but if the opponent betrays once, it will betray forever.  
   - **Cooperator**: Always cooperates.  
   - **Detective**: Starts by testing multiple strategies before adopting a winning approach.  
3. **Graphical Interface**: Visualization of players as colored bubbles (blue for Tit-for-Tat, red for Cheater, yellow for Grudger, green for Cooperator). The user can adjust the number of each type of player.  

## Resources  
- [The Evolution of Trust](https://ncase.me/trust/)
- [Wikipedia - Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)  
- [The Evolution of Cooperation](https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation)  
