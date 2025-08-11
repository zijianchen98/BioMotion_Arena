
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human figure walking)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles
def initial_positions():
    return np.array([
        [0, 10],  # head
        [-2, 8], [-2, 8],  # left shoulder, right shoulder
        [-4, 6], [-4, 6],  # left elbow, right elbow
        [-6, 4], [-6, 4],  # left wrist, right wrist
        [0, 0], [0, 0],  # left hip, right hip
        [-2, -2], [-2, -2],  # left knee, right knee
        [-4, -4], [-4, -4]   # left ankle, right ankle
    ])

# Update function for animation
def update(frame):
    # Simulate walking motion with sinusoidal movement for legs and arms
    t = frame * 0.1
    positions = initial_positions().copy()
    
    # Arm movement
    positions[2] = [-2 - np.sin(t) * 2, 8]  # left shoulder
    positions[3] = [-4 - np.sin(t) * 2, 6]  # left elbow
    positions[4] = [-6 - np.sin(t) * 2, 4]  # left wrist
    positions[6] = [2 + np.sin(t) * 2, 8]   # right shoulder
    positions[7] = [4 + np.sin(t) * 2, 6]   # right elbow
    positions[8] = [6 + np.sin(t) * 2, 4]   # right wrist
    
    # Leg movement (opposite phase for natural walk)
    positions[10] = [0 - np.cos(t) * 2, 0]  # left hip
    positions[11] = [-2 - np.cos(t) * 2, -2]  # left knee
    positions[12] = [-4 - np.cos(t) * 2, -4]  # left ankle
    positions[13] = [0 + np.cos(t) * 2, 0]  # right hip
    positions[14] = [2 + np.cos(t) * 2, -2]  # right knee
    positions[15] = [4 + np.cos(t) * 2, -4]  # right ankle
    
    scat.set_offsets(positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-8, 8)
ax.set_ylim(-6, 16)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
