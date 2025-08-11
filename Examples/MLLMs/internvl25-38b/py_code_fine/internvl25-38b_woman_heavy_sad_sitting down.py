
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the 15 points
points = np.array([
    [0.5, 1.0],  # Head
    [0.4, 0.8], [0.6, 0.8],  # Shoulders
    [0.45, 0.7], [0.55, 0.7],  # Arms
    [0.5, 0.5],  # Torso
    [0.4, 0.4], [0.6, 0.4],  # Hips
    [0.35, 0.3], [0.45, 0.3], [0.55, 0.3], [0.65, 0.3],  # Thighs
    [0.3, 0.1], [0.4, 0.1], [0.5, 0.1], [0.6, 0.1], [0.7, 0.1]  # Knees
])

# Define the motion path for sitting down
def update(frame, scatter):
    if frame < 40:
        t = frame / 40.0
        points[:, 1] = points[:, 1] * (1 - t) + np.array([1.0, 0.8, 0.8, 0.7, 0.7, 0.6, 0.4, 0.4, 0.4, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1]) * t
    scatter.set_offsets(points)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
scatter = ax.scatter(points[:, 0], points[:, 1], s=100, color='white')

ani = animation.FuncAnimation(fig, update, frames=70, fargs=(scatter,), interval=50, blit=False)
plt.show()
