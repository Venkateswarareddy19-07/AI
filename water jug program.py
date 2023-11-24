jug1_capacity = 4
jug2_capacity = 3
target_amount = 2
jug1_current = 0
jug2_current = 0
step = 1
while jug1_current != target_amount and jug2_current != target_amount:
    print(f"Step {step}: Jug 1 has {jug1_current} units and Jug 2 has {jug2_current} units")
    if jug1_current == 0:
        jug1_current = jug1_capacity
    while jug1_current > 0 and jug2_current < jug2_capacity:
        jug1_current -= 1
        jug2_current += 1
        print(f"Step {step}: Pour water from Jug 1 to Jug 2 - Jug 1 has {jug1_current} units and Jug 2 has {jug2_current} units")
        step += 1
    if jug2_current == jug2_capacity:
        jug2_current = 0
        print(f"Step {step}: Empty Jug 2 - Jug 1 has {jug1_current} units and Jug 2 has {jug2_current} units")
        step += 1
print(f"\nTarget amount of {target_amount} units achieved!")
