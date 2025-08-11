
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions and movements of 15 point-lights for a walking man
# These are approximate coordinates and velocities based on biomechanical data
# Adjusted to mimic the example image with 15 points

# Initial positions for 15 joints (head, shoulders, elbows, wrists, hips, knees, ankles, etc.)
points = np.array([
    [0, 10],  # Head
    [-2, 8],  # Left shoulder
    [-4, 6],  # Left elbow
    [-6, 4],  # Left wrist
    [2, 8],   # Right shoulder
    [4, 6],   # Right elbow
    [6, 4],   # Right wrist
    [-1, 0],  # Left hip
    [-2, -2], # Left knee
    [-3, -4], # Left ankle
    [1, 0],   # Right hip
    [2, -2],  # Right knee
    [3, -4],  # Right ankle
    [0, 2],   # Chest
    [0, 6]    # Neck
])

# Velocities for walking motion (x, y) - cyclic and biomechanical
velocities = np.array([
    [0.1, 0],   # Head
    [-0.1, -0.1], [-0.2, -0.2], [-0.3, -0.3],  # Left arm
    [0.1, -0.1], [0.2, -0.2], [0.3, -0.3],     # Right arm
    [-0.1, -0.2], [-0.2, -0.3], [-0.3, -0.4],  # Left leg
    [0.1, -0.2], [0.2, -0.3], [0.3, -0.4],     # Right leg
    [0, -0.1], [0, -0.1]                       # Chest, Neck
])

# Animation setup
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-8, 8)
ax.set_ylim(-6, 16)
ax.axis('off')
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Animation update function
def update(frame):
    global points, velocities
    # Update positions with cyclic motion
    points += velocities * 0.1  # Small step for smooth motion
    
    # Simple bounce back for legs and arms to simulate walking cycle
    for i in [2, 3, 5, 6, 8, 9, 11, 12]:  # Elbows, wrists, knees, ankles
        if points[i, 1] < -4 or points[i, 1] > 4:
            velocities[i] *= -1
    
    # Keep torso and head within bounds
    for i in [0, 13, 14]:  # Head, chest, neck
        if points[i, 0] < -2 or points[i, 0] > 2:
            velocities[i, 0] *= -1
        if points[i, 1] < 0 or points[i, 1] > 10:
            velocities[i, 1] *= -1
    
    scat.set_offsets(points)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
