import turtle, time

turtle.title("A turtles learns to draw")
screen = turtle.getscreen()

# Create turtle(s)
my_turtle = turtle.Turtle()
circle_turtle = turtle.Turtle()

# Move turtle
my_turtle.shape("turtle")
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.backward(100)

my_turtle.goto(-100,0)
my_turtle.home()
my_turtle.penup() # we can take the pen up to avoid noting our positional change with a tracing line
my_turtle.goto(50,0)
my_turtle.pendown() # the pen can be placed back down to pick up a trace once moved again

# Drawing a circle
circle_turtle.penup()
circle_turtle.goto(50,-100)
circle_turtle.pendown()
circle_turtle.pensize(2)
circle_turtle.circle(50)

# Fill an image
my_turtle.fillcolor("orange")
my_turtle.begin_fill()
my_turtle.fd(100)   # note us of short-hand in turtle directions
my_turtle.lt(120)
my_turtle.fd(100)
my_turtle.lt(120)
my_turtle.fd(100)
my_turtle.end_fill()


# Cleaning up
# my_turtle.clear()  # we can clear our turtles traces
# my_turtle.reset() # or use the reset to remove our turtles settings
screen.reset() # we can also run a reset to remove all turtles settings on-screen


# Combine for loop & turtle
for i in range(4):
    my_turtle.fd(100)
    my_turtle.rt(90)

time.sleep(2)

# immediate code
if __name__ == "__main__":
    pass
