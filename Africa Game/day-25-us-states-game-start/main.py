import turtle
import pandas as dp
import pandas as pd

screen = turtle.Screen()
screen.title("Africa Countries Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_cick_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_cick_coor)

# screen.exitonclick()

data = pd.read_csv("africa_countries.csv")
data = pd.DataFrame(data)
all_states = data.state.to_list()
guessed_state = []
# print(all_states)

while len(guessed_state) < 50:

    answer = turtle.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What is another country's name?").title()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missed_countries.csv")
        print(f' These are the missing countries {missing_states}')
        break

    if answer in all_states:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        # t.write(answer)
        t.write(state_data.state.item())



# def plotting_the_cord():
#     data = pd.read_csv("africa_countries.csv")
#     data = pd.DataFrame(data)
#     state = data.state
#     print(state)
#     data[ANSWER] == state
# plotting_the_cord()









