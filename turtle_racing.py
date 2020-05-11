'''
turtle_race: a turtle racing program
'''

import turtle
import random


turtle.setup(width=900, height=500)

screen = turtle.Screen()
screen.title("Turtle Race")


def create_turtles():
     colors = ["blue", "red"]
     racer_list = []
     x_position = -300
     y_position = 0
     for color in colors:
          racer = turtle.Turtle()
          racer.color(color)
          racer.shape("turtle")
          racer.name = color + " turtle"
          racer.penup()
          racer.setposition(x_position, y_position)
          racer.pendown()
          y_position += 50
          racer_list.append(racer)
     return racer_list

def run_race(racers_list):
     goal = 100
     position = 0
     winner = ""
     
     while position < goal:
          runner = random.choice(racers_list)
          speed = random.randint(1, 10)
          distance = random.randint(1, 5)
          runner.speed(speed)
          runner.forward(distance)
          current_position = runner.position()
          position = current_position[0]
          winner = runner
     print("Congratulations! You are a WINNER!")
     winner.write("WIN!")
     winner.forward(20)

racers = create_turtles()
run_race(racers)

turtle.mainloop()
