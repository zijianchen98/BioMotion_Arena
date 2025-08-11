
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Right hip
    [0, -3],  # Left knee
    [2, -3],  # Right knee
    [0, -4],  # Left ankle
    [2, -4]   # Right ankle
]

# Define the angles for the happywoman turning around
angles = np.linspace(0, 2 * np.pi, 15)

def update(frame):
    angle = angles[frame]
    new_positions = []
    for pos in positions:
        x, y = pos
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        new_positions.append([new_x, new_y])
    return new_positions

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

ani = FuncAnimation(fig, update, frames=len(angles), init_func=init, blit=True)
plt.show()
