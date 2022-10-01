rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
player_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if player_input >= 3 or player_input < 0:
  print("You chose an invalid number. YOU LOSE.")
  exit(0)
choice_list=[rock,paper,scissors]
choice_names=["rock","paper","scissors"]
computer_input=random.randint(0,2)
print("You chose " + (choice_names[player_input]) + "\n" + choice_list[player_input])
print("Computer chose " + (choice_names[computer_input]) + "\n" + choice_list[computer_input])
if player_input==computer_input:
  print("Draw.")
elif player_input==0:
  if computer_input==1:
    print("Computer wins.")
  elif computer_input==2:
    print("Human wins.")
elif player_input==1:
  if computer_input==2:
    print("Computer wins.")
  elif computer_input==0:
    print("Human wins.")
elif player_input==2:
  if computer_input==0:
    print("Computer wins.")
  elif computer_input==1:
    print("Human wins.")