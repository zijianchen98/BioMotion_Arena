
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
n_points = 15

# Create initial positions for a happy person with heavy weight
initial_positions = np.array([
    [0, 2],   # Head
    [-0.5, 1], [0.5, 1],  # Shoulders
    [-1, 0], [0, 0], [1, 0],  # Hips
    [-0.5, -0.5], [0.5, -0.5],  # Arms
    [-0.5, -1], [0.5, -1],  # Hands
    [-0.5, -2], [0.5, -2],  # Legs
    [-0.25, -3], [0.25, -3],  # Feet
    [-0.25, -4], [0.25, -4],  # Additional feet detail
    [0, -5]  # Base support
])

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-6, 3)
ax.set_facecolor('black')
scatter = ax.scatter([], [], color='white')

def init():
    scatter.set_offsets(np.zeros((n_points, 2)))
    return scatter,

def update(frame):
    rotated_positions = np.dot(initial_positions, rotation_matrix(frame))
    scatter.set_offsets(rotated_positions)
    return scatter,

def rotation_matrix(angle):
    rad = np.radians(angle)
    return np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad), np.cos(rad)]
    ])

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5),
                              init_func=init, blit=True)
plt.axis('off')
plt.show()
