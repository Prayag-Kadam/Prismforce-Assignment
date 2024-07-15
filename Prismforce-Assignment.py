def can_cross_chakravyuha(p, enemies, a, b):
    initial_power = p
    skips_remaining = a
    recharges_remaining = b

    # Enemies with regenerating power
    regen_enemies = [3, 7]
    regen_used = {3: False, 7: False}
    
    for i in range(1, 12):
        if skips_remaining > 0:
            skips_remaining -= 1
            continue
        
        if recharges_remaining > 0 and p < enemies[i-1]:
            p = initial_power
            recharges_remaining -= 1
        
        if p < enemies[i-1]:
            return False
        
        p -= enemies[i-1]

        # Check for regenerating enemies
        if (i == 4 or i == 8) and not regen_used[i-1]:
            p -= enemies[i-2] // 2
            regen_used[i-1] = True
        
        if p < 0:
            return False

    return True

# Example test cases
p1 = 10
enemies1 = [3, 2, 6, 5, 8, 2, 10, 4, 7, 6, 5]
a1 = 2
b1 = 1

p2 = 15
enemies2 = [5, 6, 8, 7, 10, 3, 9, 6, 7, 8, 7]
a2 = 3
b2 = 2

print(can_cross_chakravyuha(p1, enemies1, a1, b1))  # Example test case 1
print(can_cross_chakravyuha(p2, enemies2, a2, b2))  # Example test case 2


