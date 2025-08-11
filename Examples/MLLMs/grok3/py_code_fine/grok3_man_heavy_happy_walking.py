
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define joint positions for a walking human (15 points)
def get_initial_positions():
    return np.array([
        [0, 10],  # Head
        [0, 7],   # Neck
        [-1, 5],  # Left shoulder
        [-2, 3],  # Left elbow
        [-3, 1],  # Left wrist
        [1, 5],   # Right shoulder
        [2, 3],   # Right elbow
        [3, 1],   # Right wrist
        [-1, 4],  # Left hip
        [-2, 2],  # Left knee
        [-2, 0],  # Left ankle
        [1, 4],   # Right hip
        [2, 2],   # Right knee
        [2, 0],   # Right ankle
        [0, 3]    # Torso center
    ])

# Update function for animation
def update(frame, points, scat):
    # Simulate walking motion with phase shift for legs and arms
    phase = frame * 0.1
    motion = np.array([
        [0, 0],  # Head
        [0, 0],  # Neck
        [-0.5 * np.sin(phase), 0],  # Left shoulder
        [-1 * np.sin(phase), -0.5 * np.cos(phase)],  # Left elbow
        [-1.5 * np.sin(phase), -1 * np.cos(phase)],  # Left wrist
        [0.5 * np.sin(phase), 0],  # Right shoulder
        [1 * np.sin(phase), -0.5 * np.cos(phase)],  # Right elbow
        [1.5 * np.sin(phase), -1 * np.cos(phase)],  # Right wrist
        [-0.5 * np.cos(phase), 0],  # Left hip
        [-1 * np.cos(phase), -1 * np.sin(phase)],  # Left knee
        [-1 * np.cos(phase), -2 * np.sin(phase)],  # Left ankle
        [0.5 * np.cos(phase), 0],  # Right hip
        [1 * np.cos(phase), -1 * np.sin(phase)],  # Right knee
        [1 * np.cos(phase), -2 * np.sin(phase)],  # Right ankle
        [0, -0.5 * np.sin(phase)]  # Torso center
    ])
    new_points = points + motion
    scat.set_offsets(new_points)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 12)
ax.axis('off')

# Initial positions
points = get_initial_positions()
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), fargs=(points, scat), interval=50, blit=True)

plt.show()
