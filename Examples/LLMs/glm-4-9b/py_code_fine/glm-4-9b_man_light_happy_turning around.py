
import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happyman Point-Light Stimulus Animation")

# Create turtle object for drawing
happyman = turtle.Turtle()
happyman.color("white")
happyman.shape("circle")
happyman.shapesize(0.1, 0.1)  # Small point-light size
happyman.speed(0)  # Fastest animation speed

# Define coordinates for the 15 point-lights (initial positions)
num_lights = 15
lights = []
radius = 100  # Radius of circular path
center_x, center_y = 0, 0

# Function to update the position of the lights
def update_lights(angle):
    for light in lights:
        light.clear()
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        light.goto(x, y)

# Create the initial point-lights
for i in range(num_lights):
    light = turtle.Turtle()
    light.color("white")
    light.shape("circle")
    light.shapesize(0.1, 0.1)
    light.speed(0)
    angle = (360 / num_lights) * i
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    light.goto(x, y)
    lights.append(light)

# Animation loop for "turning around"
duration = 10  # Duration of the animation in seconds
fps = 60  # Frames per second
frames = duration * fps
angle Increment = 360 / frames

for _ in range(frames):
    update_lights(math.degrees(math.atan2(center_y, center_x)) - _ * angle Increment)
    screen.update()

# Clean up
screen.mainloop()
