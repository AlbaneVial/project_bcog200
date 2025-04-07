# How to Test the Prisoner’s Dilemma Simulation

This section describes a complete test scenario that a user can follow to verify that the simulation program functions correctly from start to finish. 

## **Test Scenario**

### **Step 1: Preparation**
Ensure that the following image files are present in the same directory as the Python script:
- `grudger.gif`
- `cooporate.gif`
- `cheater.gif`
- `tit_for_tat.gif`


### **Step 2: Launch the Program**
Run the main script from your terminal:
```bash
python evolution_of_trust.py
```

---

### **Step 3: Input Test Values**
Once the GUI window opens:
- In the left panel, enter the following values in each corresponding field:

| Field                | Value |
|----------------------|-------|
| nb_tit_for_tat       | 2     |
| nb_cheater           | 2     |
| nb_gudger            | 2     |
| nb_cooporate         | 2     |
| nb_match             | 5     |
| reward_cooperate     | 2     |
| reward_cheat         | 3     |
| reward_cheated       | 1     |

These values will create 8 players in total and simulate 5 rounds for each player-vs-player interaction.

---

### **Step 4: Display Players**
- Click the **"Show the character"** button.
- The canvas on the right side should populate with 8 players, evenly spaced in a circle, with each player showing:
  - Their corresponding image
  - An initial score (default: 300)

Check that the images and scores are properly displayed for all players.

---

### **Step 5: Run the Simulation**
- Click the **"start_step_by_step"** button.
- The program will:
  1. Simulate matches between each pair of players.
  2. Update player scores based on their strategies and the input reward/penalty system.
  3. Replace the lowest-scoring player with a copy of the best-performing one.
  4. Refresh the canvas with new scores and positions.

Verify that:
- Scores change appropriately.
- A player is removed and replaced.
- The new canvas reflects updated states.

---

### **Step 6: Repeat**
Click **"start_step_by_step"** again to simulate a second generation.
Observe if the simulation correctly continues the evolutionary cycle.

---

### **Step 7: Manual Verification**
Repeat the process with different parameters:
- Increase the number of matches
- Change reward/penalty values
- Set some strategies to 0 to test edge cases

Ensure that the application behaves as expected under various configurations.

---

## **Expected Output**
- Players appear and update correctly
- Scores increase/decrease based on behavior logic
- Evolution mechanism works (player replacement)
- No crashes or unexpected behavior when changing parameters or repeating the simulation

