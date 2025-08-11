
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
initial_positions = np.array([
    [0, 1], [-0.5, 0.5], [0.5, 0.5], [-1, 0], [0, 0], [1, 0],
    [-0.5, -0.5], [0.5, -0.5], [-1, -1], [0, -1], [1, -1],
    [-0.5, -1.5], [0.5, -1.5], [0, -2], [0, -3]
])

# Define the target positions for the bowing action
target_positions = np.array([
    [0, 0.5], [-0.5, 0], [0.5, 0], [-1, -0.5], [0, -0.5], [1, -0.5],
    [-0.5, -1], [0.5, -1], [-1, -1.5], [0, -1.5], [1, -1.5],
    [-0.5, -2], [0.5, -2], [0, -2.5], [0, -3.5]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Calculate the current position as a linear interpolation between initial and target positions
    current_positions = (1 - i/100) * initial_positions + (i/100) * target_positions
    x = current_positions[:, 0]
    y = current_positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

plt.show()
