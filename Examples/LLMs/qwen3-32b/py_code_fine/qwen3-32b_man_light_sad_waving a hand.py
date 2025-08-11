
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.axis('off')

# Define the skeleton structure (15 joints)
# Each joint is a list of [x, y] coordinates
skeleton = []

# Create a simple stick figure for a sad man waving a hand
def reset_skeleton(t):
    # t is a time parameter to animate the waving
    # Head
    skeleton[0] = [0, 60]
    # Torso center
    skeleton[1] = [0, 30]
    # Left shoulder
    skeleton[2] = [-20, 30]
    # Right shoulder
    skeleton[3] = [20, 30]
    # Left elbow
    skeleton[4] = [-40, 10]
    # Right elbow
    skeleton[5] = [40, 10]
    # Left hand (waving)
    skeleton[6] = [-60, 0 + 10 * math.sin(t * 2)]
    # Right hand (still)
    skeleton[7] = [60, 0]
    # Left hip
    skeleton[8] = [-10, 0]
    # Right hip
    skeleton[9] = [10, 0]
    # Left knee
    skeleton[10] = [-10, -40]
    # Right knee
    skeleton[11] = [10, -40]
    # Left foot
    skeleton[12] = [-10, -70]
    # Right foot
    skeleton[13] = [10, -70]
    # Neck (between head and torso)
    skeleton[14] = [0, 45]

# Initialize the 15 point lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(15)]

# Animation update function
def update(frame):
    reset_skeleton(frame * 0.1)  # Smooth waving motion
    for i, point in enumerate(points):
        point.set_data(skeleton[i][0], skeleton[i][1])
    return points

# Initialize the skeleton with zeros
skeleton = [[0, 0] for _ in range(15)]

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
