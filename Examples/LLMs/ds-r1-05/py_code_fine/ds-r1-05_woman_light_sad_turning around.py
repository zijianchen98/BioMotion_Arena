
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial configuration for 15 body points in a standing pose (sad posture: head slightly down)
initial_points = np.array([
    [0, 6.5, 0],    # head
    [0, 6, 0],      # neck
    [-0.7, 5.6, 0], # right shoulder
    [0.7, 5.6, 0],  # left shoulder
    [-1.0, 4.8, 0], # right elbow
    [1.0, 4.8, 0],  # left elbow
    [-1.2, 4.0, 0], # right wrist
    [1.2, 4.0, 0],  # left wrist
    [0, 4.8, 0],    # chest/upper back
    [-0.4, 3.8, 0], # right hip
    [0.4, 3.8, 0],  # left hip
    [-0.4, 2.5, 0], # right knee
    [0.4, 2.5, 0],  # left knee
    [-0.4, 0.8, 0], # right ankle
    [0.4, 0.8, 0]   # left ankle
])

fig = plt.figure(figsize=(7, 7), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Remove axes and set plot limits for a clean view
ax.set_axis_off()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 8)
ax.set_zlim(-2, 2)

# Initial scatter plot of points
scatter = ax.scatter(
    initial_points[:, 0],
    initial_points[:, 1],
    initial_points[:, 2],
    c='white',
    s=80
)

# Animation update function
def update(frame):
    # Calculate rotation angle (full turn over 60 frames)
    theta = 2 * np.pi * frame / 60
    # Rotation matrix for Y-axis rotation
    rotation_matrix = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    # Apply rotation to each point
    rotated_points = np.array([rotation_matrix @ p for p in initial_points])
    # Update scatter plot positions
    scatter._offsets3d = (
        rotated_points[:, 0],
        rotated_points[:, 1],
        rotated_points[:, 2]
    )
    return scatter,

# Create the animation
ani = FuncAnimation(
    fig,
    update,
    frames=60,  # Total frames for one complete turn
    interval=50,  # Milliseconds between frames
    blit=False   # Do not use blitting for 3D scatter
)

plt.tight_layout()
plt.show()
