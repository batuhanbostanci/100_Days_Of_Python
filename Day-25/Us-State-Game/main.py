import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Us state game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                   prompt="What is the another state name ").title()
    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        states_to_learn_csv = pd.DataFrame(missing_states)
        states_to_learn_csv.to_csv("States that need to reviewed ")
        break

    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        # t.goto(state_data.x, state_data.y), you can use also this uses
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data.state.item())
