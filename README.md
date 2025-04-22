# Prisoner's Dilemma Simulation

## Project Description
This project implements an interactive simulation of the Prisoner's Dilemma inspired by *The Evolution of Trust*. Through a graphical interface, users observe how different strategies (Tit-for-Tat, Cheater, Grudger, Cooperator) interact over repeated matches and how evolutionary pressure favors successful strategies.

Players are visualized on a circular canvas, and their scores evolve according to classic payoff rules. After each series of interactions, the lowest‑scoring player is eliminated and replaced by a clone of the highest‑scoring one, simulating natural selection.

## Features
- **Customizable Parameters:** Users configure the number of players per strategy, number of rounds per match, and payoff values.
- **Dynamic Visualization:** Players are displayed on a circle, with real-time score updates and eliminations.
- **Evolution Mechanism:** The lowest-scoring player is replaced by a clone of the best-performing one.

## Project Structure
There are four source files, each containing one or more classes:

- **`trustapp.py`**
  - `TrustApp`: Main application class managing the window, assets, and navigation between panels.
  - `IntroPanel`: Panel for the welcome screen and strategy introduction.
  - `BotMatchPanel`: Panel for demo matches against each type of player.
  - `TopoPanel`: Panel displaying descriptions of each player personality type.
  - `MainPlayPanel`: Panel for the full tournament simulation.

- **`player.py`**
  - `Player`: Class representing an agent with a fixed personality and score.

- **`main.py`**
  - Contains the script entry point that instantiates and runs `TrustApp`.

- **`test.py`**
  - Contains unit test classes or functions to verify core behaviors of the simulation.

## How It Works

1. **Intro & Demo**
   - Launching the app shows the **Intro** panel. Click **Let’s start the game!** to begin.
   - In each **Bot Demo** panel, you face a specific strategy for five rounds. Use **Cooperate/Cheat** buttons or click **Skip the matches!** to move on immediately.

2. **Setup Tournament**
   - After demos, the **Topology** panel displays each strategy’s description. Click **Let’s go!** to enter tournament mode.
   - In the **Tournament** panel, configure:
     - Number of Tit-for-Tat players
     - Number of Cheater players
     - Number of Grudger players
     - Number of cooperate players
     - Number of rounds per match
     - Reward for mutual cooperation
     - Reward for successful cheating
     - Penalty for being cheated
   - Click **Show players** to visualize all participants on the canvas.

3. **Run Tournament**
   - Click **Start match** to execute a complete round‑robin: each pair plays the specified number of rounds.
   - Upon completion, the lowest‑scoring player is eliminated and replaced by a clone of the highest‑scoring one.
   - The canvas updates with new positions and scores for the next generation.

## Running the Simulation

1. **Place image files** (`grudger.gif`, `cooperate.gif`, `cheater.gif`, `tit_for_tat.gif`) alongside the scripts.
2. **Launch the app**:
   ```bash
   python main.py
   ```
3. **Run tests (optional)**:
   ```bash
   pytest test.py
   ```


## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- NumPy
- Image files: `grudger.gif`, `cooperate.gif`, `cheater.gif`, `tit_for_tat.gif`

## Possible Improvements

- Add a global **Stop/Reset** button.
- Automatic multi‑generation mode with pause.
- Add a **Back-navigation** button to return to the previous panel.

## Resources

- [The Evolution of Trust](https://ncase.me/trust/)
- [Prisoner’s Dilemma – Wikipedia](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)
- [The Evolution of Cooperation – Wikipedia](https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation)
