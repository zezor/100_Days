import random

# Rock wins against scissor
# Scissors wins against paper
# Paper wins against rock



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
print("Welcome Rock Paper Scissors Game")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
user_choice =int(input())

out_come_list = ["rock", "paper", "scissors"]


if user_choice ==0:
    print("Your choice: ")
    #print(out_come_list[user_choice])
    print("Rock")
    print(rock)
elif user_choice == 1:
    print("Your choice: ")
    #print(out_come_list[user_choice])
    print("paper")
    print(paper)
else:
    print("Your choice: ")
    #print(out_come_list[user_choice])
    print("scissors")
    print(scissors)


computer_choice = random.randint(0,2)
print(computer_choice)

if computer_choice == 0:
    print("Computer Choice: ")
    print(out_come_list[computer_choice])
    print(rock)
elif computer_choice == 1:
    print("Computer Choice: ")
    print(out_come_list[computer_choice])
    print(paper)
else:
    print("Computer Choice: ")
    print(out_come_list[computer_choice])
    print(scissors)

# Who wins

if user_choice >= 3:
    print("You chose a wrong number ")
if computer_choice == 0 and user_choice ==2:
    print("You Loose")
elif computer_choice == 1 and user_choice == 0:
    print("You Loose!")
elif computer_choice >  user_choice:
    print("You Loose!")
elif computer_choice == 0 and user_choice == 1:
    print("You Win!")
elif computer_choice == 2 and user_choice == 0:
    print("You Win!")
elif computer_choice <  user_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Its a draw")

