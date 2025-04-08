# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0
# if size == "S":
#     bill = 15
#     if pepperoni == "Y":
#         bill += 2
#     else:
#         bill = 15
#     if extra_cheese == "Y":
#         bill += 1
#     else:
#         bill = 15
#     print(f"Your final bill is: ${bill}.")
# elif size == "M":
#     bill = 20
#     if pepperoni == "Y":
#         bill += 3
#     else:
#         bill = 20
#     if extra_cheese == "Y":
#         bill += 1
#     else:
#         bill = 20
#     print(f"Your final bill is: ${bill}.")
# elif size == "L":
#     bill = 25
#     if pepperoni == "Y":
#         bill += 3
#     else:
#         bill = 25
#     if extra_cheese == "Y":
#         bill += 1
#     else:
#         bill = 25
#     print(f"Your final bill is: ${bill}.")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
