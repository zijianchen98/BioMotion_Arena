
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

matplotlib.use('TkAgg')  # Use an appropriate backend

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Initialize points in a standing pose
points_standing = np.array([
    [0, 1.8],    # head
    [0, 1.6],    # neck
    [-0.5, 1.5], # left shoulder
    [0.5, 1.5],  # right shoulder
    [-0.8, 1.3], # left elbow
    [0.8, 1.3],  # right elbow
    [-0.9, 1.0], # left wrist
    [0.9, 1.0],  # right wrist
    [0, 1.4],    # chest
    [-0.3, 1.0], # left hip
    [0.3, 1.0],  # right hip
    [-0.3, 0.5], # left knee
    [0.3, 0.5],  # right knee
    [-0.3, 0.0], # left ankle
    [0.3, 0.0]   # right ankle
])

# Calculate the lying down pose by rotating the standing pose 90 degrees counterclockwise
theta = np.pi / 2
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])
points_lying = np.array([rotation_matrix.dot(point) for point in points_standing])

# Create a scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white', edgecolors='white')

# Cubic easing function for smooth motion
def ease(t):
    return t * t * (3 - 2 * t)

# Update function for the animation
def update(frame):
    t = frame / 100.0
    eased_t = ease(t)
    
    # Interpolate between standing and lying poses
    points_interp = points_standing + eased_t * (points_lying - points_standing)
    
    # Update scatter plot data
    scatter.set_offsets(points_interp)
    return scatter,

# Create and show the animation
ani = FuncAnimation(fig, update, frames=100, interval=20, blit=True)
plt.title('Point-Light Stimulus: Sad Man Lying Down', color='white', fontsize=10)
plt.tight_layout()
plt.show()
