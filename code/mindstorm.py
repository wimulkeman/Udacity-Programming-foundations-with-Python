import turtle

def draw_square():
    # Create a window to display the lines
    window = turtle.Screen()
    window.bgcolor("red")

    # The turtle is the moving part for the line
    brad = turtle.Turtle()
    brad.shape('turtle')  # Default is arrow
    brad.color('yellow')  # Default is color
    brad.speed(2)  # Default is 1

    # Moving the turtle
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    
    # Close the window after a click
    window.exitonclick()

draw_square()