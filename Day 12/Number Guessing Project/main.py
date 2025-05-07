import random

EASY_TURNS = 10
HARD_TURNS = 5



# Welcome page
print("Welcome to computer Guessing Game")


# Computer guess
print("I am thinking of a number between 1 and 100")

com_guess = random.randint(1, 100)
print(com_guess)


#Difficulty function
difficulty = input("Choose a difficulty Type 'easy' or 'hard': ")
def set_difficulty():
    if difficulty == "easy":
        return EASY_TURNS

    else:
        return HARD_TURNS
set_difficulty()
print(f"You have {set_difficulty()} attempts remaining to guess the number")

#Guess input
guess_answer = 0

# Attempt function
TURNS =  set_difficulty()

while guess_answer != com_guess:
    guess_answer = int(input("Make a guess: "))

# compare guess and computer guess
    def compare(com_answer, user_answer, turns):

        if user_answer > com_answer:
            turns -= 1
            print("Too High")
            print(f"You have {turns} attempts remaining to guess the number")

        elif user_answer < com_answer:
            turns -= 1
            print("Too Low")
            print(f"You have {turns} attempts remaining to guess the number")

        else:
            print(   f"You got it! The answer was {com_guess}")

    compare(com_answer= com_guess,user_answer=guess_answer, turns=set_difficulty())



#def attempt():

#
#     guess_answer = int(input("Make a guess: "))

# compare guess and computer guess