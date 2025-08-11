
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points (joints)
# These points represent a simplified human figure
initial_positions = np.array([
    # Head
    [0, 1],
    # Shoulders
    [-0.5, 0], [0.5, 0],
    # Elbows
    [-1, -0.5], [1, -0.5],
    # Wrists
    [-1.5, -1], [1.5, -1],
    # Hips
    [-0.3, -1.5], [0.3, -1.5],
    # Knees
    [-0.8, -2.5], [0.8, -2.5],
    # Ankles
    [-1.2, -3.5], [1.2, -3.5]
])

# Function to rotate a point around the origin
def rotate_point(point, angle):
    """Rotate a 2D point around the origin."""
    x, y = point
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    rotated_x = x * cos_theta - y * sin_theta
    rotated_y = x * sin_theta + y * cos_theta
    return np.array([rotated_x, rotated_y])

# Function to update the animation frame
def update(frame):
    """Update the positions of the points for each frame."""
    angle = np.radians(frame * 2)  # Rotate by 2 degrees per frame
    rotated_points = np.array([rotate_point(p, angle) for p in initial_positions])
    
    # Update the scatter plot data
    scatter.set_offsets(rotated_points)
    return scatter,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide the axes
ax.set_aspect('equal')  # Ensure aspect ratio is equal for proper rotation

# Plot the initial points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create the animation
animation = FuncAnimation(fig, update, frames=180, interval=30, blit=True)  # 180 frames for a full rotation

# Display the animation
plt.show()
