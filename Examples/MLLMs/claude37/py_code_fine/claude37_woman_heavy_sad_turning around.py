
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
frames = 100
radius = 1.5

# Define the locations of the points (e.g., joints)
# Here, we'll represent a rough skeleton for demonstration
joint_positions = np.array([
    [0, 3],  # Head
    [-0.5, 2], [0.5, 2],  # Shoulders
    [-0.3, 1.5], [0.3, 1.5],  # Elbows
    [-0.5, 1], [0.5, 1],  # Wrists
    [0, 0],  # Center of body
    [-0.3, -0.5], [0.3, -0.5],  # Hips
    [-0.5, -1.5], [0.5, -1.5],  # Knees
    [-0.3, -2], [0.3, -2],  # Ankles
    [0, -3]  # Feet
])

def update(frame):
    plt.clf()
    plt.xlim(-4, 4)
    plt.ylim(-4, 1)
    plt.axis('off')

    angle = frame * (2 * np.pi / frames)  # Rotate over time
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Rotate the joints
    rotated_positions = joint_positions @ rotation_matrix
    plt.scatter(rotated_positions[:, 0], rotated_positions[:, 1], s=100, color='white')

# Setting up the plot for animation
fig = plt.figure(figsize=(6, 4), facecolor='black')

# Create animation
ani = FuncAnimation(fig, update, frames=frames, repeat=True)

# Show the animation
plt.show()
