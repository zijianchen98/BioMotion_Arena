
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the number of points
num_points = 15

# Define the positions of the point lights representing the body and weight
# Simplified positions for the happy man structure
positions = np.array([
    [0, 1.5],   # head
    [-0.5, 1],  # left shoulder
    [0.5, 1],   # right shoulder
    [-0.5, 0.5], # left elbow
    [0.5, 0.5],  # right elbow
    [-0.5, 0],  # left hand
    [0.5, 0],   # right hand
    [0, 1],     # chest
    [0, 0],     # body center (torso)
    [0, -1],    # hips
    [-0.5, -1.5], # left knee
    [0.5, -1.5],  # right knee
    [-0.5, -2],    # left foot
    [0.5, -2],     # right foot
    [-0.75, -0.5], # left weight (heavy)
    [0.75, -0.5],  # right weight (heavy)
])

# Function for updating the animation
def update(frame):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_facecolor('black')
    # Calculate the rotation angle
    angle = np.radians(frame * 5)
    # Rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate and plot the point lights
    rotated_positions = positions @ rotation_matrix
    ax.scatter(rotated_positions[:, 0], rotated_positions[:, 1], color='white')
    ax.axis('off')

# Set up the figure and axis
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=360, interval=50)

plt.show()
