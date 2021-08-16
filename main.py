import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(246, 240, 243), (129, 165, 205), (223, 150, 110), (31, 40, 60), (201, 134, 146), (140, 185, 163), (236, 214, 93), (167, 60, 48), (35, 100, 151), (141, 64, 72), (236, 165, 156), (215, 86, 78), (171, 29, 32), (49, 113, 91), (231, 160, 164), (155, 34, 31), (170, 188, 221), (18, 96, 71), (29, 64, 59), (57, 51, 48), (51, 45, 48), (28, 60, 114), (104, 128, 161), (174, 200, 188), (34, 151, 210), (208, 92, 96), (65, 65, 57)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)




screen = turtle_module.Screen()
screen.exitonclick()