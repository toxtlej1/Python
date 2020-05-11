'''
This program will display a canvas of 500x500 in which we will create turtles and
have them form a square using the drawSquare() function.'''



import turtle
import random

turtle.setup(width=500, height=500)


screen = turtle.Screen()
screen.title("Turtle Fun!")


Taiga = turtle.Turtle()


def draw_square_manual(yertle, distance):
     '''
     The purpose behind this to create a square automatically compared to the last one.
     :param yertle: the turtle object; in this case Taiga
     :param distance: the length of the side of the square
     '''

     yertle.forward(distance)
     yertle.left(90)
     yertle.forward(distance)
     yertle.left(90)
     yertle.forward(distance)
     yertle.left(90)
     yertle.forward(distance)
     yertle.left(90)

draw_square_manual(Taiga, 100)
turtle.mainloop()
     
