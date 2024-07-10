import random

player_win = False
is_tie = False
player_choice = ""
computer_choice = ""
player = 0;
computer = 0;

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🖖")
print("5) 🦎")

player= int(input("Pick a number: "))

computer = random.randint(1,5)

if (player == 3 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 5) or \
   (player == 5 and computer == 4) or (player == 4 and computer == 3) or (player == 3 and computer == 5) or \
   (player == 5 and computer == 2) or (player == 2 and computer == 4) or (player == 4 and computer == 1) or \
   (player == 1 and computer == 3):
    player_win = True
elif player==computer:
    is_tie = True
    
if player == 1:
    player_choice = "✊"
elif player == 2:
    player_choice = "✋"
elif player == 3:
    player_choice = "✌️"
elif player == 4:
    player_choice = "🖖"
elif player == 5:
    player_choice = "🦎"
    
if computer == 1:
    computer_choice = "✊"
elif computer == 2:
    computer_choice = "✋"
elif computer == 3:
    computer_choice = "✌️"
elif computer == 4:
    computer_choice = "🖖"
elif computer == 5:
    computer_choice = "🦎"
    
print(f"You Chose: {player_choice}")
print(f"CPU Chose: {computer_choice}")

if is_tie:
    print("It's a tie")
else:
    if player_win:
        print("The player won!")
    else:
        print("The CPU won!")

