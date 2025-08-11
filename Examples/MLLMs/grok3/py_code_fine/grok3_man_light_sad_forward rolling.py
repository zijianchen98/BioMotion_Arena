
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Define 15 joint positions for a human figure (simplified for forward rolling)
# Initial positions in a stick-figure-like arrangement
joints = np.array([
    [0, 0],    # pelvis
    [0.5, 0.5], [0.3, 0.5],  # shoulders and head
    [0.7, 0.2], [-0.2, 0.2],  # arms
    [0.4, -0.5], [0.1, -0.5],  # thighs
    [0.6, -1], [0, -1],        # shins
    [0.8, -0.2], [-0.4, -0.2],  # hands
    [0.5, -1.2], [0.2, -1.2],  # feet
    [0.1, 0.7], [0.4, 0.7]     # upper chest and neck
])

# Scatter plot for point lights
scatter = ax.scatter(joints[:, 0], joints[:, 1], c='white', s=50)

# Animation function
def update(frame):
    # Simulate forward rolling motion (simplified sinusoidal movement)
    angle = np.radians(frame * 5)  # Rolling motion
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation and slight vertical oscillation for realism
    center = np.mean(joints, axis=0)
    rotated_joints = np.dot(joints - center, rotation_matrix) + center
    vertical_shift = 0.1 * np.sin(np.radians(frame * 10))  # Slight bounce
    rotated_joints[:, 1] += vertical_shift
    
    # Update scatter points
    scatter.set_offsets(rotated_joints)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(0, 360, 1), interval=50, blit=True)

plt.show()
