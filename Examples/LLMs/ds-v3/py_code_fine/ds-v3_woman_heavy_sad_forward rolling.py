
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = ax.scatter([], [], color='white', s=50)

# Define the key points for a human figure (approximate positions for a sad woman with heavy weight rolling forward)
# These points will be animated to simulate the rolling motion
key_points = {
    'head': 0,
    'shoulder_left': 1,
    'shoulder_right': 2,
    'elbow_left': 3,
    'elbow_right': 4,
    'hand_left': 5,
    'hand_right': 6,
    'hip_left': 7,
    'hip_right': 8,
    'knee_left': 9,
    'knee_right': 10,
    'ankle_left': 11,
    'ankle_right': 12,
    'toe_left': 13,
    'toe_right': 14
}

# Initial positions (standing pose)
def initial_positions():
    pos = np.zeros((num_points, 2))
    # Head
    pos[0] = [0, 1.5]
    # Shoulders
    pos[1] = [-0.3, 1.3]
    pos[2] = [0.3, 1.3]
    # Elbows
    pos[3] = [-0.5, 1.1]
    pos[4] = [0.5, 1.1]
    # Hands
    pos[5] = [-0.7, 0.9]
    pos[6] = [0.7, 0.9]
    # Hips
    pos[7] = [-0.2, 0.8]
    pos[8] = [0.2, 0.8]
    # Knees
    pos[9] = [-0.2, 0.4]
    pos[10] = [0.2, 0.4]
    # Ankles
    pos[11] = [-0.2, 0.1]
    pos[12] = [0.2, 0.1]
    # Toes
    pos[13] = [-0.2, -0.1]
    pos[14] = [0.2, -0.1]
    return pos

# Function to rotate points around a center
def rotate_points(points, angle, center):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    centered = points - center
    rotated = np.dot(centered, rotation_matrix.T)
    return rotated + center

# Function to update the positions for rolling motion
def update_positions(t):
    pos = initial_positions()
    # Center of mass (approximate)
    com = np.mean(pos[[7, 8, 9, 10, 11, 12, 13, 14]], axis=0)
    # Angle varies with time (rolling forward)
    angle = -t * 0.1  # Negative for forward rolling
    # Rotate all points around the center of mass
    pos = rotate_points(pos, angle, com)
    # Add some vertical movement to simulate the rolling motion
    pos[:, 1] -= 0.05 * np.sin(t * 0.2)
    return pos

# Animation update function
def update(frame):
    t = frame * 0.1
    pos = update_positions(t)
    points.set_offsets(pos)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.tight_layout()
plt.show()
