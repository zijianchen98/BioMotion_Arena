
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
# We'll use a simplified model of a human body with 15 joints
# The x, y coordinates are in a 2D space, with the origin at the center
point_lights = np.array([
    [-0.3, 0.5],  # Head
    [-0.2, 0.4],  # Right shoulder
    [0.2, 0.4],   # Left shoulder
    [-0.1, 0.3],  # Right elbow
    [0.1, 0.3],   # Left elbow
    [-0.2, 0.2],  # Right hand
    [0.2, 0.2],   # Left hand
    [0, 0.1],     # Hip
    [-0.1, 0],    # Right knee
    [0.1, 0],     # Left knee
    [-0.2, -0.1], # Right ankle
    [0.2, -0.1],  # Left ankle
    [-0.1, -0.2], # Right foot
    [0.1, -0.2],  # Left foot
    [0, -0.3]     # Center of mass
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the positions of the point-lights based on the frame number
    # We'll use a simple rotation to simulate the woman turning around
    angle = np.radians(frame * 2)
    rotated_point_lights = np.copy(point_lights)
    rotated_point_lights[:, 0] = point_lights[:, 0] * np.cos(angle) - point_lights[:, 1] * np.sin(angle)
    rotated_point_lights[:, 1] = point_lights[:, 0] * np.sin(angle) + point_lights[:, 1] * np.cos(angle)

    # Plot the point-lights
    ax.scatter(rotated_point_lights[:, 0], rotated_point_lights[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(180), interval=50)

plt.show()
