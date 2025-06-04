import random
import turtle
from turtle import Turtle, Screen



is_race_on = False
my_screen = Screen()
my_screen.setup(500, 400)
my_screen.bgcolor("lavender")
my_screen.title("Turtle Race")
user_bet = my_screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color: " )
colors = ["red", "green", "blue", "black", "yellow", "pink"]
y_position = [-70, -40, -10, 20, 50, 80 ]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()




# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(15)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# my_screen.listen()
# my_screen.onkey(key="w", fun=move_forwards)
# my_screen.onkey(key="s", fun=move_backwards)
# my_screen.onkey(key="a", fun=turn_left)
# my_screen.onkey(key="d", fun=turn_right)
# my_screen.onkey(key="c", fun=clear)
# my_screen.exitonclick()


# tom = Turtle("turtle")
# tom.color(colors[1])
# tom.penup()
# tom.goto(x=-230, y=70)
#
# tam = Turtle("turtle")
# tam.color(colors[2])
# tam.penup()
# tam.goto(x=-230, y=40)
#
# tum = Turtle("turtle")
# tum.color(colors[3])
# tum.penup()
# tum.goto(x=-230, y=10)
#
# tem = Turtle("turtle")
# tem.color(colors[4])
# tem.penup()
# tem.goto(x=-230, y=-20)
#
# tin = Turtle("turtle")
# tin.color(colors[5])
# tin.penup()
# tin.goto(x=-230, y=-50)
