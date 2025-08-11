
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)
RUNNING_STEPS = 100
RUNNING_SPEED = 1.0

# Create a new figure
fig, ax = plt.subplots()

# Initialize the point lights
point_lights = []
for i in range(15):
    light = plt.Line2D([0, WIDTH], [0, 0], color=WHITE_COLOR, lw=2)
    point_lights.append(light)

# Set the axis limits
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Function to update the point lights
def update(frame):
    # Clear the previous frame
    ax.clear()

    # Update the point lights
    for light in point_lights:
        light.set_data([light.get_xdata()[0], WIDTH], [light.get_ydata()[0], 0])

    # Set the axis limits
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')

    # Set the text for the sadwoman
    ax.text(WIDTH / 2, HEIGHT / 2, 'Sadwoman', color=BLACK_COLOR, ha='center')

    # Set the step counter
    ax.text(0, HEIGHT / 2, f'Step: {frame + 1}', color=WHITE_COLOR, ha='center')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=RUNNING_STEPS, interval=20)

# Show the animation
plt.show()
