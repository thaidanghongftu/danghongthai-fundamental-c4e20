from turtle  import *
shape ("classic")

for side in range (3,7):
    for i in range (side):
        if side == 3 or side == 5:
            color("blue")
        else:
            color("red")
        
        forward(100)
        left(360/side)

exitonclick()