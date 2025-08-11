
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                   [1, -1], [2, -2], [3, -3], [4, -4],
                   [-1, 1], [-2, 2], [-3, 3], [-4, 4],
                   [-1, -1], [-2, -2], [-3, -3]])

# Define the forward rolling motion
def update_points(num):
    global points
    angle = num / 10
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    points = np.dot(points, rotation_matrix)
    scat.set_offsets(points)
    return scat,

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

ani = animation.FuncAnimation(fig, update_points, frames=range(0, 360, 10), interval=50, blit=True)
plt.show()
