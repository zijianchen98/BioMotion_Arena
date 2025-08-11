
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the points
num_points = 15
points = np.random.rand(num_points, 2) * 100

def update(frame):
    global points
    # Simulate movement
    for i in range(num_points):
        points[i, 0] -= 0.1  # Move left
        points[i, 1] += 0.1 if np.random.rand() > 0.5 else -0.1  # Move up or down
    
    # Ensure points stay within the plot boundaries
    points[:, 0] = np.clip(points[:, 0], 0, 100)
    points[:, 1] = np.clip(points[:, 1], 0, 100)

fig, ax = plt.subplots()
ax.set_xlim((-10, 110)
ax.set_ylim((-10, 110))
ax.set_aspect('equal')
ax.axis('off')

scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

ani = FuncAnimation(fig, update, frames=np.arange((0, 100), interval=20, blit=False)

plt.show()

