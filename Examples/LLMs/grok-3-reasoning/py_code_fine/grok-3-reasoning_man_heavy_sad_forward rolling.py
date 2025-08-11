
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define standing positions for the 15 points (x, y coordinates in meters)
points_standing = [
    (0, 1.8),    # head
    (0, 1.6),    # neck
    (-0.2, 1.5), # left shoulder
    (0.2, 1.5),  # right shoulder
    (-0.4, 1.3), # left elbow
    (0.4, 1.3),  # right elbow
    (-0.5, 1.1), # left wrist
    (0.5, 1.1),  # right wrist
    (0, 1.0),    # waist
    (-0.1, 0.9), # left hip
    (0.1, 0.9),  # right hip
    (-0.1, 0.5), # left knee
    (0.1, 0.5),  # right knee
    (-0.1, 0.1), # left ankle
    (0.1, 0.1)   # right ankle
]

# Define tucked positions for the 15 points during the roll
points_tucked = [
    (0, 0.6),    # head
    (0, 0.7),    # neck
    (-0.1, 0.8), # left shoulder
    (0.1, 0.8),  # right shoulder
    (-0.2, 0.7), # left elbow
    (0.2, 0.7),  # right elbow
    (-0.3, 0.6), # left wrist
    (0.3, 0.6),  # right wrist
    (0, 0.5),    # waist
    (-0.1, 0.4), # left hip
    (0.1, 0.4),  # right hip
    (-0.2, 0.3), # left knee
    (0.2, 0.3),  # right knee
    (-0.3, 0.2), # left ankle
    (0.3, 0.2)   # right ankle
]

# Convert lists to numpy arrays for vectorized operations
points_standing = np.array(points_standing)
points_tucked = np.array(points_tucked)

# Define 2D rotation matrix for a given angle theta
def R(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], 
                     [np.sin(theta), np.cos(theta)]])

# Compute positions of all 15 points at a given rotation angle theta
def get_positions(theta, r=0.3):
    # Interpolation parameter: 0 (standing) to 1 (tucked) and back to 0
    k = (1 - np.cos(theta)) / 2
    # Interpolate between standing and tucked positions
    positions_local = (1 - k) * points_standing + k * points_tucked
    # Apply rotation
    positions = positions_local @ R(theta).T
    # Apply translation (forward movement)
    d = np.array([r * theta, 0])
    positions += d
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Solid black background
ax.set_xlim(-1, 4)         # x-axis range to accommodate roll
ax.set_ylim(-1, 2)         # y-axis range for height
ax.set_aspect('equal')     # Equal aspect ratio for realistic motion
ax.axis('off')             # Hide axes

# Initialize scatter plot with 15 white points
scatter = ax.scatter([], [], color='white', s=50)

# Animation update function
def update(frame):
    theta = 2 * np.pi * frame / num_frames  # Full rotation over animation
    positions = get_positions(theta)
    scatter.set_offsets(positions)
    return scatter,

# Animation parameters
num_frames = 100  # Number of frames for smooth motion
interval = 50     # Milliseconds per frame (~20 fps)

# Create and run the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, 
                    blit=True, repeat=True)

plt.show()
