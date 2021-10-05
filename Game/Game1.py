# Stone Paper Size GamePratik
import random
choices = ["Stone", "Paper", "Sizer"]
first_player = input("First Player: Enter your Name:")
computer_player = "Computer player"
for i in range(len(choices)):
    print(i, choices[i], end="\t")
print()
first_player_choice = input(f"{first_player}: Enter your choice:").lower()
if first_player_choice not in choices:
    first_player_choice = input(f"{first_player}: Plz.. Enter correct choice:").lower()
second_player_choice = random.choice(choices).lower()
print(f"{computer_player}'s choice is: {second_player_choice}")
while True:
    if(first_player_choice == "stone" and second_player_choice == "sizer"):
        print("First player Won")
        break
    elif first_player_choice == "stone" and second_player_choice == "paper":
        print("Second Player Won")
        break
    elif first_player_choice == "paper" and second_player_choice == "sizer":
        print("Second player Won")
        break
    elif first_player_choice == "stone" and second_player_choice == "stone":
        print("DRAW!!")
        break
    elif first_player_choice == "paper" and second_player_choice == "paper":
        print("DRAW!!")
        break
    elif first_player_choice == "sizer" and second_player_choice == "sizer":
        print("DRAW!!")
        break
    if(first_player_choice == "sizer" and second_player_choice == "stone"):
        print("Second player Won")
        break
    elif first_player_choice == "paper" and second_player_choice == "stone":
        print("First Player Won")
        break
    elif first_player_choice == "sizer" and second_player_choice == "paper":
        print("Second player Won")
        break

