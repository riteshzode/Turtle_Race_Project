import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)

l1 = [-70, -40, -10, 20, 50, 80]
l2 = ["red", "orange", "yellow", "green", "blue", "purple"]
turtlelist = []
race_on = False

for i in range(6):
    tim = Turtle()
    tim.penup()
    tim.color(l2[i])
    tim.shape("turtle")
    tim.goto(x=-230, y=l1[i])
    turtlelist.append(tim)

userchoice = screen.textinput(title="this is turtle race", prompt="choose a color")

while userchoice not in l2:
    userchoice = screen.textinput(title="this is turtle race", prompt="choose a color")

if userchoice:
    race_on = True

while race_on:

    for i in range(6):
        if turtlelist[i].xcor() > 220:
            race_on = False
            winner = turtlelist[i].pencolor()
            if winner == userchoice:
                print(f"you win, the winner turtle color is {winner}")
            else:
                print(f"you lose, the winner turtle color is {winner}")

        randx = random.randint(0, 10)
        turtlelist[i].forward(randx)

screen.exitonclick()
