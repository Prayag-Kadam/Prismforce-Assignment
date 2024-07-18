# Chakravyuha Problem Solver

This repository contains a Python implementation of the Chakravyuha problem solver, which determines whether Abhimanyu can cross the Chakravyuha given certain initial conditions.

## Problem Statement

Abhimanyu needs to cross 11 circles of enemies to reach the Pandavas' army. Each circle has an enemy with a specific power. Abhimanyu can skip fighting some enemies and can recharge his power a limited number of times. Additionally, some enemies regenerate their power after a certain point.

## Function Description

The function `can_cross_chakravyuha(p, enemies, a, b)` determines whether Abhimanyu can cross all 11 circles.

### Parameters

- `p` (int): The initial power of Abhimanyu.
- `enemies` (list of int): A list containing the power of enemies in each of the 11 circles.
- `a` (int): The number of times Abhimanyu can skip fighting an enemy.
- `b` (int): The number of times Abhimanyu can recharge his power.

### Returns

- `bool`: Returns `True` if Abhimanyu can reach the Pandavas' army, `False` otherwise.

### Logic

1. **Initial Setup**: Initialize the power, skips, and recharges.
2. **Loop Through Circles**: Iterate through each circle and apply the following rules:
   - Skip the enemy if skips are remaining.
   - Recharge power if recharges are remaining and power is less than the enemy's power.
   - Check if Abhimanyu's power is less than the enemy's power, and if so, return `False`.
   - Deduct the enemy's power from Abhimanyu's power.
   - Check for regenerating enemies and adjust power accordingly.
3. **Final Check**: Return `True` if Abhimanyu successfully crosses all circles.


### Example Test Case 1

- Initial power: 9
- Enemies: [1, 1, 1, 2, 2, 2, 5, 5, 8, 2, 3, 1]
- Skips: 3
- Recharges: 2

### Example Test Case 2

- Initial power: 15
- Enemies: [5, 6, 8, 7, 10, 3, 9, 6, 7, 8, 7]
- Skips: 3
- Recharges: 2

## Running the Code

To run the code, simply execute the Python script in a Python 3 environment. You can modify the test cases as needed to validate different scenarios.

```sh
python Prismforce-Assignment.py
```
