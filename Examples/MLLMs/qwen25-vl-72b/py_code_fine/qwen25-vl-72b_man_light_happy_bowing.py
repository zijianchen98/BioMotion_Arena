
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([
    [0, 1], [-0.5, 0.5], [0.5, 0.5], [-1, 0], [0, 0], [1, 0],
    [-0.5, -0.5], [0.5, -0.5], [-1, -1], [0, -1], [1, -1],
    [-0.5, -1.5], [0.5, -1.5], [0, -2], [0, -2.5]
])

# Define the bowing motion
def update_points(num):
    angle = num / 10 * np.pi / 4
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    new_points = np.dot(points, rotation_matrix)
    scat.set_offsets(new_points)
    return scat,

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.set_facecolor('black')
scat = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

ani = animation.FuncAnimation(fig, update_points, frames=range(0, 20), interval=50, blit=True)

plt.show()
