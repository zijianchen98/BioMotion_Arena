
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happy woman with heavy weight
# Each row represents a point-light, and the columns represent the x, y, and z coordinates
point_lights = np.array([
    [0.0, 0.5, 0.0],  # Head
    [-0.1, 0.6, 0.1],  # Left shoulder
    [0.1, 0.6, 0.1],  # Right shoulder
    [-0.2, 0.4, 0.1],  # Left elbow
    [0.2, 0.4, 0.1],  # Right elbow
    [-0.3, 0.2, 0.1],  # Left wrist
    [0.3, 0.2, 0.1],  # Right wrist
    [-0.1, 0.5, -0.1],  # Left hip
    [0.1, 0.5, -0.1],  # Right hip
    [-0.2, 0.3, -0.1],  # Left knee
    [0.2, 0.3, -0.1],  # Right knee
    [-0.3, 0.1, -0.1],  # Left ankle
    [0.3, 0.1, -0.1],  # Right ankle
    [0.0, 0.4, 0.2],  # Heavy weight (center of mass)
    [-0.1, 0.3, 0.2],  # Heavy weight (left)
    [0.1, 0.3, 0.2]  # Heavy weight (right)
])

# Define the animation parameters
num_frames = 100
rotation_angle = np.linspace(0, 2 * np.pi, num_frames)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot with the initial point-light positions
points = ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white', s=10)

# Define the animation function
def animate(frame):
    angle = rotation_angle[frame]
    rotated_point_lights = np.copy(point_lights)
    rotated_point_lights[:, 0] = point_lights[:, 0] * np.cos(angle) - point_lights[:, 2] * np.sin(angle)
    rotated_point_lights[:, 2] = point_lights[:, 0] * np.sin(angle) + point_lights[:, 2] * np.cos(angle)
    points.set_offsets(rotated_point_lights[:, :2])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, interval=50)

plt.show()
