
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the basic position of the points for the frame of a happy woman turning around
# The positions are roughly estimated for the specific human action
point_positions = [
    [0, 10],    # Head
    [-4, 8],    # Shoulder left
    [4, 8],     # Shoulder right
    [-6, 7],    # Arm left
    [6, 7],     # Arm right
    [0, 5],     # Body center
    [-2, 4],    # Hip left
    [2, 4],     # Hip right
    [-4, 2],    # Leg left
    [4, 2],     # Leg right
    [-4, 0],    # Foot left
    [4, 0],     # Foot right
    [-1, 8],    # Chest left
    [1, 8],     # Chest right
    [-2, 6],    # Waist left
    [2, 6],     # Waist right
]

# Convert to numpy array for easier manipulation
points = np.array(point_positions)

# Function to update the frame
def update(frame):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-2, 12)
    ax.set_facecolor('black')
    angle = frame * 5  # Rotation speed
    rotation_matrix = np.array([
        [np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle))],
        [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))]
    ])
    rotated_points = np.dot(points, rotation_matrix)
    ax.scatter(rotated_points[:, 0], rotated_points[:, 1], color='white')

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Create animation
ani = FuncAnimation(fig, update, frames=range(0, 360, 5), repeat=True)

plt.show()
