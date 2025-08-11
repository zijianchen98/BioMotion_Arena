
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point lights
num_points = 15

# Initial positions of the point lights (representing joints)
# Example positions in a simple upright pose
body_positions = np.array([
    [0, 4],     # Head
    [-1, 3],    # Left shoulder
    [1, 3],     # Right shoulder
    [-1, 2],    # Left elbow
    [1, 2],     # Right elbow
    [-1, 1],    # Left wrist
    [1, 1],     # Right wrist
    [-2, 0],    # Left hip
    [2, 0],     # Right hip
    [-2, -3],   # Left knee
    [2, -3],    # Right knee
    [-2, -5],   # Left ankle
    [2, -5],    # Right ankle
    [0, 0],     # Center of mass
    [0, -5],    # Weight center 
    [0, -6]     # Exaggerated position for turning
])

# Prepare scatter plot for the point lights
point_lights, = ax.plot([], [], 'o', color='white', markersize=10)

# Update function for animation
def update(frame):
    angle = frame * np.pi / 30  # Rotation angle
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate and translate the points
    transformed_positions = body_positions @ rotation_matrix
    # Update the position of point lights
    point_lights.set_data(transformed_positions[:, 0], transformed_positions[:, 1])
    return point_lights,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 60), blit=True, interval=100)

plt.show()
