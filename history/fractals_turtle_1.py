import turtle
#install tkinter https://stackoverflow.com/questions/76105218/why-does-tkinter-or-turtle-seem-to-be-missing-or-broken-shouldnt-it-be-part
def fractal(level):
    if level == 0:
        return

    turtle.forward(10)
    fractal(level - 1)
    turtle.right(90)
    fractal(level - 1)
    turtle.right(90)
    fractal(level - 1)
    turtle.right(90)

turtle.speed(-1)
fractal(15)
turtle.exitonclick()

import turtle

def fractal(level, size):
    if level == 0:
        return

    for i in range(4):
        turtle.forward(size)
        fractal(level - 1, size / 2)
        turtle.right(90)

turtle.speed(0)
fractal(5, 100)
turtle.exitonclick()
