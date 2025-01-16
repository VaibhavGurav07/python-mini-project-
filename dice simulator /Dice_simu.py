import random

Run_Dice = True
while Run_Dice:
    print(random.randint(1 , 6))
    Again = input("Want to the Again Run dice (y/n) : ")
    if Again.lower() == 'y':
        continue
    else:
        break