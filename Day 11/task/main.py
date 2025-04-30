
import random
import  art
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#
# user_card_choice_1 = []
#
# computer_card_choice = []
#
# def deal_card():
#     user_card_choice_1.append(random.choice(cards))
#     user_card_choice_1.append(random.choice(cards))
#     computer_card_choice.append(random.choice(cards))
#     print(user_card_choice_1)
#     print(computer_card_choice)
#
# deal_card()

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😎😎😎"
    elif c_score == 0:
        return "You Lose, Opponent has Blackjack 😢😒 "
    elif u_score == 0:
        return "You Win, with Blackjack 🤪 "
    elif u_score > 21:
        return "You Lose, You went over  🤔 "
    elif c_score > 21:
        return "You Win, Opponent went over  🫡🫡 "
    elif u_score > c_score:
        return "You Win 🤪🤪🫡 "
    else:
        return "You Lose"
def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards} Current score : {user_score}")
        print(f"Computer's first cards: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play the game again? Type 'y' to continue or 'no' to stop ").lower() == 'y':
    print(
        '\n' * 20
    )
    play_game()
