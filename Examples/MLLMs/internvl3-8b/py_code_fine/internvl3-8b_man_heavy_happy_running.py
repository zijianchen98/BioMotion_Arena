
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Define a list of colors
colors = ["white"] * 15

# Create the lights
lights = []
for color in colors:
    light = turtle.Turtle()
    light.color(color)
    light.shape("circle")
    light.shapesize(0.5, 1)
    light.penup()
    lights.append(light)

# Define the initial positions for the lights
positions = [(i * 50, 100 - i * 50) for i in range(15)]
for light, pos in zip(lights, positions):
    light.goto(pos)

# Function for the animation
def animate():
    for light in lights:
        new_pos = light.position()
        new_pos = (new_pos[0] - 0.5, new_pos[1])
        light.goto(new_pos)
        if light.position()[1] > -100:
            turtle.ontimer(animate, 10)

# Start the animation
animate()
turtle.done()
