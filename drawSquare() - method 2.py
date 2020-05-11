'''
This program will display a canvas of 500x500 in which we will create turtles and
have them form a square using the drawSquare() function.'''



import turtle
import random

turtle.setup(width=500, height=500)


screen = turtle.Screen()
screen.title("Turtle Fun!")


Taiga = turtle.Turtle()
Taiga.shape("turtle")
Taiga.color("green")

def draw_square_loop(yertle, distance):
     '''
     The purpose behind this function is there will be a loop that will run 4 times.
     the same amount of instructions as the first drawSquare() program.
     :param yertle: the turtle object; in this case Taiga
     :param distance: the length of the side of the square
     '''
     for num in range(4):
          yertle.forward(distance)
          yertle.left(90)

draw_square_loop(Taiga, 100)
turtle.mainloop()
     
