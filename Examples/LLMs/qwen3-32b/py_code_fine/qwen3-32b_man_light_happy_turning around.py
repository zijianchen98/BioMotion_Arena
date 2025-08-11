
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Define the number of points
num_points = 15

# Define the positions of the point-lights (relative to the center)
# These positions represent a simplified stick figure with 15 points
# (head, torso, hips, and limbs)
positions = np.array([
    [0.0, 0.5],  # head
    [0.0, 0.2],  # neck
    [0.0, 0.0],  # torso center
    [0.0, -0.2], # pelvis
    [0.2, -0.3], # right hip
    [0.5, -0.3], # right knee
    [0.7, -0.2], # right ankle
    [-0.2, -0.3], # left hip
    [-0.5, -0.3], # left knee
    [-0.7, -0.2], # left ankle
    [0.2, 0.1],  # right shoulder
    [0.4, 0.1],  # right elbow
    [0.6, 0.0],  # right wrist
    [-0.2, 0.1], # left shoulder
    [-0.4, 0.1], # left elbow
    [-0.6, 0.0], # left wrist
])

# Define a function to rotate a point around the origin
def rotate_point(point, angle):
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])
    return np.dot(rotation_matrix, point)

# Define a function to update the positions of the point-lights
def update(frame):
    angle = frame * 0.05  # Adjust the rotation speed
    rotated_positions = np.array([rotate_point(p, angle) for p in positions])
    scat.set_offsets(rotated_positions)
    return scat,

# Create the scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Create the animation
animation = FuncAnimation(fig, update, frames=120, interval=50, blit=True)

# Display the animation
plt.show()
