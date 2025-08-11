
import turtle
import math
import time

# Constants
WIDTH = 800
HEIGHT = 600
LIGHTS = 15
MOUTH_SIZE = 20

# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screensize = screen.screensize()
turtle.hideturtle()

# Function to create a list of point-lights
def create_lights(screensize, num_lights):
    lights = []
    for _ in range(num_lights):
        t = turtle.Turtle()
        t.penup()
        t.goto(screensize[0], screensize[1])
        t.color("white")
        t.shape("circle")
        t.setheading(45)
        t.speed(0)
        lights.append(t)
    return lights

# Function to create the man
def create_man(screensize):
    man = turtle.Turtle()
    man.penup()
    man.color("white")
    man.shape("circle")
    man.setposition(screensize[0] - 40, screensize[1] - 40)
    man.pendown()
    man.circle(10)
    man.left(90)
    man.penup()
    return man

# Function to move point-lights
def move_lights(lights, screensize):
    for light in lights:
        light.forward(2)
        if light.xcor() > screensize[0] - MOUTH_SIZE * 10:
            light.right(20)
        elif light.xcor() < -screensize[0] + MOUTH_SIZE * 10:
            light.right(-20)

def rotate_lights(lights):
    for light in lights:
        light.setheading(light.heading() + 2)

# Main function
def main():
    screen.tracer(0)
    lights = create_lights(screensize, LIGHTS)
    man = create_man(screensize)

    while True:
        move_lights(lights, screensize)
        screen.update()
        screen.ontimer(move_lights, 50)
        screen.ontimer(rotate_lights, 250)
        screen.ontimer(screen.update(), 0)

if __name__ == "__main__":
    main()
