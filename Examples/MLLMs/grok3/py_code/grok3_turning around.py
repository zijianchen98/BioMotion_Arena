
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define joint positions for a turning man (simplified 2D representation)
# Initial positions of 15 point-lights (head, torso, arms, legs, etc.)
joints = np.array([
    [0, 10],    # Head
    [0, 8],     # Neck
    [0, 6],     # Chest
    [0, 4],     # Pelvis
    [-1, 3],    # Left hip
    [-1, 1],    # Left knee
    [-1, 0],    # Left ankle
    [1, 3],     # Right hip
    [1, 1],     # Right knee
    [1, 0],     # Right ankle
    [-2, 6],    # Left shoulder
    [-3, 4],    # Left elbow
    [-4, 2],    # Left wrist
    [2, 6],     # Right shoulder
    [3, 4]      # Right elbow
])

# Number of frames for one full turn (e.g., 360 degrees)
n_frames = 60
theta = np.linspace(0, 2 * np.pi, n_frames)

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 11)
ax.axis('off')

# Scatter plot for point-lights
scatter = ax.scatter([], [], c='white', s=100)

def update(frame):
    # Rotate all joints around the origin
    angle = theta[frame]
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_joints = np.dot(joints - [0, 6], rotation_matrix) + [0, 6]
    
    # Update scatter data
    scatter.set_offsets(rotated_joints)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
