
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])

# Define 15 point-light positions for a simplified human figure (head, torso, arms, legs)
# Initial positions for a sadman with arms slightly raised for waving
points = np.array([
    [0, 0.8],    # Head
    [0, 0.6],    # Neck
    [0, 0.4],    # Chest
    [0, 0.2],    # Pelvis
    [-0.2, 0.6], # Left shoulder
    [-0.4, 0.6], # Left elbow
    [-0.6, 0.6], # Left hand
    [0.2, 0.6],  # Right shoulder
    [0.4, 0.6],  # Right elbow
    [0.6, 0.6],  # Right hand (waving)
    [-0.1, 0],   # Left knee
    [-0.2, -0.4],# Left ankle
    [0.1, 0],    # Right knee
    [0.2, -0.4], # Right ankle
    [0, -0.6]    # Base
])

# Scatter plot for point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Animation function
def update(frame):
    # Wave motion for right hand (index 9)
    angle = np.sin(frame * 0.2) * 0.3  # Smooth waving motion
    points[9] = [0.6 + angle, 0.6]     # Right hand moves slightly
    
    # Slight torso and shoulder movement for realism
    points[2] = [0, 0.4 + np.sin(frame * 0.1) * 0.02]  # Chest
    points[5] = [-0.4 + np.sin(frame * 0.1) * 0.02, 0.6]  # Left elbow
    points[7] = [0.2 + np.sin(frame * 0.1) * 0.02, 0.6]   # Right shoulder
    
    # Leg movement (subtle for sadman walking slowly)
    points[10] = [-0.1 + np.cos(frame * 0.1) * 0.05, 0]  # Left knee
    points[12] = [0.1 + np.cos(frame * 0.1 + np.pi) * 0.05, 0]  # Right knee
    
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
