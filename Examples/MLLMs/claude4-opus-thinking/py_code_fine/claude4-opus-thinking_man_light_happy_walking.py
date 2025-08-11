
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 2)
ax.axis('off')

# Parameters for the walking animation
num_points = 15
walk_speed = 0.1
num_frames = 200

# Define initial positions of the points
points = np.array([
    [0, 1],    # Head
    [-0.5, 0.8], [0.5, 0.8],  # Shoulders
    [-0.5, 0.6], [0.5, 0.6],  # Elbows
    [-0.5, 0.4], [0.5, 0.4],  # Wrists
    [-0.2, 0.0], [0.2, 0.0],  # Hips
    [-0.5, -0.6], [0.5, -0.6],  # Knees
    [-0.3, -1], [0.3, -1],  # Ankles
    [-0.2, -1.3], [0.2, -1.3]  # Feet
])

# Function to update animation
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1, 2)
    ax.axis('off')

    # Animate walking motion
    theta = frame * walk_speed
    walk_offset = np.array([np.sin(theta), np.cos(theta)]) * 0.05
    new_points = points + walk_offset

    # Draw points
    ax.scatter(new_points[:, 0], new_points[:, 1], color='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show animation
plt.show()
