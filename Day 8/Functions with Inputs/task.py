# def greet():
#     print("Hello Emma")
#     print("How do you do?")
#     print("Isn't the weather nice?")
# greet()
#
#
# # Functions with input
#
# def greet_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name} ?")
#     print("Isn't the weather nice?")
#
# greet_name("Gloria")
from itertools import count


# name = parameter....name of that data being passed to that data
# Gloria = argument.... data to pass to a function

# import maths

# def life_in_weeks(age):
#     age = int(input("What is your age?"))
#     years_in_weeks = 52
#     weeks_in_90yrs = 52 * 90
#     weeks_left = weeks_in_90yrs - (age * 52)
#     print(f"You have {weeks_left} weeks to live")
#
#
# life_in_weeks(31)


# Functions with more than one input
#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Gloria" , "Kumasi")
#
#
# #adding keyword argument
# greet_with( name="Emma", location="Techiman")
# greet_with( location="Techiman", name="Emma")

# count1 = 0
#
# def calculate_love_score(name1, name2):
#     true_love = "TRUE LOVE"
#     for char in true_love:
#         if char in name1:
#             count1 += char.count(char)
#             print(f"{char} = {count1}")
#         elif char in name2:
#             count1 += char.count(char)
#             print(f"{char} = {count1}")
#
#         else:
#             print(char)
#             count1 = 0
#
# calculate_love_score("GLORIA", "EMMANUEL")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    print(first_digit)

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    print(second_digit)


    score = int(str(first_digit)) + int(str(second_digit))
    print(score)

calculate_love_score("GLORIA OWUSU AFRIYIE", "EMMANUEL NYAMEKYE NTI")
