
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
initial_positions = np.array([
    [0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
    [1, -1], [2, -2], [3, -3], [4, -4],
    [-1, 1], [-2, 2], [-3, 3], [-4, 4],
    [-1, -1], [-2, -2], [-3, -3]
])

# Define the target positions of the points when sitting down
target_positions = np.array([
    [0, -2], [1, -1], [2, 0], [3, 1], [4, 2],
    [1, -3], [2, -4], [3, -5], [4, -6],
    [-1, -1], [-2, 0], [-3, 1], [-4, 2],
    [-1, -3], [-2, -4], [-3, -5]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-7, 5)

# Create 15 white point lights
points = []
for i in range(15):
    point, = ax.plot([], [], 'w.', markersize=10)
    points.append(point)

def init():
    for point, pos in zip(points, initial_positions):
        point.set_data(pos[0], pos[1])
    return points

def animate(i):
    t = i / 100  # Time parameter
    for point, initial, target in zip(points, initial_positions, target_positions):
        pos = (1 - t) * initial + t * target
        point.set_data(pos[0], pos[1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=100, interval=20, blit=True)

plt.show()
