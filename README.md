# Prisoner's Dilemma Simulation  

## Project Description  
This project aims to implement an interactive simulation of the Prisoner's Dilemma, inspired by *The Evolution of Trust*. The program will simulate multiple player strategies interacting over a series of matches to observe the evolution of cooperation and betrayal. A visual interface will represent the players and their behaviors throughout the game.  

At the start, *n* players participate, and each player competes against every other player in *n* matches. A confrontation between two players is called a *round*. At the end of each round, players receive a score that changes based on their interactions. Once all players have faced each other, the *m* worst-performing players are replaced by copies of the best-performing player type. The game continues until only one type of player remains or the user presses the stop button.  


## Features
- **Customizable Parameters:** Users can specify the number of players for each strategy, the number of matches, and rewards/penalties for different outcomes.
- **Dynamic Visualization:** Players are displayed on a canvas arranged in a circle, with real-time score updates.
- **Evolution Mechanism:** After each match series, players are sorted by score. The lowest scoring player is replaced by a clone of the best performing one, mimicking evolutionary dynamics.

## How It Works?

1. **Interface Setup:**  
   - The main window is divided into two frames: one for the simulation settings and another for the display canvas.
   - Users input values for:
     - Number of Tit-for-Tat players (`nb_tit_for_tat`)
     - Number of Cheater players (`nb_cheater`)
     - Number of Gudger players (`nb_gudger`)
     - Number of Cooperator players (`nb_cooporate`)
     - Number of rounds per interaction (`nb_round`)
     - Reward for mutual cooperation (`reward_cooperate`)
     - Reward for successful cheating (`reward_cheat`)
     - Penalty for being cheated (`reward_cheated`)

2. **Player Initialization:**  
   - When the "Show the character" button is pressed, the program creates player objects for each strategy with their initial scores and displays them on the canvas using corresponding images.

3. **Simulation Execution:**  
   - The "start_step_by_step" button initiates the match series where every player interacts with every other player.
   - After all matches, players’ scores are updated and the weakest player is removed and replaced by a clone of the highest scoring player.
   - The canvas updates to reflect new scores and positions.

## Key Functions and Methods

- **`Display.__init__(self)`**  
  - Sets up the main window, interface frame, and loads required images.

- **`Display.init_window(self)`**  
  - Configures the main window layout, including frames for interface and game display.

- **`Display.create_interface_frame(self)`**  
  - Creates labels, entry fields, and buttons in the interface.
  - Buttons:
    - **"Show the character"**: Calls `create_circle_of_characters` to initialize players and display them.
    - **"start_step_by_step"**: Initiates the simulation through `play_match`.

- **`Display.create_circle_of_characters(self)`**  
  - Reads user inputs, initializes players based on the selected strategies, and draws them on the canvas.

- **`Display.play_match(self)`**  
  - Loops through each pair of players and plays rounds using the `play_round` function.
  - Updates the canvas and applies the evolutionary replacement rule.

- **`Display.remove_and_replace_players(self)`**  
  - Sorts players by score, removes the lowest scoring one, and replaces it with a clone of the best performing player.

- **`Display.update_canvas(self)`**  
  - Clears and redraws the canvas with the updated positions and scores for each player.

- **`play_round(player1, player2, nb_match, reward_cooperate, reward_cheat, reward_cheated)`**  
  - Simulates a series of matches between two players.
  - Each match round updates the players’ scores based on their strategies.

- **`Player.play(self, history)`**  
  - Determines the move for a player based on their personality and the interaction history.


## Example Use Cases

- **Educational Tool:**  
  - This simulation can be used to demonstrate concepts from game theory, such as the evolution of cooperation and the dynamics of trust.
- **Interactive Experimentation:**  
  - Users can tweak settings to see how changes in rewards or player distribution affect overall game dynamics.

## Requirements

**Image Files:** Ensure that the following image files are in the same directory as the script:
  - `grudger.gif`
  - `cooporate.gif`
  - `cheater.gif`
  - `tit_for_tat.gif`

## Running the Program

1. **Place Image Files:**  
   Ensure the required `.gif` image files are in the same directory as the main Python script.

2. **Execute the Script:**  
   Run the program using the command:
   ```bash
   python .\evolution_of_trust.py
3. **Interact:**  
   - Enter the desired values into the interface fields.
   - Click "Show the character" to visualize the initial player distribution.
   - Click "start_step_by_step" to run the simulation and observe the evolutionary changes.


## Possible Improvements

Here are some potential features that could be added in the future to enhance the experience:

- **Display Instructions Before Game Starts:**  
  Show a welcome message or instruction panel before launching the canvas, so users understand the purpose and how to interact with the simulation.

- **Step-by-Step Strategy Demonstration:**  
  Just like the interactive explanation in ["The Evolution of Trust"](https://ncase.me/trust/), consider showing how each personality behaves in sample rounds to help users understand strategies before running the full simulation.

- **Add a “Stop” Button:**  
  Allow the user to stop or reset the simulation entirely, without having to close and restart the program.

- **Multiple Generations Mode:**  
  Let the simulation run for multiple generations automatically with controls to pause/resume.

**Note:** I am working on this project alone.  

## Resources  
- [The Evolution of Trust](https://ncase.me/trust/)  
- [Wikipedia - Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)  
- [The Evolution of Cooperation](https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation)




