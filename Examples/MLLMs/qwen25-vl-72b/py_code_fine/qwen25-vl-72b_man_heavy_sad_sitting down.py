
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
initial_positions = np.array([
    [0, 1], [-0.5, 0.5], [0.5, 0.5], [-1, 0], [0, 0], [1, 0],
    [-0.5, -0.5], [0.5, -0.5], [-1, -1], [0, -1], [1, -1],
    [-0.5, -1.5], [0.5, -1.5], [0, -2], [0, -2.5]
])

# Define the target positions of the points when sitting down
target_positions = np.array([
    [0, 0.5], [-0.5, 0], [0.5, 0], [-1, -0.5], [0, -0.5], [1, -0.5],
    [-0.5, -1], [0.5, -1], [-1, -1.5], [0, -1.5], [1, -1.5],
    [-0.5, -2], [0.5, -2], [0, -2.5], [0, -3]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Calculate the current position of each point using linear interpolation
    current_positions = initial_positions + (target_positions - initial_positions) * i / 100
    x = current_positions[:, 0]
    y = current_positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

plt.show()
