import random
from turtle import Turtle, Screen

game_is_on=False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")  
colours=["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list=[]
for turtle_index in range(0, 6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100+turtle_index*40)
    turtle_list.append(new_turtle)

if user_bet:
    game_is_on=True

while game_is_on:

    for turtle in turtle_list:
        if turtle.xcor()>230:
            game_is_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance=random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()