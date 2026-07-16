from turtle import *


shape("turtle")
color("red")

speed("fastest")
for _ in range(36):
    circle(100)
    currentheading = heading()
    setheading(currentheading + 10)

exitonclick()