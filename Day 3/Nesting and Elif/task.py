print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age: "))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    elif age > 18:
        print("Please pay $10")
else:
    print("Sorry you have to grow taller before you can ride.")
