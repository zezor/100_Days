print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill += 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    want_a_photo = input("Do you want a picture? Y= Yes, N = No: ")
    if want_a_photo == "Y":
        bill += 3
    else:
        bill
    print(f"Your final bill is: ${bill} ")

else:
    print("Sorry you have to grow taller before you can ride.")
