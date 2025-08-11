
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect("equal")
ax.axis("off")

# Create initial positions for the points
points = np.zeros((15, 3))
points[:, 0] += np.array([5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5]) * 0.8
points[:, 1] += np.array([1, 1, 1, 1, 1, 6, 6, 6, -6, -6, -6, 1, 1, 1, 1]) * 0.8
points[:, 2] *= 0.8

# Add points to figure
scat = ax.scatter(points[:, 0], points[:, 1], points[:, 2], color="white")

def update(frame):
    theta = 2 * np.pi * frame / 60
    for i in range(15):
        if i < 7:
            points[i, 0] = 5 + 5 * np.cos(theta[i])
            points[i, 1] = 1 + 1 * np.sin(theta[i])
            points[i, 2] = 0.8 * i * 0.1 + 0.8
        else:
            points[i, 0] = 5 + 5 * np.cos(theta[i-7] + theta[i])
            points[i, 1] = 1 + 1 * np.sin(theta[i-7] + theta[i])
            points[i, 2] = 0.8 * (i-7) * 0.1 + 0.8

    scat.set_offsets(points)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=60, interval=50, blit=True, repeat=False)
plt.show()
