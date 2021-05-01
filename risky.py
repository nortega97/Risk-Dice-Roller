import numpy as np

print("Type exit to quit the program")
var = 1
while var == 1: 
    attack_units = input("Number of attacking units: ")
    if attack_units == "exit":
        break 
    else:
        attack_units = int(attack_units)
    stop_attack = input("Stop attacking when attacking units number reaches: ")
    if stop_attack == "exit":
        break
    else:
        stop_attack = int(stop_attack)
    defend_units = input("Number of defending units: ")
    if defend_units == "exit":
        break
    else:
        defend_units = int(defend_units)
    while defend_units > 0 and attack_units > stop_attack:   
        if attack_units > 3:
            attack_dice = sorted([np.random.randint(1, 6) for x in range(3)], reverse = True)
        else:
            attack_dice = sorted([np.random.randint(1, 6) for x in range(attack_units)], reverse = True)
        if defend_units > 2:
            defend_dice = sorted([np.random.randint(1, 6) for x in range(2)], reverse = True)
        else: 
            defend_dice = sorted([np.random.randint(1, 6) for x in range(defend_units)], reverse = True)
        for x in range(len(defend_dice)):
            if attack_dice[x] > defend_dice[x]:
                defend_units = defend_units - 1
            elif attack_dice[x] < defend_dice[x]:
                attack_units = attack_units - 1
            else:
                attack_units = attack_units - 1
        if defend_units == 0 or attack_units == stop_attack:
            print("Number of remaining attacking units: " + str(attack_units))
            print("Number of remaining defending units: " + str(defend_units))