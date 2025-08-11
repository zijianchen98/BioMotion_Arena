
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human figure)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 10], [2, 8], [-2, 8], [4, 6], [-4, 6], [6, 4], [-6, 4],  # Head, shoulders, elbows, wrists
    [0, 0], [2, -2], [-2, -2], [4, -4], [-4, -4], [6, -6], [-6, -6], [0, -8]  # Hips, knees, ankles, torso
])

# Number of frames for one full turn (e.g., 360 degrees)
n_frames = 100
theta = np.linspace(0, 2 * np.pi, n_frames)

# Rotation matrix for turning motion
def rotate_point(point, angle):
    x, y = point
    new_x = x * np.cos(angle) - y * np.sin(angle)
    new_y = x * np.sin(angle) + y * np.cos(angle)
    return [new_x, new_y]

# Initialize figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Scatter plot for point-lights
scat = ax.scatter([], [], c='white', s=50)

def init():
    scat.set_offsets(initial_positions)
    return scat,

def update(frame):
    angle = theta[frame]
    rotated_positions = np.array([rotate_point(p, angle) for p in initial_positions])
    scat.set_offsets(rotated_positions)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, init_func=init, blit=True, interval=50, repeat=True)

plt.show()
