
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
initial_positions = np.array([
    [0, 0], [1, 0], [2, 0],
    [0, 1], [1, 1], [2, 1],
    [0, 2], [1, 2], [2, 2],
    [0, 3], [1, 3], [2, 3],
    [1, 4], [1, 5], [1, 6]
])

# Define the target positions of the points when lying down
target_positions = np.array([
    [0, 0], [1, 0], [2, 0],
    [0, -1], [1, -1], [2, -1],
    [0, -2], [1, -2], [2, -2],
    [0, -3], [1, -3], [2, -3],
    [1, -4], [1, -5], [1, -6]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 3)
ax.set_ylim(-7, 1)

# Create the points
points = []
for i in range(15):
    point, = ax.plot([], [], 'w.', markersize=10)
    points.append(point)

def init():
    for i, point in enumerate(points):
        point.set_data(initial_positions[i][0], initial_positions[i][1])
    return points

def animate(frame):
    t = frame / 100  # Time parameter
    for i, point in enumerate(points):
        x = (1 - t) * initial_positions[i][0] + t * target_positions[i][0]
        y = (1 - t) * initial_positions[i][1] + t * target_positions[i][1]
        point.set_data(x, y)
    return points

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

plt.show()
