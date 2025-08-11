
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 point-light positions for a sad man turning around
# These are approximate coordinates based on a human figure
# Positions are relative to the center of the figure

# Initial positions (simplified human figure)
initial_positions = np.array([
    [0.3, 0.3],  # head
    [0.2, 0.1],  # upper chest
    [0.1, -0.1], # lower chest
    [0.0, -0.3], # waist
    [-0.1, -0.5], # left hip
    [-0.3, -0.3], # left knee
    [-0.5, -0.1], # left ankle
    [0.1, -0.5], # right hip
    [0.3, -0.3], # right knee
    [0.5, -0.1], # right ankle
    [-0.2, 0.2], # left shoulder
    [-0.1, 0.4], # left elbow
    [0.1, 0.4], # right shoulder
    [0.2, 0.2], # right elbow
    [0.0, 0.0]  # center of mass
])

# Define a function to animate the turning motion
def animate(i):
    # Simulate turning around by rotating the points
    angle = np.radians(360 * i / 100)
    rotated = np.dot(initial_positions, np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ]))

    # Apply a slight translation to simulate turning around
    rotated += np.array([0, 0.5 * np.sin(angle)])

    # Update the positions of the point lights
    for j in range(15):
        circle = circles[j]
        circle.center = rotated[j]

# Create the point light circles
circles = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for circle in circles:
    ax.add_patch(circle)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
