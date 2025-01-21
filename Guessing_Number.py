import random

print("Welcome Welcome ...... ")
print("We are Play the Guessing Number....!!!!")
print("---------------------------")

Number_to_guess = random.randrange(1,100)

No_Guess = 7

Guess_num = 0

while No_Guess >=Guess_num :
    
    Guess_num = +1
    Number_input = int (input("Enter the Your mind numbers :- "))

    if Number_input == Number_to_guess:
        print("congratulations..!!!!!!!  ")
        print("Your Correct Guess Number ")
        break
    elif No_Guess <= Guess_num and Number_input != Number_to_guess:
        print("Your Look The Game Sorry try Again....!!!!!")
    elif Number_input <Number_to_guess:
        print("Your Number is to low")
    elif Number_to_guess < Number_input:
        print("Your Number is To big ")