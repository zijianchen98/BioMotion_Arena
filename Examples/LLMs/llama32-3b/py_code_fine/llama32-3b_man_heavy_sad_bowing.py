
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the figure and axis
fig, ax = plt.subplots()

# Define the point lights
points = [
    [0.2, 0.2],  # top left
    [0.2, 0.8],  # top right
    [0.8, 0.8],  # bottom right
    [0.8, 0.2],  # bottom left
    [0.4, 0.1],  # top center
    [0.4, 0.9],  # bottom center
    [0.6, 0.1],  # left center
    [0.6, 0.9],  # right center
    [0.5, 0.5],  # center
    [0.1, 0.5],  # left center
    [0.9, 0.5],  # right center
    [0.4, 0.4],  # center
    [0.4, 0.6],  # center
    [0.5, 0.4],  # center
    [0.5, 0.6],  # center
]

# Define the action
action = [
    [0.2, 0.2],  # start
    [0.2, 0.3],  # start
    [0.2, 0.4],  # start
    [0.2, 0.5],  # start
    [0.2, 0.6],  # start
    [0.2, 0.7],  # start
    [0.2, 0.8],  # start
    [0.2, 0.9],  # start
    [0.2, 0.95],  # start
    [0.2, 0.98],  # start
    [0.2, 0.99],  # start
    [0.2, 0.995],  # start
    [0.2, 0.99],  # start
    [0.2, 0.995],  # start
    [0.2, 0.99],  # start
    [0.2, 0.995],  # start
]

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    # Draw the point lights
    for point in points:
        circle = Circle(point, 0.01, edgecolor='white', facecolor='white', zorder=1)
        ax.add_patch(circle)

    # Update the point lights
    for j in range(len(points)):
        x = action[j][0]
        y = action[j][1]
        points[j] = [x, y]
        circle = Circle(points[j], 0.01, edgecolor='white', facecolor='white', zorder=1)
        ax.add_patch(circle)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
