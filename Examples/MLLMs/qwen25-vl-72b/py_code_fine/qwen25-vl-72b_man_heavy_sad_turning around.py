
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
initial_positions = np.array([
    [0, 0], [-1, 1], [1, 1], [-2, 2], [2, 2],
    [-3, 3], [3, 3], [-4, 4], [4, 4], [-5, 5],
    [5, 5], [-6, 6], [6, 6], [-7, 7], [7, 7]
])

# Define the rotation matrix
theta = np.radians(5)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    global initial_positions
    rotated_positions = np.dot(initial_positions, rotation_matrix.T)
    x = rotated_positions[:, 0]
    y = rotated_positions[:, 1]
    points.set_data(x, y)
    initial_positions = rotated_positions
    return points,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.show()
