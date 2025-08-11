
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.8, 0.4], [-0.6, 0.4], [-0.4, 0.4], [-0.2, 0.4], [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4],
    [-0.3, 0.2], [0.3, 0.2]
])

# Define the target positions for sitting down
target_positions = np.array([
    [0, -1], [-0.5, -0.7], [0, -0.7], [0.5, -0.7],
    [-0.8, -0.4], [-0.6, -0.4], [-0.4, -0.4], [-0.2, -0.4], [0, -0.4], [0.2, -0.4], [0.4, -0.4], [0.6, -0.4], [0.8, -0.4],
    [-0.3, -0.2], [0.3, -0.2]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Create 15 white point lights
points = []
for i in range(15):
    point, = ax.plot([], [], 'w.', markersize=10)
    points.append(point)

def init():
    for i, point in enumerate(points):
        point.set_data(initial_positions[i][0], initial_positions[i][1])
    return points

def animate(frame):
    t = frame / 100  # Time parameter from 0 to 1
    for i, point in enumerate(points):
        x = (1 - t) * initial_positions[i][0] + t * target_positions[i][0]
        y = (1 - t) * initial_positions[i][1] + t * target_positions[i][1]
        point.set_data(x, y)
    return points

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

plt.show()
