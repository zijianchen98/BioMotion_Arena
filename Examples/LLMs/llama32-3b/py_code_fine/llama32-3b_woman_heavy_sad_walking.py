
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
NUM_LIGHTS = 15
LIGHT_SIZE = 5
LIGHT_COLOR = (1, 1, 1)
BACKGROUND_COLOR = (0, 0, 0)

# Define the figure and axis
fig, ax = plt.subplots(figsize=(WIDTH, HEIGHT))

# Initialize the lights
lights = []
for i in range(NUM_LIGHTS):
    x = i * (LIGHT_SIZE + 10)
    y = HEIGHT // 2
    lights.append(ax.add_patch(plt.Circle((x, y), LIGHT_SIZE, color=LIGHT_COLOR, alpha=0.5)))

# Set the background color
ax.set_facecolor(BACKGROUND_COLOR)

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the background color
    ax.set_facecolor(BACKGROUND_COLOR)

    # Define the movement parameters
    dx = np.cos(2 * np.pi * i / 100)
    dy = np.sin(2 * np.pi * i / 100)

    # Move the lights
    for j, light in enumerate(lights):
        x = j * (LIGHT_SIZE + 10) + LIGHT_SIZE * (1 + dx * 0.5)
        y = HEIGHT // 2 + LIGHT_SIZE * (1 + dy * 0.5)
        light.center = (x, y)

    # Set the limits
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)

    # Set the aspect ratio
    ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# Show the animation
plt.show()
