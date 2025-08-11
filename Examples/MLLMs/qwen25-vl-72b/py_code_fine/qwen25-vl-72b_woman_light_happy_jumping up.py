
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.7, 0.4], [-0.3, 0.4], [0.3, 0.4], [0.7, 0.4],
    [-0.8, 0.1], [-0.4, 0.1], [0, 0.1], [0.4, 0.1], [0.8, 0.1],
    [-0.3, -0.2], [0.3, -0.2]
])

# Define the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', ms=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Calculate new positions for each frame
    amplitude = 0.5 * np.sin(0.1 * i)
    new_positions = initial_positions + np.array([0, amplitude])
    
    x = new_positions[:, 0]
    y = new_positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=200, interval=20, blit=True)

plt.show()
