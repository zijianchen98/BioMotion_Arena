
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point positions (x, y)
points = np.zeros((num_points, 2))
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Define key body points (approximate for a turning motion)
# Head, shoulders, elbows, hands, hips, knees, feet
body_points = {
    'head': 0,
    'left_shoulder': 1,
    'right_shoulder': 2,
    'left_elbow': 3,
    'right_elbow': 4,
    'left_hand': 5,
    'right_hand': 6,
    'hip_center': 7,
    'left_hip': 8,
    'right_hip': 9,
    'left_knee': 10,
    'right_knee': 11,
    'left_ankle': 12,
    'right_ankle': 13,
    'torso_mid': 14
}

# Initial positions (facing forward)
def initial_positions():
    positions = np.zeros((num_points, 2))
    # Head
    positions[body_points['head']] = [0, 1.5]
    # Shoulders
    positions[body_points['left_shoulder']] = [-0.5, 1.2]
    positions[body_points['right_shoulder']] = [0.5, 1.2]
    # Elbows
    positions[body_points['left_elbow']] = [-0.7, 0.9]
    positions[body_points['right_elbow']] = [0.7, 0.9]
    # Hands
    positions[body_points['left_hand']] = [-0.9, 0.6]
    positions[body_points['right_hand']] = [0.9, 0.6]
    # Hips
    positions[body_points['hip_center']] = [0, 0.7]
    positions[body_points['left_hip']] = [-0.3, 0.7]
    positions[body_points['right_hip']] = [0.3, 0.7]
    # Knees
    positions[body_points['left_knee']] = [-0.3, 0.2]
    positions[body_points['right_knee']] = [0.3, 0.2]
    # Ankles
    positions[body_points['left_ankle']] = [-0.3, -0.3]
    positions[body_points['right_ankle']] = [0.3, -0.3]
    # Torso mid
    positions[body_points['torso_mid']] = [0, 1.0]
    return positions

# Function to rotate points around the y-axis (simulate turning)
def rotate_points(positions, angle):
    rotated = np.zeros_like(positions)
    for i in range(len(positions)):
        x, y = positions[i]
        # Rotate around the origin (0,0) for simplicity
        rotated[i, 0] = x * math.cos(angle) - y * math.sin(angle)
        rotated[i, 1] = x * math.sin(angle) + y * math.cos(angle)
    return rotated

# Animation update function
def update(frame):
    angle = frame * 0.05  # Control rotation speed
    positions = initial_positions()
    # Apply rotation
    rotated_positions = rotate_points(positions, angle)
    # Update scatter plot data
    scatter.set_offsets(rotated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.tight_layout()
plt.show()
