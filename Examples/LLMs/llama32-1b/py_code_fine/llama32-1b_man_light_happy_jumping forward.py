
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_COUNT = 15

# Initialize figure and axis
fig, ax = plt.subplots()

# Initialize point lights
lights = []
for i in range(LIGHT_COUNT):
    light = plt.Line2D([0, WIDTH], [0, 0], color=WHITE, lw=1, alpha=0.5)
    ax.add_line(light)
    lights.append(light)

# Set axis limits and aspect ratio
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

# Function to update point lights
def update(frame):
    for light in lights:
        light.set_data((frame % WIDTH, frame // WIDTH))
    return ax,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Show animation
plt.show()
