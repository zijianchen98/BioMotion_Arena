
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [0.2, 0.8], [0.4, 0.8], [0.6, 0.8],
    [0.2, 0.6], [0.4, 0.6], [0.6, 0.6], [0.8, 0.6],
    [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4],
    [0.4, 0.2], [0.6, 0.2], [0.5, 0]
])

# Define the target positions for sitting down
target_positions = np.array([
    [0.5, 0.5], [0.5, 0.4], [0.5, 0.3], [0.5, 0.2],
    [0.4, 0.5], [0.4, 0.4], [0.4, 0.3], [0.4, 0.2],
    [0.6, 0.5], [0.6, 0.4], [0.6, 0.3], [0.6, 0.2],
    [0.5, 0.6], [0.5, 0.7], [0.5, 0.8]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Interpolate between initial and target positions
    t = i / 100.0
    current_positions = (1 - t) * initial_positions + t * target_positions
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=100, interval=20, blit=True)

plt.show()
