
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                   [1, -1], [2, -2], [3, -3], [4, -4],
                   [-1, 1], [-2, 2], [-3, 3], [-4, 4],
                   [-1, -1], [-2, -2], [-3, -3]])

# Define the rotation matrix
theta = np.radians(5)
c, s = np.cos(theta), np.sin(theta)
rotation_matrix = np.array(((c, -s), (s, c)))

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    global points
    points = np.dot(points, rotation_matrix)
    scat.set_offsets(points)

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)
plt.show()
