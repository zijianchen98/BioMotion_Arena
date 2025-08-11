
import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Define the initial positions and colors for the points
points = [
    {'x': -150, 'y': 0, 'color': 'white'},
    {'x': -130, 'y': 0, 'color': 'white'},
    {'x': -110, 'y': 0, 'color': 'white'},
    {'x': -90, 'y': 0, 'color': 'white'},
    {'x': -70, 'y': 0, 'color': 'white'},
    {'x': -50, 'y': 0, 'color': 'white'},
    {'x': -30, 'y': 0, 'color': 'white'},
    {'x': -10, 'y': 0, 'color': 'white'},
    {'x': 10, 'y': 0, 'color': 'white'},
    {'x': 30, 'y': 0, 'color': 'white'},
    {'x': 50, 'y': 0, 'color': 'white'},
    {'x': 70, 'y': 0, 'color': 'white'},
    {'x': 90, 'y': 0, 'color': 'white'},
    {'x': 110, 'y': 0, 'color': 'white'},
    {'x': 130, 'y': 0, 'color': 'white'},
]

# Create turtle objects for each point
turtles = []
for point in points:
    t = turtle.Turtle()
    t.shape("circle")
    t.color(point['color'])
    t.penup()
    t.goto(point['x'], point['y'])
    t.speed(0)
    turtles.append(t)

# Function to move the points
def move_points():
    for t in turtles:
        t.forward(10)
        t.setheading(t.heading() + 10)
        if t.heading() > 180:
            t.setheading(t.heading() - 360)

    # Clear the screen and redraw the points
    screen.clear()
    for t in turtles:
        t.goto(t.xcor(), t.ycor())
    
    # Keep the screen updated
    screen.update()

# Animation loop
while True:
    move_points()
    time.sleep(0.1)

turtle.done()
