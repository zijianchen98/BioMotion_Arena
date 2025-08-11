
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Define the joints of the human figure (15 points)
# Coordinates are relative to a simple stick figure
joints = np.array([
    [0, 0],     # Center of body
    [0, 5],     # Head
    [-1, 2],    # Left shoulder
    [1, 2],     # Right shoulder
    [-2, 0],    # Left elbow
    [2, 0],     # Right elbow
    [-3, -2],   # Left hand
    [3, -2],    # Right hand
    [-0.5, -2], # Left hip
    [0.5, -2],  # Right hip
    [-1, -4],   # Left knee
    [1, -4],    # Right knee
    [-1.5, -6], # Left foot
    [1.5, -6],  # Right foot
    [0, -3]     # Center of pelvis
])

# Create scatter plot for the joints
scat = ax.scatter(joints[:, 0], joints[:, 1], c='white', s=100)

# Define the waving motion (simple oscillation of right arm)
def wave_hand(frame):
    joints = np.array([
        [0, 0],
        [0, 5],
        [-1, 2],
        [1, 2],
        [-2, 0],
        [2 + 0.5 * np.sin(frame * 0.1), 0],
        [-3, -2],
        [3 + 1.5 * np.sin(frame * 0.1), -2],
        [-0.5, -2],
        [0.5, -2],
        [-1, -4],
        [1, -4],
        [-1.5, -6],
        [1.5, -6],
        [0, -3]
    ])
    return joints

# Update function for animation
def update(frame):
    points = wave_hand(frame)
    scat.set_offsets(points)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show animation
plt.show()
