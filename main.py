import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
names = ["timmy", "tommy", "tony", "tammy", "trippy", "tiny"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_pos = [(-450, -275), (-450, -175), (-450, -75), (-450, 75), (-450, 175), (-450, 275)]
current = 0
running = True
turtles = {}
for name in names:
    make = Turtle(shape="turtle")
    make.color(colors[current])
    make.speed("fastest")
    # make.hideturtle()
    make.penup()
    make.setx(start_pos[current][0])
    make.sety(start_pos[current][1])
    turtles[make] = colors[current]
    current += 1

# for turtle in turtles:
#     turtle.showturtle()

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

while running:
    for turtle in turtles:
        turtle.forward(random.randint(5, 15))
        position = turtle.xcor()
        if position >= 450:
            print(f"{turtles[turtle]} is the winner!")
            if turtles[turtle] == bet:
                print("Congratulations, your pick won!")
            else:
                print("Too bad...")
            running = False
            break

screen.exitonclick()
