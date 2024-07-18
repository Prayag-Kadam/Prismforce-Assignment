def can_cross_chakravyuha(p, enemies, a, b):
    initial_power = p
    skips_remaining = a
    recharges_remaining = b

    # Enemies with regenerating power
    regen_enemies = {3, 7}
    regen_used = {3: False, 7: False}
    
    for i in range(1, 12):
        # Check for regenerating enemies before encountering them
        if i in regen_enemies and not regen_used[i]:
            p -= enemies[i-1] // 2
            regen_used[i] = True

        if skips_remaining > 0:
            skips_remaining -= 1
            continue
        
        if recharges_remaining > 0 and p < enemies[i-1]:
            p = initial_power
            recharges_remaining -= 1
        
        if p < enemies[i-1]:
            return False
        
        p -= enemies[i-1]
        
        if p < 0:
            return False

    return True

# Test case you provided
p1 = 9
enemies1 = [1, 1, 1, 2, 2, 2, 5, 5, 8, 2, 3, 1]
a1 = 3
b1 = 2

print(can_cross_chakravyuha(p1, enemies1, a1, b1))  # Expected output: True or False based on the logic

# Additional test case
p2 = 15
enemies2 = [5, 6, 8, 7, 10, 3, 9, 6, 7, 8, 7]
a2 = 3
b2 = 2

print(can_cross_chakravyuha(p2, enemies2, a2, b2))  # Expected output: True or False based on the logic
