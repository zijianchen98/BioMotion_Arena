
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Settings
num_points = 15
fig, ax = plt.subplots()

# Set the background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Hide axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Initial positions of points (representing joints)
points = np.array([
    [0, 1],     # Head
    [0, 0.6],   # Neck
    [0.3, 0.8], # Right Shoulder
    [-0.3, 0.8],# Left Shoulder
    [0.3, 0.5], # Right Elbow
    [-0.3, 0.5],# Left Elbow
    [0.3, 0],   # Right Wrist
    [-0.3, 0],  # Left Wrist
    [0.5, -1],  # Right Hip
    [-0.5, -1], # Left Hip
    [0.5, -1.5],# Right Knee
    [-0.5, -1.5],# Left Knee
    [0.5, -2],  # Right Ankle
    [-0.5, -2], # Left Ankle
    [0, 0],     # Center of Gravity
    [0, -1.5]   # Sitting position
])

# Create scatter plot for points
sc = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

def update(frame):
    # Update the points to simulate sitting down
    sitting_down_points = points.copy()
    sitting_down_points[1, 1] -= 0.05 * frame
    sitting_down_points[4, 1] -= 0.05 * frame
    sitting_down_points[5, 1] -= 0.05 * frame
    sitting_down_points[10, 1] += 0.05 * frame
    sitting_down_points[11, 1] += 0.05 * frame
    sitting_down_points[12, 1] -= 0.05 * frame
    
    # Update scatter plot with new points
    sc.set_offsets(sitting_down_points)
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(1, 30), interval=100, blit=True)

plt.show()
