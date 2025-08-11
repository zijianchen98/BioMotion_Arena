
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import time

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
LIGHT_RADIUS = 2

# Define the man's body and leg positions
BODY_POSITION = (WIDTH // 2, HEIGHT // 2)
LEFT_LEG_POSITION = (BODY_POSITION[0] - 100, BODY_POSITION[1] + 50)
RIGHT_LEG_POSITION = (BODY_POSITION[0] + 100, BODY_POSITION[1] + 50)

# Create the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor(BLACK)

# Create a list to hold the light positions
lights = []

# Create the point lights
for i in range(15):
    x = np.random.uniform(0, WIDTH)
    y = np.random.uniform(0, HEIGHT)
    lights.append((x, y))

# Create the circles for the lights
for light in lights:
    circle = Circle(xy=light, radius=LIGHT_RADIUS, edgecolor='white', facecolor='none', lw=2)
    ax.add_patch(circle)

# Create the man's body
body = Circle(xy=BODY_POSITION, radius=50, edgecolor='white', facecolor='none', lw=2)
ax.add_patch(body)

# Create the man's legs
left_leg = Circle(xy=LEFT_LEG_POSITION, radius=30, edgecolor='white', facecolor='none', lw=2)
ax.add_patch(left_leg)

right_leg = Circle(xy=RIGHT_LEG_POSITION, radius=30, edgecolor='white', facecolor='none', lw=2)
ax.add_patch(right_leg)

# Function to update the light positions
def update(frame):
    # Clear the axis
    ax.clear()
    ax.set_facecolor(BLACK)

    # Set the background color to black
    ax.set_facecolor(BLACK)

    # Create the point lights
    for i, light in enumerate(lights):
        # Calculate the x and y coordinates of the light
        x = np.random.uniform(0, WIDTH)
        y = np.random.uniform(0, HEIGHT)

        # Create the circle for the light
        circle = Circle(xy=(x, y), radius=LIGHT_RADIUS, edgecolor='white', facecolor='none', lw=2)
        ax.add_patch(circle)

    # Create the man's body
    body = Circle(xy=BODY_POSITION, radius=50, edgecolor='white', facecolor='none', lw=2)
    ax.add_patch(body)

    # Create the man's legs
    left_leg = Circle(xy=LEFT_LEG_POSITION, radius=30, edgecolor='white', facecolor='none', lw=2)
    ax.add_patch(left_leg)

    right_leg = Circle(xy=RIGHT_LEG_POSITION, radius=30, edgecolor='white', facecolor='none', lw=2)
    ax.add_patch(right_leg)

# Animate the lights
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the animation
plt.show()
