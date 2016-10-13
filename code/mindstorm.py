import turtle


def draw_line(turtle_drawer, take_steps, turn):
    turtle_drawer.forward(take_steps)
    turtle_drawer.right(turn)


def draw_square(turtle_drawer):
    # Moving the turtle
    for i in range(0,4):
        draw_line(turtle_drawer, 100, 90)

def draw_circle():
    # Adding a second turtle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")

    angie.circle(100)  # Radius of the circle

def draw_triangle(turtle_drawer):
    for i in range(0, 3):
        draw_line(turtle_drawer, 40, 120)

def draw_fancy_circle(turtle_drawer):
    # Moving the turtle
    turnDegreeOnStep = 10
    # Create the circle
    for i in range(0,360, turnDegreeOnStep):
        # Create the square
        for turn in range(0, 4):
            draw_line(turtle_drawer, 100, 90)
        brad.right(turnDegreeOnStep)


def draw_flower(turtle_drawer):
    draw_fancy_circle(turtle_drawer)
    turtle_drawer.right(90)
    turtle_drawer.color('green')
    turtle_drawer.width(10)
    turtle_drawer.forward(300)


def define_turtle(shape, color, speed):
    turtle_drawer = turtle.Turtle()
    turtle_drawer.shape(shape)
    turtle_drawer.color(color)
    turtle_drawer.speed(speed)

    return turtle_drawer


# Create a window to display the lines
window = turtle.Screen()
window.bgcolor("red")

# Define the used turtles
# The turtle is the part that draws the line
brad = define_turtle('turtle', 'yellow', 50)
angie = define_turtle('arrow', 'blue', 6)
jenny = define_turtle('circle', 'green', 6)

# draw_square(brad)
# draw_circle(angie)
# draw_triangle(jenny)
# draw_fancy_circle(brad)

# Create a flower
draw_flower(brad)

# Close the window after a click
window.exitonclick()
