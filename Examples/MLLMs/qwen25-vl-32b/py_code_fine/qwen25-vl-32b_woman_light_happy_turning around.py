
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
    [-1, -3], [1, -3]
])

# Function to rotate a point around the origin
def rotate_point(point, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    return np.dot(rotation_matrix, point)

# Function to update the animation frame
def update(frame):
    global positions
    # Rotate each point around the origin
    positions = np.array([rotate_point(p, frame * 2) for p in initial_positions])
    # Update the scatter plot data
    scat.set_offsets(positions)
    return scat,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide the axes
ax.set_aspect('equal')  # Ensure aspect ratio is equal

# Initialize the scatter plot
positions = initial_positions
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=20, blit=True)

# Display the animation
plt.show()
