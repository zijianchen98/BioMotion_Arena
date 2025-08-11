
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Define the initial positions of 15 points
points = np.array([
    [0.05, 0.40],
    [0.10, 0.40],
    [0.15, 0.40],
    [0.20, 0.40],
    [0.25, 0.45],
    [0.30, 0.50],
    [0.35, 0.55],
    [0.40, 0.55],
    [0.45, 0.55],
    [0.50, 0.50],
    [0.55, 0.45],
    [0.60, 0.40],
    [0.65, 0.40],
    [0.70, 0.40],
    [0.75, 0.40]
])

# Create a scatter plot for the initial positions
scat = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

def update(frame):
    # Move each point slightly in the forward direction, simulating rolling
    points[:, 1] = np.sin(np.linspace(0, np.pi/2, 16) + frame/30 - np.pi/2)
    scat.set_offsets(points)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=50, interval=30, blit=True)
plt.xticks([])
plt.yticks([])
plt.show()
