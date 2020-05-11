# What is the purpose of this module?
import turtle


# setup an empty canvas in a new Python window
turtle.setup(width=500, height=500)

# Creating screen object and giving it a title
screen = turtle.Screen()
screen.title("Hello Turtles")

# creating a turtle and naming my turtle named "Taiga"
Taiga = turtle.Turtle()

''' The following lines of code is using the created object and
by using the dot-notation, we are able to use functions within the turtle module.
This will make Taiga create a shape. What shape do you think it will make?'''
Taiga.forward(100)
Taiga.left(90)
Taiga.forward(100)
Taiga.left(90)
Taiga.forward(100)
Taiga.left(90)
Taiga.forward(100)
