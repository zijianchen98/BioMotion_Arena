
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Define the point lights
lights = [
    {'x': 0.1, 'y': 0.1, 'radius': 0.01},
    {'x': 0.2, 'y': 0.2, 'radius': 0.01},
    {'x': 0.3, 'y': 0.3, 'radius': 0.01},
    {'x': 0.4, 'y': 0.4, 'radius': 0.01},
    {'x': 0.5, 'y': 0.5, 'radius': 0.01},
    {'x': 0.6, 'y': 0.6, 'radius': 0.01},
    {'x': 0.7, 'y': 0.7, 'radius': 0.01},
    {'x': 0.8, 'y': 0.8, 'radius': 0.01},
    {'x': 0.9, 'y': 0.9, 'radius': 0.01},
    {'x': 0.1, 'y': 0.9, 'radius': 0.01},
    {'x': 0.2, 'y': 0.8, 'radius': 0.01},
    {'x': 0.3, 'y': 0.7, 'radius': 0.01},
    {'x': 0.4, 'y': 0.6, 'radius': 0.01},
    {'x': 0.5, 'y': 0.5, 'radius': 0.01},
    {'x': 0.6, 'y': 0.4, 'radius': 0.01},
]

# Define the action (lying down)
def lying_down(t):
    for i, light in enumerate(lights):
        # Move the points in a circular motion
        light['x'] = 0.5 + 0.2 * np.cos(2 * np.pi * (i + t) / 10)
        light['y'] = 0.5 + 0.2 * np.sin(2 * np.pi * (i + t) / 10)

# Define the update function for the animation
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    lying_down(frame)
    for light in lights:
        circle = patches.Circle((light['x'], light['y']), light['radius'], edgecolor='white', facecolor='white', alpha=0.5)
        ax.add_patch(circle)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Display the animation
plt.show()
