
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point lights (simplified human stick figure)
def init_positions():
    # Head, torso, hips, shoulders, elbows, wrists, knees, ankles
    return np.array([
        [0, 10],  # Head
        [0, 8],   # Upper torso
        [0, 4],   # Lower torso
        [0, 7],   # Left shoulder
        [-2, 6],  # Left elbow
        [-3, 5],  # Left wrist
        [0, 7],   # Right shoulder
        [2, 6],   # Right elbow
        [3, 5],   # Right wrist
        [0, 4],   # Left hip
        [-1, 2],  # Left knee
        [-1, 0],  # Left ankle
        [0, 4],   # Right hip
        [1, 2],   # Right knee
        [1, 0]    # Right ankle
    ])

# Update function for animation
def update(frame, points, scat):
    # Simulate walking motion with sinusoidal movement for limbs
    t = frame * 0.1
    offsets = np.zeros((15, 2))
    # Head and torso move slightly forward
    offsets[0:3, 0] = t  # Move forward
    # Arm swing (left and right arms)
    offsets[4, 1] = np.sin(t) * 2  # Left elbow
    offsets[5, 1] = np.sin(t) * 3  # Left wrist
    offsets[7, 1] = -np.sin(t) * 2  # Right elbow
    offsets[8, 1] = -np.sin(t) * 3  # Right wrist
    # Leg swing (left and right legs)
    offsets[10, 1] = np.sin(t + np.pi/2) * 2  # Left knee
    offsets[11, 1] = np.sin(t + np.pi/2) * 3  # Left ankle
    offsets[13, 1] = -np.sin(t + np.pi/2) * 2  # Right knee
    offsets[14, 1] = -np.sin(t + np.pi/2) * 3  # Right ankle
    
    # Update positions
    new_points = points + offsets
    scat.set_offsets(new_points)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 12)
ax.axis('off')

# Initial positions
points = init_positions()
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), fargs=(points, scat),
                    interval=50, blit=True)

plt.show()
