
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define 15 point-light positions for a human figure (sad man waving hand)
# Initial positions based on a simplified human stick figure
points = np.array([
    [0, 0],      # Torso center
    [0.1, 0.2],  # Head
    [-0.2, -0.1], [-0.1, -0.3],  # Left arm (shoulder, elbow)
    [0.2, -0.1], [0.3, -0.3],    # Right arm (shoulder, elbow, waving)
    [-0.1, -0.5], [0, -0.8],     # Left leg (hip, knee)
    [0.1, -0.5], [0.2, -0.8],    # Right leg (hip, knee)
    [-0.15, 0.1], [0, 0.1],      # Shoulders
    [0.15, 0.1], [0.05, -0.1]    # Additional points for natural motion
])

scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Animation function
def update(frame):
    # Wave motion for right arm
    angle = np.sin(frame * 0.2) * 0.3
    points[4] = [0.2 + 0.1 * np.cos(angle), -0.1 + 0.1 * np.sin(angle)]  # Shoulder
    points[5] = [0.3 + 0.15 * np.cos(angle + 0.5), -0.3 + 0.15 * np.sin(angle + 0.5)]  # Elbow
    
    # Slight torso sway for sadness
    points[0] = [0 + 0.05 * np.sin(frame * 0.1), 0]  # Torso center
    
    # Leg movement for walking slowly
    points[6] = [-0.1 + 0.05 * np.sin(frame * 0.1), -0.5 - 0.1 * np.cos(frame * 0.1)]  # Left hip
    points[7] = [0 + 0.05 * np.sin(frame * 0.1), -0.8 - 0.1 * np.cos(frame * 0.1)]     # Left knee
    points[8] = [0.1 - 0.05 * np.sin(frame * 0.1), -0.5 + 0.1 * np.cos(frame * 0.1)]  # Right hip
    points[9] = [0.2 - 0.05 * np.sin(frame * 0.1), -0.8 + 0.1 * np.cos(frame * 0.1)]  # Right knee
    
    # Update shoulder and additional points
    points[10] = [-0.15 + 0.02 * np.sin(frame * 0.1), 0.1]  # Left shoulder
    points[11] = [0 + 0.02 * np.sin(frame * 0.1), 0.1]      # Center shoulder
    points[12] = [0.15 + 0.02 * np.sin(frame * 0.1), 0.1]   # Right shoulder
    points[13] = [0.05 + 0.02 * np.sin(frame * 0.1), -0.1]  # Torso point
    
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
