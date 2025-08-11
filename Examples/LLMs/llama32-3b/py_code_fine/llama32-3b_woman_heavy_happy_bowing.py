
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import time

# Set up the figure and axis
fig, ax = plt.subplots()

# Set up the background and axis limits
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Define the point-light positions and radii
point_light_positions = np.array([
    [-4.5, -4.5],  # 1
    [-4.5, -2.5],  # 2
    [-4.5, 0.5],   # 3
    [-4.5, 2.5],   # 4
    [-4.5, 4.5],   # 5
    [-3.5, -4.5],  # 6
    [-3.5, -2.5],  # 7
    [-3.5, 0.5],   # 8
    [-3.5, 2.5],   # 9
    [-3.5, 4.5],   # 10
    [-2.5, -4.5],  # 11
    [-2.5, -2.5],  # 12
    [-2.5, 0.5],   # 13
    [-2.5, 2.5],   # 14
    [-1.5, -4.5],  # 15
])

point_light_radii = np.array([0.2] * 15)

# Create the point lights
point_lights = []
for i in range(15):
    point_light = Circle((point_light_positions[i, 0], point_light_positions[i, 1]), point_light_radii[i], edgecolor='white', facecolor='white', zorder=10)
    point_lights.append(point_light)
    ax.add_patch(point_light)

# Set up the animation
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set up the background and axis limits
    ax.set_facecolor('black')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # Define the point-light positions and radii
    point_light_positions = np.array([
        [-4.5, -4.5],  # 1
        [-4.5, -2.5],  # 2
        [-4.5, 0.5],   # 3
        [-4.5, 2.5],   # 4
        [-4.5, 4.5],   # 5
        [-3.5, -4.5],  # 6
        [-3.5, -2.5],  # 7
        [-3.5, 0.5],   # 8
        [-3.5, 2.5],   # 9
        [-3.5, 4.5],   # 10
        [-2.5, -4.5],  # 11
        [-2.5, -2.5],  # 12
        [-2.5, 0.5],   # 13
        [-2.5, 2.5],   # 14
        [-1.5, -4.5],  # 15
    ])

    point_light_radii = np.array([0.2] * 15)

    # Create the point lights
    point_lights = []
    for i in range(15):
        point_light = Circle((point_light_positions[i, 0], point_light_positions[i, 1]), point_light_radii[i], edgecolor='white', facecolor='white', zorder=10)
        point_lights.append(point_light)
        ax.add_patch(point_light)

    # Update the positions of the point lights
    for i in range(15):
        angle = np.radians(10 * i)
        x = point_light_positions[i, 0] + 5 * np.cos(angle)
        y = point_light_positions[i, 1] + 5 * np.sin(angle)
        point_light_positions[i, 0] = x
        point_light_positions[i, 1] = y

    # Draw the point lights
    for point_light in point_lights:
        ax.add_patch(point_light)

# Animate the point lights
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
