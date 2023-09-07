import turtle

def square_fractal(turtle, size):
  if size == 0:
    return
  turtle.forward(size)
  turtle.right(90)
  square_fractal(turtle, size // 2)

turtle.speed(0)
square_fractal(turtle, 300)
turtle.hideturtle()
turtle.exitonclick()