
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                   [0, 4], [1, 3], [2, 2], [3, 1], [4, 0],
                   [2, 0], [1, 1], [0, 2], [1, 3], [2, 4]])

# Define the forward rolling motion
def update_points(num):
    global points
    angle = num / 10 * np.pi / 4
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    points = np.dot(points, rotation_matrix)
    scatter.set_offsets(points)

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

ani = animation.FuncAnimation(fig, update_points, frames=range(100), interval=50)
plt.show()
