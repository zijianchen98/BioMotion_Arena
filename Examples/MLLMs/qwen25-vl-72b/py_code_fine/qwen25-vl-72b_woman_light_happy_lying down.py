
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [0.2, 0.8], [0.4, 0.8], [0.6, 0.8],
    [-0.2, 0.6], [0, 0.6], [0.2, 0.6], [0.4, 0.6], [0.6, 0.6], [0.8, 0.6],
    [-0.1, 0.4], [0.1, 0.4], [0.3, 0.4], [0.5, 0.4], [0.7, 0.4]
])

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', ms=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Update the positions of the points for each frame
    new_positions = initial_positions + 0.01 * i * np.random.randn(*initial_positions.shape)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()
