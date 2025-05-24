# import turtle
#
# from turtle import  Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color ("red")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen)
# my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable

table = PrettyTable()
table.add_column(fieldname="Name",column=["Emma", "Gloria"])
table.add_column(fieldname="Pet_Name",column=["Kemma", "Glory"])
table.align ="l"
print(table)