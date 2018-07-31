from turtle import *
color("blue")
shape("classic")
speed(1000)
def square_divide(): 
    for i in range(4):
        forward(100)
        left(90)

    left(180)

    for i in range(4):
        forward(100)
        left(90)

    left(90)

    for i in range(4):
        forward(100)
        left(90)

    left(180)

    for i in range(4):
        forward(100)
        left(90)

for i in range(6):
    square_divide()
    left(15)

exitonclick()
