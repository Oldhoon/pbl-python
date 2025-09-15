from turtle import Turtle

import pandas as pd
import turtle as t

screen = t.Screen()
screen.title("Name the States")
image = "assets/blank_states_img.gif"
screen.addshape(image)
t.shape(image)
screen.setup(750, 550)



df = pd.read_csv("assets/50_states.csv")
game_over = False
all_states = df.state.to_list()
correct_states = set()


def draw_state(ans):
    state_data = df[df.state == ans]
    new_turtle = t.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(state_data.x.item(), state_data.y.item())
    new_turtle.write(ans)

score = 0

def print_game_over():
    n_t = Turtle()
    n_t.write("Congrats! You've guessed all 50 states")
    n_t.penup()
    n_t.hideturtle()

while not game_over:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?" ).title()
    if answer_state in correct_states:
        pass
    elif answer_state in all_states:
        draw_state(answer_state)
        correct_states.add(answer_state)
        score += 1

    if 50 == len(correct_states):
        game_over = True
        print_game_over()




