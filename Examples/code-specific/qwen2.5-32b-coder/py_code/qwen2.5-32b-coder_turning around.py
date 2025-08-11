
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 60
fps = 30
radius = 0.5

# Initialize points representing a man's joints in a standing position
initial_positions = np.array([
    [0, 0],  # Head
    [0, -0.1],  # Neck
    [0, -0.4],  # Spine
    [-0.1, -0.7],  # Left shoulder
    [-0.2, -1],  # Left elbow
    [-0.2, -1.5],  # Left wrist
    [0.1, -0.7],  # Right shoulder
    [0.2, -1],  # Right elbow
    [0.2, -1.5],  # Right wrist
    [-0.1, -0.4],  # Left hip
    [-0.2, -0.8],  # Left knee
    [-0.2, -1.2],  # Left ankle
    [0.1, -0.4],  # Right hip
    [0.2, -0.8],  # Right knee
    [0.2, -1.2]  # Right ankle
])

def rotate_points(points, angle):
    """Rotate points counterclockwise by a given angle."""
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array(((c, -s), (s, c)))
    return np.dot(points, rotation_matrix)

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

points, = ax.plot([], [], 'o', ms=10, color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    angle = i * 6  # Full rotation in 10 seconds
    rotated_positions = rotate_points(initial_positions, angle)
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
