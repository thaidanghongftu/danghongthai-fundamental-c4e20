from turtle import *
color("blue")
shape("classic")
speed(10000)
left(120)
# for i in range (4):
#     forward(200)
#     left(90)

for j in range (0,200,5):
    left(-15)

    for i in range (4):
        forward(200-j)
        left(90)




