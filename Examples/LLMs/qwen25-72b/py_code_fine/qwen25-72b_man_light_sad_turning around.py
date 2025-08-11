
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the sadman's joints
points = np.array([
    [0, 0],  # Center
    [-0.1, 0.1],  # Left shoulder
    [-0.15, 0.15],  # Left elbow
    [-0.2, 0.1],  # Left hand
    [0.1, 0.1],  # Right shoulder
    [0.15, 0.15],  # Right elbow
    [0.2, 0.1],  # Right hand
    [-0.1, -0.1],  # Left hip
    [-0.15, -0.15],  # Left knee
    [-0.2, -0.1],  # Left foot
    [0.1, -0.1],  # Right hip
    [0.15, -0.15],  # Right knee
    [0.2, -0.1],  # Right foot
    [0, -0.2],  # Head
    [0, -0.3]  # Torso
])

# Define the rotation function
def rotate(points, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation update function
def update(frame):
    angle = frame * np.pi / 180  # Rotate by 1 degree per frame
    new_points = rotate(points, angle)
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=20, blit=True)

# Show the animation
plt.show()
