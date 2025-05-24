
import random

## import game_data
from game_data import data

# ## import art
from art import logo, vs

# ## Random choose from the data A
# random_choice_a = random.randint(0,30)
# A = random_choice_a
#
# ## Random choose from the data B
# random_choice_b = random.randint(0,30)
# B = random_choice_b
#
#
# ## compare function
# def compare_func():
#     count_a = 0
#     count_b = 0
#     count_a = game_data.data[random_choice_a]["follower_count"]
#     count_b = game_data.data[random_choice_b]["follower_count"]
#
#     if count_a > count_b:
#         A
#     else:
#         print(f"Lower {B}")
#

#
# ##printing welcome page with art
#
# print(art.logo)
# print(f"Compare {"A"}: {game_data.data[random_choice_a]["name"]} a"
#       f" {game_data.data[random_choice_a]["description"]} in {game_data.data[random_choice_a]["country"]} ")
# compare_func()
#
# print(art.vs)
# print(f"With  {"B"}: {game_data.data[random_choice_b]["name"]} a"
#       f" {game_data.data[random_choice_b]["description"]} in {game_data.data[random_choice_b]["country"]} ")
#
# A = input("Your Answer: ")






# Display Art

def check(guess, a_followers, b_followers):
    # if a_followers > b_followers and guess == "a":
    #     return  True
    # elif a_followers > b_followers and guess != "a":
    #     return False
    # elif b_followers > a_followers and guess == "b":
    #     return True
    # elif a_followers > b_followers and guess != "b":
    #     return False
    if a_followers > b_followers:
        return guess == "a"
    elif b_followers > a_followers:
        return  guess == "b"

# Format the game data into printable format
def account_format(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_descr} from {account_country}"

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    print("\n" * 20)

    print(logo)
    # Generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {account_format(account_a)}")

    print(vs)

    print(f"Against B: {account_format(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type A or B: ").lower()
    # # Check if user is correct
    ##-- Get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = check(guess= guess, a_followers=a_follower_account, b_followers=b_follower_account)
    if is_correct:
         score += 1
         print(f"You are right: Current Score {score}")
    else:

         print(f" Sorry!! That's wrong: Final score {score}")
         game_should_continue = False

