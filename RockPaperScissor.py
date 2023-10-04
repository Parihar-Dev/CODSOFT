
# --------------------    TASK 03    --------------------

# Rock Paper Scissor Game

import random

# User Input

# Computer Selection

# Display Result

round = 1
c = 0
p = 0
t = 0

def Game(round) :
    global c
    global p
    global t

    player_choice = input("\nChoose Rock(r) , Paper(p) or Scissor(s) : ").lower()
    computer_choice = random.choice(["Rock","Paper","Scissor"])

    if (computer_choice == 'Rock' and player_choice == 's') or (computer_choice == 'Paper' and player_choice == 'r') or (computer_choice == 'Scissor' and player_choice == 'p') :
        c += 1
        print("\nComputer Won")

    elif (player_choice == 'r' and computer_choice == 'Scissor') or (player_choice == 'p' and computer_choice == 'Rock') or (player_choice == 's' and computer_choice == 'Paper') :
        p += 1
        print("\nYou Won")

    elif (player_choice == 's' and computer_choice == 'Scissor') or (player_choice == 'r' and computer_choice == 'Rock') or (player_choice == 'p' and computer_choice == 'Paper') :
        t+= 1
        print("\nGame Tied")

    else:
        print("You provided an invalid input")
    
    print(f"  ----------  Round {round}  ----------")
    print(f"\nComputer Won {c}")
    print(f"Player Won {p}")
    print(f"Games Tied {t}")

Game(round)

# Score Tracking

# Play Again
flag = 1
while flag == 1 :
    n = input("\nWant to play again (y/n) : ")
    if n == 'y' :
        round += 1
        Game(round)

    elif n == 'n' :
        flag = 0

    else : 
        print("You provided invalid input")
