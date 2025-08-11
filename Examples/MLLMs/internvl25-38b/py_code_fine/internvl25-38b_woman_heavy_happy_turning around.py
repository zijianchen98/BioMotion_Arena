
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame, points):
    angle = np.radians(frame * 2)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    points_rotated = np.dot(points, rotation_matrix)
    scat.set_offsets(points_rotated)
    return scat,

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

points = np.array([
    [0, 1],  # Head
    [-1.5, 0.5],  # Right shoulder
    [1.5, 0.5],  # Left shoulder
    [-2, 0],  # Right elbow
    [2, 0],  # Left elbow
    [-3, -2],  # Right hand
    [3, -2],  # Left hand
    [0, -3],  # Torso
    [-1, -4.5],  # Right hip
    [1, -4.5],  # Left hip
    [-2.5, -5],  # Right knee
    [2.5, -5],  # Left knee
    [-3.5, -7],  # Right foot
    [3.5, -7],  # Left foot
    [0, -6]   # Lower torso/abdomen
])

scat = ax.scatter(points[:, 0], points[:, 1], c='white')

ani = animation.FuncAnimation(fig, update, frames=180, fargs=(points,), interval=50, blit=True)
plt.show()
