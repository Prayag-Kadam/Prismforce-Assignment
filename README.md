Here’s a description for your GitHub repository for the Prismforce coding test:

---

## Prismforce Assignment

This repository contains the solution to the coding test provided by Prismforce.

### Problem Description

The coding test involves solving a problem based on the famous Chakravyuha scenario from the Mahabharata. In this scenario, Abhimanyu is trapped in a formation of 11 circles guarded by enemies with varying powers. Abhimanyu must cross all the circles to reach the Pandavas' army. The solution involves determining if Abhimanyu can successfully navigate through all the circles, given certain constraints:

- Abhimanyu starts with an initial power `p`.
- Each circle is guarded by an enemy with power `k1, k2, ..., k11`.
- Abhimanyu can skip fighting `a` times.
- Abhimanyu can recharge his power `b` times to its initial value `p`.
- Enemies in circles 3 and 7 can regenerate once with half their initial power and attack Abhimanyu from behind if he is battling in the next circle.
- Battling an enemy reduces Abhimanyu’s power by the enemy's power. If Abhimanyu's power is less than the enemy's power when he enters a circle, he loses the battle.

### Solution

The solution is implemented in Python. It includes a function `can_cross_chakravyuha` that takes Abhimanyu's initial power, a list of enemy powers, the number of skips, and the number of recharges as inputs, and returns a boolean indicating whether Abhimanyu can cross all circles.

### Repository Structure

- `main.py`: Contains the main function `can_cross_chakravyuha` and example test cases.
- `README.md`: This readme file explaining the problem, solution, and how to run the code.

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Prismforce-Assignment.git
   cd Prismforce-Assignment
   ```

2. Run the test case:
   ```bash
   python main.py
   ```
---
