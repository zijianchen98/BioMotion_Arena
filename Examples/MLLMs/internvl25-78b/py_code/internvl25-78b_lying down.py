
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the points
initial_positions = np.array([
    [5, 1], [4, 2], [6, 2], [3, 3], [7, 3],
    [4, 3], [6, 3], [5, 4], [4, 5], [6, 5],
    [5, 6], [4, 7], [6, 7], [5, 8], [5, 9]
])

# Create the point objects
points, = ax.plot([], [], 'wo')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    # Simulate motion
    positions = initial_positions + 0.05 * frame * np.array([0, 1])
    
    x = positions[:, 0]
    y = positions[:, 1]
    
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True, repeat=False)

plt.show()
