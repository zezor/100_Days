import turtle


screen = turtle.Screen()
screen.title("Africa Countries Game")
image = "countries.gif"
screen.addshape(image)
turtle.shape(image)
turtle.shapesize(200, 200, 200)

def get_mouse_cick_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_cick_coor)

screen.mainloop()
