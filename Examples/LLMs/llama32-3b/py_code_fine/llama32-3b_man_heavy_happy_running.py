
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()

# Set up the background color
ax.set_facecolor('black')

# Define the point-lights
point_lights = [
    {'x': 0.2, 'y': 0.2, 'radius': 0.01},
    {'x': 0.4, 'y': 0.4, 'radius': 0.01},
    {'x': 0.6, 'y': 0.6, 'radius': 0.01},
    {'x': 0.8, 'y': 0.8, 'radius': 0.01},
    {'x': 1, 'y': 1, 'radius': 0.01},
    {'x': 0.2, 'y': 0.8, 'radius': 0.01},
    {'x': 0.4, 'y': 0.6, 'radius': 0.01},
    {'x': 0.6, 'y': 0.4, 'radius': 0.01},
    {'x': 0.8, 'y': 0.2, 'radius': 0.01},
    {'x': 1, 'y': 0.2, 'radius': 0.01},
    {'x': 0.2, 'y': 0.4, 'radius': 0.01},
    {'x': 0.4, 'y': 0.6, 'radius': 0.01},
    {'x': 0.6, 'y': 0.8, 'radius': 0.01},
    {'x': 0.8, 'y': 1, 'radius': 0.01},
]

# Define the action parameters
action_x = [0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 2.9, 3.1, 3.3]
action_y = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Create the point-lights
for i, light in enumerate(point_lights):
    ax.add_patch(Circle((light['x'], light['y']), light['radius'], color='white'))

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    for j in range(len(point_lights)):
        x = action_x[j]
        y = action_y[j]
        ax.add_patch(Circle((x, y), point_lights[j]['radius'], color='white'))
    ax.scatter(action_x[i], action_y[i], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(point_lights), interval=50)

plt.show()
