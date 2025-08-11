
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                   [1, -1], [2, -2], [3, -3], [4, -4],
                   [-1, 1], [-2, 2], [-3, 3], [-4, 4],
                   [-1, -1], [-2, -2], [-3, -3]])

# Define the movement of the points
def update_points(num):
    global points
    x = points[:, 0]
    y = points[:, 1]
    x += np.sin(np.radians(num))
    y += np.cos(np.radians(num))
    points = np.column_stack((x, y))
    scat.set_offsets(points)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=360, interval=50, blit=True)

plt.show()
